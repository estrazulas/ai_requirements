"""
ecosystem-bot-gitlab-glpi.py - Automação de Ecossistema GitLab ↔ GLPI

Bot que sincroniza Merge Requests do GitLab com tickets do GLPI:
- Fluxo 1: MR criado/atualizado → cria/atualiza ticket no GLPI
- Fluxo 2: Status do ticket muda → adiciona comentário no MR

===========================================================================
COMO USAR
===========================================================================

CENÁRIO 1 - Modo local (testes com mocks)
----------------------------------------------------------------------

    python ecosystem-bot-gitlab-glpi.py --local

CENÁRIO 2 - Modo webhook (produção)
----------------------------------------------------------------------

    python ecosystem-bot-gitlab-glpi.py

    Requer:
    - .env configurado com tokens de API
    - Servidor web acessível (Flask)
    - Webhooks configurados no GitLab e GLPI

===========================================================================
"""

import argparse
import json
import os
import sys
from pathlib import Path
from datetime import datetime
import hashlib

try:
    from dotenv import load_dotenv
    env_path = Path(__file__).parent / ".env"
    if env_path.exists():
        load_dotenv(env_path)
except ImportError:
    pass

import requests

# ---------------------------------------------------------------------------
# CONFIGURAÇÃO DE AUDITORIA
# ---------------------------------------------------------------------------

AUDIT_LOG_FILE = os.environ.get("AUDIT_LOG_FILE", "audit_log.jsonl")
PROMPT_VERSION = "1.0.0"  # Versão do NL_PARSER_PROMPT

# ---------------------------------------------------------------------------
# SISTEMA DE AUDITORIA
# ---------------------------------------------------------------------------

class AuditLogger:
    """
    Sistema de auditoria para rastrear criação de tickets.
    Registra logs em formato JSONL (uma linha por evento).
    """
    
    def __init__(self, log_file=AUDIT_LOG_FILE):
        self.log_file = Path(log_file)
    
    def _get_prompt_hash(self):
        """Retorna hash MD5 do prompt para versionamento"""
        return hashlib.md5(NL_PARSER_PROMPT.encode()).hexdigest()[:12]
    
    def log_ticket_creation(self, message, parsed, ticket_id, metadata=None):
        """
        Registra criação de ticket com metadados de auditoria.
        
        Args:
            message: Mensagem original em linguagem natural
            parsed: JSON parseado pela IA
            ticket_id: ID do ticket criado no GLPI
            metadata: Dict com informações adicionais (canal, user_id, etc)
        """
        log_entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "event": "ticket_created",
            "prompt_version": PROMPT_VERSION,
            "prompt_hash": self._get_prompt_hash(),
            "ai_provider": AI_PROVIDER,
            "ai_model": AI_MODEL,
            "message_id": metadata.get("message_id") if metadata else None,
            "channel": metadata.get("channel") if metadata else None,
            "user_id": metadata.get("user_id") if metadata else None,
            "original_message": message,
            "parsed_output": parsed,
            "ticket_id": ticket_id,
            "confidence": parsed.get("confidence"),
            "ticket_type": parsed.get("type"),
            "priority": parsed.get("priority"),
            "assignee": parsed.get("assignee"),
        }
        
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
        
        return log_entry
    
    def log_mr_sync(self, mr_iid, ticket_id, action):
        """
        Registra sincronização MR ↔ ticket.
        
        Args:
            mr_iid: ID do Merge Request
            ticket_id: ID do ticket GLPI
            action: "mr_to_ticket" ou "ticket_to_mr"
        """
        log_entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "event": "mr_sync",
            "action": action,
            "mr_iid": mr_iid,
            "ticket_id": ticket_id,
        }
        
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
        
        return log_entry
    
    def get_logs(self, limit=100, event_type=None):
        """
        Retorna logs de auditoria.
        
        Args:
            limit: Número máximo de logs a retornar
            event_type: Filtrar por tipo de evento (ticket_created, mr_sync)
        
        Returns:
            Lista de logs em ordem cronológica reversa (mais recente primeiro)
        """
        if not self.log_file.exists():
            return []
        
        logs = []
        with open(self.log_file, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    log = json.loads(line.strip())
                    if event_type and log.get("event") != event_type:
                        continue
                    logs.append(log)
                except json.JSONDecodeError:
                    continue
        
        # Retorna mais recentes primeiro
        logs.reverse()
        return logs[:limit]
    
    def get_log_by_ticket_id(self, ticket_id):
        """
        Busca log de criação de um ticket específico.
        
        Args:
            ticket_id: ID do ticket GLPI
        
        Returns:
            Log do ticket ou None se não encontrado
        """
        logs = self.get_logs(event_type="ticket_created")
        for log in logs:
            if log.get("ticket_id") == ticket_id:
                return log
        return None


# Instância global do logger
audit_logger = AuditLogger()

# ---------------------------------------------------------------------------
# CONFIGURAÇÃO DE IA (OPCIONAL)
# ---------------------------------------------------------------------------

AI_PROVIDER = os.environ.get("AI_PROVIDER", "openai")  # openai ou anthropic
AI_MODEL = os.environ.get("AI_MODEL", "gpt-4o-mini")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

# ---------------------------------------------------------------------------
# CONFIGURAÇÃO
# ---------------------------------------------------------------------------

CONFIG = {
    "gitlab_url": os.environ.get("GITLAB_URL", "https://git.ifsc.edu.br"),
    "gitlab_token": os.environ.get("GITLAB_TOKEN", ""),
    "gitlab_project_id": os.environ.get("GITLAB_PROJECT_ID", ""),
    
    "glpi_url": os.environ.get("GLPI_URL", "https://glpi.ifsc.edu.br/apirest.php"),
    "glpi_app_token": os.environ.get("GLPI_APP_TOKEN", ""),
    "glpi_user_token": os.environ.get("GLPI_USER_TOKEN", ""),
    
    # Mapeamento de status GitLab → GLPI
    "status_mapping": {
        "opened": "1",      # New
        "closed": "6",      # Solved
        "merged": "6",      # Solved
    },
    
    # Categoria padrão para tickets criados automaticamente
    "default_category": "Development",
}

# ---------------------------------------------------------------------------
# NL PARSER PROMPT (adaptado do nl-to-workflow-prompt.md do professor)
# ---------------------------------------------------------------------------

NL_PARSER_PROMPT = """Você é um NL to Workflow Parser - um sistema de extração de entidades embarcado
em um bot de gestão de projetos. Seu mandato é converter mensagens em linguagem
natural (chat, email, notas) em tickets estruturados prontos para criação no GLPI.

Você não é um assistente de conversação. Você é um parser. Não responda em prosa.
Retorne sempre JSON válido, sem texto antes ou depois do bloco JSON.

---------------------------------------------
CAMPOS DO OUTPUT
---------------------------------------------

Para cada mensagem, extraia os seguintes campos:

{{
  "type":           "bug" | "task" | "feature" | "question" | "decision",
  "title":          "string - título conciso do ticket, máximo 80 caracteres",
  "priority":       "1" | "2" | "3" | "4" | "5" | "6",
  "assignee":       "string | null | [A DEFINIR]",
  "dueDate":        "string | null - descrição relativa ou data",
  "category":       "string | null - categoria do ticket (Desenvolvimento, Infraestrutura, Suporte, etc)",
  "requestedBy":    "string | null - quem solicitou, se mencionado",
  "reason":         "string | null - contexto de negócio ou justificativa",
  "description":    "string - expansão contextual da mensagem original",
  "tags":           ["array", "de", "strings", "- palavras-chave relevantes"],
  "actionRequired": "string | null - instrução para o humano antes de criar o ticket",
  "confidence":     "high" | "medium" | "low" - confiança do parser no output,
  "rawMessage":     "string - mensagem original sem alteração"
}}

---------------------------------------------
REGRAS DE EXTRAÇÃO
---------------------------------------------

TYPE - classifique assim:
  bug:      relato de comportamento incorreto ou inesperado do sistema
  task:     ação de trabalho clara que precisa ser executada
  feature:  nova capacidade ou melhoria solicitada
  question: pergunta sem ação implícita - NÃO crie ticket automaticamente
  decision: registro de uma decisão já tomada que precisa ser documentada

PRIORITY - mapeie para valores GLPI:
  1: Very high (crítico, bloqueador)
  2: High (urgente, impacto significativo)
  3: Medium (relevante sem urgência)
  4: Low (sugestão, cosmético)
  5: Very low (nice-to-have)
  6: None (não classificado)

ASSIGNEE - regras:
  - Se um nome é mencionado como responsável direto, use o nome
  - Se a mensagem pede voluntário ("alguém pode?", "quem pega?"), use "[A DEFINIR]"
    e adicione em actionRequired: "Confirmar assignee antes de criar o ticket"
  - Se nenhum responsável é mencionado, use null

DUEDATE - inferência:
  - "antes do fim do mês"    -> "[fim do mês corrente]"
  - "essa sprint"            -> "[fim da sprint corrente]"
  - "antes do deploy de sexta" -> "[próxima sexta-feira]"
  - Se não mencionado        -> null

DESCRIPTION - expansão:
  Não copie a mensagem original. Expanda com:
  1. O problema ou ação em termos técnicos
  2. Os pontos de investigação mais prováveis (para bugs)
  3. O impacto operacional implícito

CONFIDENCE - classifique assim:
  high:   mensagem clara, campos principais identificados sem ambiguidade
  medium: pelo menos um campo foi inferido sem base explícita na mensagem
  low:    mensagem muito vaga, múltiplas interpretações possíveis

---------------------------------------------
CASOS ESPECIAIS
---------------------------------------------

MENSAGEM COM MÚLTIPLAS AÇÕES:
  Se a mensagem contém ações para pessoas diferentes, retorne um array de tickets:
  [{{ ticket1 }}, {{ ticket2 }}]
  Adicione em cada ticket: "linkedMessage": "Gerado da mesma mensagem"

MENSAGEM QUE É UMA PERGUNTA:
  Retorne:
  {{
    "type": "question",
    "actionRequired": false,
    "suggestedAction": "Criar ticket de investigação? Aguardando confirmação.",
    "rawMessage": "..."
  }}
  Não crie ticket de tarefa a partir de uma pergunta sem confirmação.

MENSAGEM SEM CONTEXTO SUFICIENTE:
  Se a mensagem tem menos de 10 palavras úteis ou não permite inferir tipo e título:
  {{
    "type": "unknown",
    "confidence": "low",
    "actionRequired": "Mensagem insuficiente para criar ticket. Solicitar detalhes ao autor.",
    "rawMessage": "..."
  }}

---------------------------------------------
RESTRIÇÕES
---------------------------------------------

- Nunca invente assignees não mencionados na mensagem
- Nunca invente datas sem base na mensagem
- Nunca retorne texto fora do bloco JSON
- Se a confiança for "low", sempre preencha actionRequired com instrução clara
- Ao final de todo output, não adicione nenhum comentário - só o JSON

---------------------------------------------
MENSAGEM PARA PROCESSAR
---------------------------------------------

{message}
"""

# ---------------------------------------------------------------------------
# CLIENTE DE IA (NL PARSER)
# ---------------------------------------------------------------------------

def parse_natural_language(message: str) -> dict:
    """
    Converte mensagem em linguagem natural em JSON estruturado usando IA.
    Similar ao parseNaturalLanguage() do bot do professor.
    
    Args:
        message: Mensagem em linguagem natural para processar
        
    Returns:
        dict: JSON estruturado com campos extraídos (type, title, priority, etc)
    """
    prompt = NL_PARSER_PROMPT.replace("{message}", message)
    
    if AI_PROVIDER == "anthropic":
        if not ANTHROPIC_API_KEY:
            raise ValueError("ANTHROPIC_API_KEY não configurada")
        
        import anthropic
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        
        response = client.messages.create(
            model=AI_MODEL,
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}],
        )
        
        text = response.content[0].text
    
    else:  # openai
        if not OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY não configurada")
        
        import openai
        client = openai.OpenAI(api_key=OPENAI_API_KEY)
        
        response = client.chat.completions.create(
            model=AI_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )
        
        text = response.choices[0].message.content
    
    # Extrai JSON da resposta (modelo pode adicionar texto explicativo)
    import re
    json_match = re.search(r'\{[\s\S]*\}', text)
    if not json_match:
        raise ValueError("Parser não retornou JSON válido")
    
    return json.loads(json_match.group(0))


# ---------------------------------------------------------------------------
# CLIENTE GITLAB
# ---------------------------------------------------------------------------

class GitLabClient:
    def __init__(self, url, token, project_id):
        self.base_url = f"{url}/api/v4"
        self.headers = {"PRIVATE-TOKEN": token}
        self.project_id = project_id
    
    def get_merge_request(self, mr_iid):
        """Busca informações de um Merge Request"""
        endpoint = f"{self.base_url}/projects/{self.project_id}/merge_requests/{mr_iid}"
        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def add_mr_comment(self, mr_iid, comment):
        """Adiciona comentário a um Merge Request"""
        endpoint = f"{self.base_url}/projects/{self.project_id}/merge_requests/{mr_iid}/notes"
        data = {"body": comment}
        response = requests.post(endpoint, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()
    
    def get_mr_comments(self, mr_iid):
        """Busca comentários de um MR"""
        endpoint = f"{self.base_url}/projects/{self.project_id}/merge_requests/{mr_iid}/notes"
        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()


# ---------------------------------------------------------------------------
# CLIENTE GLPI
# ---------------------------------------------------------------------------

class GLPIClient:
    def __init__(self, url, app_token, user_token):
        self.base_url = url
        self.app_token = app_token
        self.user_token = user_token
        self.session_token = None
    
    def init_session(self):
        """Inicializa sessão no GLPI"""
        headers = {
            "Authorization": f"user_token {self.user_token}",
            "App-Token": self.app_token,
        }
        response = requests.get(f"{self.base_url}/initSession", headers=headers)
        response.raise_for_status()
        self.session_token = response.json().get("session_token")
        return self.session_token
    
    def kill_session(self):
        """Encerra sessão no GLPI"""
        if not self.session_token:
            return
        headers = self._get_headers()
        requests.get(f"{self.base_url}/killSession", headers=headers)
        self.session_token = None
    
    def _get_headers(self):
        """Retorna headers com token de sessão"""
        return {
            "Session-Token": self.session_token,
            "App-Token": self.app_token,
            "Content-Type": "application/json",
        }
    
    def create_ticket(self, title, description, category_id=None, status=1):
        """Cria ticket no GLPI"""
        if not self.session_token:
            self.init_session()
        
        headers = self._get_headers()
        data = {
            "input": {
                "name": title,
                "content": description,
                "status": status,
                "itilcategories_id": category_id,
            }
        }
        
        response = requests.post(
            f"{self.base_url}/Ticket",
            headers=headers,
            json=data
        )
        response.raise_for_status()
        return response.json()
    
    def update_ticket(self, ticket_id, status=None, add_comment=None):
        """Atualiza ticket no GLPI"""
        if not self.session_token:
            self.init_session()
        
        headers = self._get_headers()
        data = {"input": {"id": ticket_id}}
        
        if status:
            data["input"]["status"] = status
        
        response = requests.put(
            f"{self.base_url}/Ticket/{ticket_id}",
            headers=headers,
            json=data
        )
        response.raise_for_status()
        
        if add_comment:
            self.add_followup(ticket_id, add_comment)
        
        return response.json()
    
    def add_followup(self, ticket_id, content):
        """Adiciona follow-up (comentário) ao ticket"""
        if not self.session_token:
            self.init_session()
        
        headers = self._get_headers()
        data = {
            "input": {
                "items_id": ticket_id,
                "itemtype": "Ticket",
                "content": content,
            }
        }
        
        response = requests.post(
            f"{self.base_url}/ITILFollowup",
            headers=headers,
            json=data
        )
        response.raise_for_status()
        return response.json()
    
    def get_ticket(self, ticket_id):
        """Busca informações de um ticket"""
        if not self.session_token:
            self.init_session()
        
        headers = self._get_headers()
        response = requests.get(
            f"{self.base_url}/Ticket/{ticket_id}",
            headers=headers
        )
        response.raise_for_status()
        return response.json()


# ---------------------------------------------------------------------------
# BOT DE SINCRONIZAÇÃO
# ---------------------------------------------------------------------------

class EcosystemBot:
    def __init__(self, config):
        self.config = config
        self.gitlab = GitLabClient(
            config["gitlab_url"],
            config["gitlab_token"],
            config["gitlab_project_id"]
        )
        self.glpi = GLPIClient(
            config["glpi_url"],
            config["glpi_app_token"],
            config["glpi_user_token"]
        )
    
    def handle_mr_event(self, mr_iid):
        """
        Fluxo 1: MR criado/atualizado → cria/atualiza ticket no GLPI
        """
        print(f"\n{'='*60}")
        print(f"PROCESSANDO MR !{mr_iid}")
        print(f"{'='*60}\n")
        
        # Busca informações do MR
        mr = self.gitlab.get_merge_request(mr_iid)
        print(f"Título: {mr['title']}")
        print(f"Status: {mr['state']}")
        print(f"Autor: {mr['author']['name']}")
        print()
        
        # Verifica se já existe ticket para este MR
        ticket_id = self._find_ticket_for_mr(mr_iid)
        
        if ticket_id:
            # Atualiza ticket existente
            print(f"Ticket existente encontrado: #{ticket_id}")
            glpi_status = self.config["status_mapping"].get(mr["state"], "1")
            
            comment = (
                f"MR atualizado no GitLab:\n\n"
                f"**Status:** {mr['state']}\n"
                f"**Título:** {mr['title']}\n"
                f"**URL:** {mr['web_url']}\n"
            )
            
            self.glpi.update_ticket(ticket_id, status=glpi_status, add_comment=comment)
            print(f"✅ Ticket #{ticket_id} atualizado\n")
            
        else:
            # Cria novo ticket
            print("Criando novo ticket no GLPI...")
            
            title = f"[MR !{mr_iid}] {mr['title']}"
            description = (
                f"**Merge Request do GitLab**\n\n"
                f"**Título:** {mr['title']}\n"
                f"**Autor:** {mr['author']['name']}\n"
                f"**Status:** {mr['state']}\n"
                f"**Branch:** {mr['source_branch']} → {mr['target_branch']}\n"
                f"**URL:** {mr['web_url']}\n\n"
                f"**Descrição:**\n{mr.get('description', 'Sem descrição')}\n"
            )
            
            glpi_status = self.config["status_mapping"].get(mr["state"], "1")
            
            ticket = self.glpi.create_ticket(
                title=title,
                description=description,
                status=glpi_status
            )
            
            ticket_id = ticket["id"]
            print(f"✅ Ticket criado: #{ticket_id}\n")
            
            # Adiciona comentário no MR com link do ticket
            comment = (
                f"🎫 Ticket GLPI criado automaticamente: **#{ticket_id}**\n\n"
                f"Este MR está sendo rastreado no GLPI para controle de mudanças."
            )
            self.gitlab.add_mr_comment(mr_iid, comment)
            print(f"✅ Comentário adicionado ao MR !{mr_iid}\n")
        
        return ticket_id
    
    def handle_ticket_event(self, ticket_id, new_status=None, comment=None):
        """
        Fluxo 2: Status do ticket muda → adiciona comentário no MR
        """
        print(f"\n{'='*60}")
        print(f"PROCESSANDO TICKET #{ticket_id}")
        print(f"{'='*60}\n")
        
        # Busca informações do ticket
        ticket = self.glpi.get_ticket(ticket_id)
        print(f"Título: {ticket['name']}")
        print(f"Status: {ticket['status']}")
        print()
        
        # Extrai MR IID do título (formato: [MR !123] ...)
        mr_iid = self._extract_mr_iid(ticket["name"])
        
        if not mr_iid:
            print("⚠️  Ticket não está vinculado a um MR (título não contém [MR !xxx])")
            return None
        
        print(f"MR vinculado: !{mr_iid}")
        
        # Monta mensagem para o MR
        message_parts = [f"🎫 **Atualização do ticket GLPI #{ticket_id}**\n"]
        
        if new_status:
            status_names = {
                "1": "New",
                "2": "Processing",
                "3": "Pending",
                "4": "Solved",
                "5": "Closed",
                "6": "Solved",
            }
            status_name = status_names.get(str(new_status), f"Status {new_status}")
            message_parts.append(f"**Status alterado para:** {status_name}")
        
        if comment:
            message_parts.append(f"\n**Comentário:** {comment}")
        
        message = "\n".join(message_parts)
        
        # Adiciona comentário no MR
        self.gitlab.add_mr_comment(mr_iid, message)
        print(f"✅ Comentário adicionado ao MR !{mr_iid}\n")
        
        return mr_iid
    
    def _find_ticket_for_mr(self, mr_iid):
        """
        Busca ticket no GLPI vinculado ao MR
        (Em produção, implementaria busca por título ou campo personalizado)
        """
        # Simulação: em produção, buscaria tickets com título contendo [MR !{mr_iid}]
        # ou usaria campo personalizado do GLPI para armazenar MR IID
        return None
    
    def _extract_mr_iid(self, title):
        """
        Extrai MR IID do título do ticket
        Formato esperado: [MR !123] Descrição
        """
        import re
        match = re.search(r'\[MR !(\d+)\]', title)
        return int(match.group(1)) if match else None
    
    def close(self):
        """Encerra sessões"""
        self.glpi.kill_session()


# ---------------------------------------------------------------------------
# MODO PARSE NL (TESTE DE LINGUAGEM NATURAL)
# ---------------------------------------------------------------------------

def run_parse_demo(message: str):
    """Executa demonstração do parser de linguagem natural"""
    print("\n" + "="*60)
    print("MODO PARSE NL - TESTE DE LINGUAGEM NATURAL")
    print("="*60 + "\n")
    
    print(f"Mensagem original: {message}\n")
    print("Processando com IA...")
    
    try:
        parsed = parse_natural_language(message)
        
        print("\n" + "-"*60)
        print("JSON PARSEADO:")
        print("-"*60)
        print(json.dumps(parsed, indent=2, ensure_ascii=False))
        
        print("\n" + "-"*60)
        print("INTERPRETAÇÃO:")
        print("-"*60)
        print(f"Tipo: {parsed.get('type', 'N/A')}")
        print(f"Título: {parsed.get('title', 'N/A')}")
        print(f"Prioridade: {parsed.get('priority', 'N/A')}")
        print(f"Assignee: {parsed.get('assignee', 'N/A')}")
        print(f"Confiança: {parsed.get('confidence', 'N/A')}")
        
        if parsed.get('actionRequired'):
            print(f"\n⚠️  Ação necessária: {parsed['actionRequired']}")
        
        if parsed.get('type') == 'question':
            print("\n❓ Esta é uma pergunta - não crie ticket automaticamente")
        elif parsed.get('confidence') == 'low':
            print("\n⚠️  Confiança baixa - revise antes de criar ticket")
        else:
            print("\n✅ Pronto para criar ticket no GLPI")
        
    except Exception as e:
        print(f"\n❌ Erro ao processar mensagem: {e}")
    
    print("\n" + "="*60 + "\n")


def run_simulate_demo(message: str, channel: str = "#teste", user_id: str = "usuario.teste"):
    """
    Executa demonstração do parser com registro de log de auditoria.
    Simula criação de ticket sem chamar API real do GLPI.
    """
    print("\n" + "="*60)
    print("MODO SIMULATE - TESTE COM AUDITORIA")
    print("="*60 + "\n")
    
    print(f"Mensagem original: {message}")
    print(f"Canal: {channel}")
    print(f"User ID: {user_id}")
    print()
    print("Processando com IA...")
    
    try:
        # 1. Parse da mensagem
        parsed = parse_natural_language(message)
        
        print("\n✅ Parsing concluído")
        print(f"   Tipo: {parsed.get('type')}")
        print(f"   Título: {parsed.get('title')}")
        print(f"   Confiança: {parsed.get('confidence')}")
        
        # 2. Simula criação de ticket (ID fictício)
        simulated_ticket_id = 9999
        
        print(f"\n📝 Simulando criação de ticket #{simulated_ticket_id}...")
        
        # 3. Registra log de auditoria
        audit_metadata = {
            "channel": channel,
            "user_id": user_id,
            "message_id": f"msg_{datetime.now().strftime('%Y%m%d%H%M%S')}",
        }
        
        audit_log = audit_logger.log_ticket_creation(
            message=message,
            parsed=parsed,
            ticket_id=simulated_ticket_id,
            metadata=audit_metadata
        )
        
        print(f"✅ Log de auditoria registrado")
        print(f"   Arquivo: {audit_logger.log_file}")
        print(f"   Timestamp: {audit_log['timestamp']}")
        print(f"   Prompt version: {audit_log['prompt_version']}")
        print(f"   Prompt hash: {audit_log['prompt_hash']}")
        
        # 4. Mostra o log completo
        print("\n" + "-"*60)
        print("LOG DE AUDITORIA COMPLETO:")
        print("-"*60)
        print(json.dumps(audit_log, indent=2, ensure_ascii=False))
        
        # 5. Demonstra consulta
        print("\n" + "-"*60)
        print("CONSULTANDO LOG VIA API (simulação):")
        print("-"*60)
        
        retrieved_log = audit_logger.get_log_by_ticket_id(simulated_ticket_id)
        if retrieved_log:
            print(f"✅ Log encontrado para ticket #{simulated_ticket_id}")
            print(f"   Mensagem original: {retrieved_log['original_message']}")
            print(f"   Canal: {retrieved_log.get('channel')}")
            print(f"   User ID: {retrieved_log.get('user_id')}")
            print(f"   Prompt version: {retrieved_log.get('prompt_version')}")
            print(f"   AI Provider: {retrieved_log.get('ai_provider')}")
            print(f"   AI Model: {retrieved_log.get('ai_model')}")
        
        print("\n" + "="*60)
        print("Para consultar logs em produção:")
        print(f"  curl http://localhost:5000/audit?ticket_id={simulated_ticket_id}")
        print(f"  cat {audit_logger.log_file}")
        print("="*60 + "\n")
        
    except Exception as e:
        print(f"\n❌ Erro ao processar mensagem: {e}")
        import traceback
        traceback.print_exc()


# ---------------------------------------------------------------------------
# MODO LOCAL (TESTES COM MOCKS)
# ---------------------------------------------------------------------------

def run_local_demo():
    """Executa demonstração local com dados simulados"""
    print("\n" + "="*60)
    print("MODO LOCAL - DEMONSTRAÇÃO COM MOCKS")
    print("="*60 + "\n")
    
    # Carrega mocks
    mock_mr_path = Path(__file__).parent / "mr-mock.json"
    mock_ticket_path = Path(__file__).parent / "ticket-mock.json"
    
    if not mock_mr_path.exists() or not mock_ticket_path.exists():
        print("❌ Arquivos de mock não encontrados:")
        print(f"   - {mock_mr_path}")
        print(f"   - {mock_ticket_path}")
        return
    
    mr_mock = json.loads(mock_mr_path.read_text())
    ticket_mock = json.loads(mock_ticket_path.read_text())
    
    print("CENÁRIO 1: MR criado → cria ticket no GLPI")
    print("-" * 60)
    print(f"MR !{mr_mock['iid']}: {mr_mock['title']}")
    print(f"Status: {mr_mock['state']}")
    print(f"Autor: {mr_mock['author']['name']}")
    print()
    print("Ações que seriam executadas:")
    print("  1. Buscar MR no GitLab")
    print("  2. Verificar se já existe ticket vinculado")
    print("  3. Criar ticket no GLPI com título: [MR !42] ...")
    print("  4. Adicionar comentário no MR com link do ticket")
    print()
    
    print("CENÁRIO 2: Status do ticket muda → notifica no MR")
    print("-" * 60)
    print(f"Ticket #{ticket_mock['id']}: {ticket_mock['name']}")
    print(f"Novo status: {ticket_mock['status']}")
    print()
    print("Ações que seriam executadas:")
    print("  1. Buscar ticket no GLPI")
    print("  2. Extrair MR IID do título: !42")
    print("  3. Adicionar comentário no MR com atualização do ticket")
    print()
    
    print("="*60)
    print("Para testar em produção, configure o .env e execute:")
    print("  python ecosystem-bot-gitlab-glpi.py")
    print("="*60 + "\n")


# ---------------------------------------------------------------------------
# MODO WEBHOOK (PRODUÇÃO)
# ---------------------------------------------------------------------------

def run_webhook_server():
    """Inicia servidor Flask para receber webhooks"""
    try:
        from flask import Flask, request, jsonify
    except ImportError:
        print("❌ Flask não instalado. Execute: pip install flask")
        return
    
    app = Flask(__name__)
    bot = EcosystemBot(CONFIG)
    
    @app.route("/webhook/gitlab", methods=["POST"])
    def gitlab_webhook():
        """Recebe webhooks do GitLab (MR events)"""
        data = request.json
        event_type = data.get("object_kind")
        
        if event_type == "merge_request":
            mr_iid = data["object_attributes"]["iid"]
            try:
                ticket_id = bot.handle_mr_event(mr_iid)
                return jsonify({"status": "ok", "ticket_id": ticket_id})
            except Exception as e:
                return jsonify({"status": "error", "message": str(e)}), 500
        
        return jsonify({"status": "ignored"})
    
    @app.route("/webhook/glpi", methods=["POST"])
    def glpi_webhook():
        """Recebe webhooks do GLPI (ticket updates)"""
        data = request.json
        ticket_id = data.get("id")
        new_status = data.get("status")
        comment = data.get("comment")
        
        if ticket_id:
            try:
                mr_iid = bot.handle_ticket_event(ticket_id, new_status, comment)
                return jsonify({"status": "ok", "mr_iid": mr_iid})
            except Exception as e:
                return jsonify({"status": "error", "message": str(e)}), 500
        
        return jsonify({"status": "ignored"})
    
    @app.route("/webhook/chat", methods=["POST"])
    def chat_webhook():
        """
        Recebe mensagens em linguagem natural e cria tickets no GLPI.
        Similar ao listener do bot do professor (Slack → Jira).
        
        Exemplo de uso:
            curl -X POST http://localhost:5000/webhook/chat \
              -H "Content-Type: application/json" \
              -d '{"message": "Preciso investigar bug no login OAuth"}'
        """
        data = request.json
        message = data.get("message", "")
        
        if not message:
            return jsonify({"status": "error", "message": "Campo 'message' é obrigatório"}), 400
        
        try:
            # 1. Parse da mensagem com IA
            parsed = parse_natural_language(message)
            
            # 2. Verifica se é uma pergunta ou mensagem insuficiente
            if parsed.get("type") == "question":
                return jsonify({
                    "status": "question",
                    "parsed": parsed,
                    "message": "Esta é uma pergunta. Confirme se deseja criar ticket de investigação."
                })
            
            if parsed.get("confidence") == "low":
                return jsonify({
                    "status": "low_confidence",
                    "parsed": parsed,
                    "message": "Confiança baixa. Revise a mensagem antes de criar ticket."
                })
            
            # 3. Cria ticket no GLPI (se confiança for alta/média)
            title = parsed.get("title", "Ticket sem título")
            description = parsed.get("description", message)
            priority = int(parsed.get("priority", 3))
            
            ticket = bot.glpi.create_ticket(
                title=title,
                description=description,
                status=1  # New
            )
            
            ticket_id = ticket["id"]
            
            # 4. Adiciona tags e metadata como follow-up
            metadata = (
                f"**Metadados extraídos por IA:**\n"
                f"- Tipo: {parsed.get('type', 'N/A')}\n"
                f"- Prioridade: {parsed.get('priority', 'N/A')}\n"
                f"- Assignee: {parsed.get('assignee', 'N/A')}\n"
                f"- Confiança: {parsed.get('confidence', 'N/A')}\n"
                f"- Mensagem original: {message}"
            )
            
            if parsed.get("tags"):
                metadata += f"\n- Tags: {', '.join(parsed['tags'])}"
            
            bot.glpi.add_followup(ticket_id, metadata)
            
            # 5. Registra log de auditoria
            audit_metadata = {
                "channel": data.get("channel"),
                "user_id": data.get("user_id"),
                "message_id": data.get("message_id"),
            }
            audit_log = audit_logger.log_ticket_creation(
                message=message,
                parsed=parsed,
                ticket_id=ticket_id,
                metadata=audit_metadata
            )
            
            return jsonify({
                "status": "ok",
                "ticket_id": ticket_id,
                "parsed": parsed,
                "audit": {
                    "log_id": audit_log.get("timestamp"),
                    "prompt_version": audit_log.get("prompt_version"),
                    "prompt_hash": audit_log.get("prompt_hash"),
                },
                "message": f"Ticket #{ticket_id} criado com sucesso"
            })
            
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500
    
    @app.route("/health", methods=["GET"])
    def health():
        """Endpoint de health check"""
        return jsonify({"status": "ok", "service": "ecosystem-bot"})
    
    @app.route("/audit", methods=["GET"])
    def audit():
        """
        Endpoint para consultar logs de auditoria.
        
        Parâmetros:
            - limit: Número máximo de logs (default: 100)
            - event_type: Filtrar por tipo (ticket_created, mr_sync)
            - ticket_id: Buscar log específico de um ticket
        
        Exemplo de uso:
            curl http://localhost:5000/audit?limit=10
            curl http://localhost:5000/audit?ticket_id=1234
            curl http://localhost:5000/audit?event_type=ticket_created
        """
        limit = request.args.get("limit", 100, type=int)
        event_type = request.args.get("event_type")
        ticket_id = request.args.get("ticket_id", type=int)
        
        try:
            if ticket_id:
                # Busca log específico de um ticket
                log = audit_logger.get_log_by_ticket_id(ticket_id)
                if log:
                    return jsonify({
                        "status": "ok",
                        "found": True,
                        "log": log
                    })
                else:
                    return jsonify({
                        "status": "ok",
                        "found": False,
                        "message": f"Nenhum log encontrado para ticket #{ticket_id}"
                    }), 404
            else:
                # Lista logs com filtros
                logs = audit_logger.get_logs(limit=limit, event_type=event_type)
                return jsonify({
                    "status": "ok",
                    "count": len(logs),
                    "logs": logs
                })
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500
    
    print("\n" + "="*60)
    print("SERVIDOR WEBHOOK INICIADO")
    print("="*60)
    print("Endpoints:")
    print("  POST /webhook/gitlab  - Recebe eventos de MR do GitLab")
    print("  POST /webhook/glpi    - Recebe atualizações de ticket do GLPI")
    print("  POST /webhook/chat    - Recebe mensagens em linguagem natural (NL Parser)")
    print("  GET  /health          - Health check")
    print("  GET  /audit           - Consulta logs de auditoria")
    print()
    print("Configure os webhooks:")
    print(f"  GitLab: {CONFIG['gitlab_url']}/hooks")
    print(f"  GLPI: Setup > Notifications > Webhook")
    print()
    print("Exemplo de uso do NL Parser:")
    print('  curl -X POST http://localhost:5000/webhook/chat \\')
    print('    -H "Content-Type: application/json" \\')
    print('    -d \'{"message": "Preciso investigar bug no login OAuth"}\'')
    print()
    print("Exemplo de consulta de auditoria:")
    print('  curl http://localhost:5000/audit?limit=10')
    print('  curl http://localhost:5000/audit?ticket_id=1234')
    print("="*60 + "\n")
    
    app.run(host="0.0.0.0", port=5000, debug=False)


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bot de sincronização GitLab ↔ GLPI")
    parser.add_argument(
        "--local",
        action="store_true",
        help="Modo local: demonstra fluxo com mocks (sem APIs reais)"
    )
    parser.add_argument(
        "--parse",
        type=str,
        metavar="MENSAGEM",
        help="Modo NL Parser: converte mensagem em linguagem natural em JSON estruturado"
    )
    parser.add_argument(
        "--simulate",
        type=str,
        metavar="MENSAGEM",
        help="Modo simulação: parse + registro de log de auditoria (sem criar ticket real)"
    )
    args = parser.parse_args()
    
    if args.parse:
        # Modo NL Parser
        if not OPENAI_API_KEY and not ANTHROPIC_API_KEY:
            print("❌ Chave de API de IA não configurada.")
            print("   Configure OPENAI_API_KEY ou ANTHROPIC_API_KEY no arquivo .env")
            sys.exit(1)
        run_parse_demo(args.parse)
    elif args.simulate:
        # Modo simulação com auditoria
        if not OPENAI_API_KEY and not ANTHROPIC_API_KEY:
            print("❌ Chave de API de IA não configurada.")
            print("   Configure OPENAI_API_KEY ou ANTHROPIC_API_KEY no arquivo .env")
            sys.exit(1)
        run_simulate_demo(args.simulate)
    elif args.local:
        run_local_demo()
    else:
        # Verifica se tokens estão configurados
        if not CONFIG["gitlab_token"] or not CONFIG["glpi_user_token"]:
            print("❌ Tokens de API não configurados.")
            print("   Configure o arquivo .env ou use --local para demonstração.")
            sys.exit(1)
        
        run_webhook_server()
