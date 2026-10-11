# Módulo 9 - Automação de Ecossistema: GitLab ↔ GLPI

> **Resolução adaptada para IFSC** - Bot de sincronização entre GitLab e GLPI

## Visão Geral

Este módulo implementa um bot de automação de ecossistema que sincroniza Merge Requests do GitLab com tickets do GLPI, similar ao exemplo do professor com Slack ↔ Jira.

### Fluxos Implementados

#### Fluxo 1: GitLab → GLPI (MR cria/atualiza ticket)

Quando um Merge Request é criado ou atualizado no GitLab:
1. Webhook do GitLab dispara evento para o bot
2. Bot busca informações do MR via API
3. Cria ticket no GLPI com título formatado: `[MR !42] Título do MR`
4. Adiciona comentário no MR com link do ticket GLPI

**Exemplo:**
```
MR !42 criado: "Implementar validação de CPF"
  ↓
Ticket #1234 criado no GLPI
  ↓
Comentário no MR: "🎫 Ticket GLPI criado: #1234"
```

#### Fluxo 2: GLPI → GitLab (ticket notifica no MR)

Quando o status de um ticket muda no GLPI:
1. Webhook do GLPI dispara evento para o bot
2. Bot busca informações do ticket
3. Extrai MR IID do título do ticket
4. Adiciona comentário no MR com atualização do status

**Exemplo:**
```
Ticket #1234 muda para "Em andamento"
  ↓
Bot identifica MR !42 no título
  ↓
Comentário no MR: "🎫 Ticket #1234 atualizado: Em andamento"
```

## Estrutura da Resolução

```
resolucao/
├── ecosystem-bot-gitlab-glpi.py    # Bot principal
├── mr-mock.json                     # Mock de MR para testes
├── ticket-mock.json                 # Mock de ticket para testes
├── .env.example                     # Template de configuração
├── .env                             # Configuração local (não commitar)
├── requirements.txt                 # Dependências Python
└── README.md                        # Este arquivo
```

## Como Usar

### 1. Configurar Ambiente

```bash
cd modulo-09-automacao-de-ecossistema/resolucao

# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 2. Configurar Tokens

Edite o arquivo `.env` com seus tokens:

```env
GITLAB_TOKEN=glpat-your-gitlab-token-here
GLPI_USER_TOKEN=your-glpi-user-token-here
GLPI_APP_TOKEN=your-glpi-app-token-here
GITLAB_URL=https://git.ifsc.edu.br
GLPI_URL=https://glpi.ifsc.edu.br/apirest.php
GITLAB_PROJECT_ID=123
```

**Onde obter os tokens:**

- **GitLab Token**: Settings → Access Tokens → Criar token com `api` scope
- **GLPI User Token**: Setup → General → API → Criar token de usuário
- **GLPI App Token**: Mesmo local, criar token de aplicação

### 3. Testar Localmente (Modo Mock)

```bash
python ecosystem-bot-gitlab-glpi.py --local
```

Este modo demonstra os fluxos sem chamar APIs reais, usando os arquivos de mock.

### 3.1 Testar NL Parser (Linguagem Natural)

O bot agora inclui um **parser de linguagem natural** que converte mensagens em tickets estruturados, similar ao bot do professor.

#### Testar via CLI

```bash
# Configura chave da API no .env primeiro
# OPENAI_API_KEY=sk-...

# Testa uma mensagem simples
python ecosystem-bot-gitlab-glpi.py --parse "Preciso investigar bug no login OAuth"

# Testa uma mensagem complexa
python ecosystem-bot-gitlab-glpi.py --parse "Carlos pediu para antecipar o módulo de relatórios para antes do fim do mês. Alguém pode pegar isso?"
```

**Saída esperada (exemplo):**

```
============================================================
MODO PARSE NL - TESTE DE LINGUAGEM NATURAL
============================================================

Mensagem original: Preciso investigar bug no login OAuth

Processando com IA...

------------------------------------------------------------
JSON PARSEADO:
------------------------------------------------------------
{
  "type": "bug",
  "title": "Investigar bug no login OAuth",
  "priority": "2",
  "assignee": null,
  "dueDate": null,
  "category": "Desenvolvimento",
  "requestedBy": null,
  "reason": "Problema de autenticação afetando usuários",
  "description": "Investigar falha no fluxo de login OAuth. Verificar logs de autenticação, tokens expirados e integração com provedor OAuth.",
  "tags": ["bug", "oauth", "login", "autenticação"],
  "actionRequired": "Atribuir assignee antes de criar ticket",
  "confidence": "high",
  "rawMessage": "Preciso investigar bug no login OAuth"
}

------------------------------------------------------------
INTERPRETAÇÃO:
------------------------------------------------------------
Tipo: bug
Título: Investigar bug no login OAuth
Prioridade: 2
Assignee: N/A
Confiança: high

⚠️  Ação necessária: Atribuir assignee antes de criar ticket

✅ Pronto para criar ticket no GLPI

============================================================
```

#### Testar via Webhook

Inicie o servidor webhook:

```bash
python ecosystem-bot-gitlab-glpi.py
```

Em outro terminal, teste o endpoint `/webhook/chat`:

```bash
# Mensagem simples
curl -X POST http://localhost:5000/webhook/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Preciso investigar bug no login OAuth"}'

# Mensagem complexa com assignee implícito
curl -X POST http://localhost:5000/webhook/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Carlos pediu para antecipar o módulo de relatórios para antes do fim do mês. Alguém pode pegar isso?"}'

# Pergunta (não cria ticket automaticamente)
curl -X POST http://localhost:5000/webhook/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Alguém já olhou o bug do GPS?"}'
```

**Resposta esperada (sucesso):**

```json
{
  "status": "ok",
  "ticket_id": 5678,
  "parsed": {
    "type": "bug",
    "title": "Investigar bug no login OAuth",
    "priority": "2",
    "assignee": null,
    "confidence": "high"
  },
  "message": "Ticket #5678 criado com sucesso"
}
```

**Resposta esperada (pergunta):**

```json
{
  "status": "question",
  "parsed": {
    "type": "question",
    "actionRequired": false,
    "suggestedAction": "Criar ticket de investigação? Aguardando confirmação."
  },
  "message": "Esta é uma pergunta. Confirme se deseja criar ticket de investigação."
}
```

#### Exemplos de Mensagens para Testar

**Bug simples:**
```
"Preciso investigar por que os alertas de velocidade não estão chegando para os motoristas na região de Uberlândia."
```

**Feature com prazo:**
```
"O Carlos pediu ontem que a gente antecipe o módulo de manutenção preditiva para antes do fim do mês porque a frota vai fazer revisão anual em junho. Alguém pode pegar isso?"
```

**Decisão crítica:**
```
"Atenção time: o deploy de sexta está bloqueado porque o módulo de Score de Comportamento ainda depende do hardware que não chegou. Precisamos decidir até amanhã se postergamos o deploy ou removemos o Score do escopo da release."
```

**Pergunta (não cria ticket):**
```
"Alguém já olhou o bug do GPS?"
```

**Mensagem insuficiente:**
```
"Problema no sistema"
```

#### Exemplos de Teste com Mocks

**Cenário 1: MR criado → cria ticket no GLPI**

O arquivo `mr-mock.json` contém um MR simulado:

```json
{
  "iid": 42,
  "title": "Implementar validação de CPF em formulário de cadastro",
  "state": "opened",
  "author": {
    "name": "João Silva",
    "username": "joao.silva"
  },
  "source_branch": "feature/validacao-cpf",
  "target_branch": "main",
  "web_url": "https://git.ifsc.edu.br/projeto/exemplo/-/merge_requests/42",
  "description": "Adiciona validação de CPF no formulário de cadastro de usuários..."
}
```

**Executar teste:**

```bash
python ecosystem-bot-gitlab-glpi.py --local
```

**Saída esperada:**

```
============================================================
MODO LOCAL - DEMONSTRAÇÃO COM MOCKS
============================================================

CENÁRIO 1: MR criado → cria ticket no GLPI
------------------------------------------------------------
MR !42: Implementar validação de CPF em formulário de cadastro
Status: opened
Autor: João Silva

Ações que seriam executadas:
  1. Buscar MR no GitLab
  2. Verificar se já existe ticket vinculado
  3. Criar ticket no GLPI com título: [MR !42] Implementar validação de CPF...
  4. Adicionar comentário no MR com link do ticket

CENÁRIO 2: Status do ticket muda → notifica no MR
------------------------------------------------------------
Ticket #1234: [MR !42] Implementar validação de CPF em formulário de cadastro
Novo status: 2

Ações que seriam executadas:
  1. Buscar ticket no GLPI
  2. Extrair MR IID do título: !42
  3. Adicionar comentário no MR com atualização do ticket

============================================================
Para testar em produção, configure o .env e execute:
  python ecosystem-bot-gitlab-glpi.py
============================================================
```

**Cenário 2: Ticket atualizado → notifica no MR**

O arquivo `ticket-mock.json` contém um ticket simulado:

```json
{
  "id": 1234,
  "name": "[MR !42] Implementar validação de CPF em formulário de cadastro",
  "status": 2,
  "content": "Ticket criado automaticamente para rastrear o Merge Request.",
  "date_creation": "2026-03-15T10:30:00-03:00"
}
```

O bot extrai o MR IID (`!42`) do título do ticket e adiciona comentário no MR correspondente.

#### Criando Mocks Personalizados

Você pode criar seus próprios mocks para testar cenários específicos:

**mr-mock-personalizado.json:**

```json
{
  "iid": 99,
  "title": "Corrigir bug de autenticação OAuth",
  "state": "merged",
  "author": {
    "name": "Maria Santos",
    "username": "maria.santos"
  },
  "source_branch": "fix/oauth-bug",
  "target_branch": "main",
  "web_url": "https://git.ifsc.edu.br/projeto/exemplo/-/merge_requests/99",
  "description": "Corrige problema de timeout na autenticação OAuth com Google."
}
```

**ticket-mock-personalizado.json:**

```json
{
  "id": 5678,
  "name": "[MR !99] Corrigir bug de autenticação OAuth",
  "status": 6,
  "content": "Ticket resolvido - bug corrigido e testado.",
  "date_creation": "2026-03-20T14:15:00-03:00"
}
```

**Testar com mock personalizado:**

```bash
# Copie os mocks personalizados para os arquivos esperados
cp mr-mock-personalizado.json mr-mock.json
cp ticket-mock-personalizado.json ticket-mock.json

# Execute o teste
python ecosystem-bot-gitlab-glpi.py --local
```

#### Simulando Webhooks em Produção

Para testar os endpoints webhook localmente sem expor o servidor:

**1. Inicie o servidor webhook:**

```bash
python ecosystem-bot-gitlab-glpi.py
```

**2. Teste o endpoint do GitLab (em outro terminal):**

```bash
# Simula webhook de MR criado
curl -X POST http://localhost:5000/webhook/gitlab \
  -H "Content-Type: application/json" \
  -d '{
    "object_kind": "merge_request",
    "object_attributes": {
      "iid": 42,
      "title": "Teste de webhook",
      "state": "opened"
    }
  }'
```

**3. Teste o endpoint do GLPI:**

```bash
# Simula webhook de ticket atualizado
curl -X POST http://localhost:5000/webhook/glpi \
  -H "Content-Type: application/json" \
  -d '{
    "id": 1234,
    "status": 2,
    "comment": "Ticket em andamento"
  }'
```

**4. Verifique health check:**

```bash
curl http://localhost:5000/health
```

Saída esperada: `{"status": "ok", "service": "ecosystem-bot"}`

### 4. Executar em Produção (Modo Webhook)

```bash
python ecosystem-bot-gitlab-glpi.py
```

O bot inicia um servidor Flask na porta 5000 com os seguintes endpoints:

- `POST /webhook/gitlab` - Recebe eventos de MR do GitLab
- `POST /webhook/glpi` - Recebe atualizações de ticket do GLPI
- `GET /health` - Health check

### 5. Configurar Webhooks

#### GitLab Webhook

1. Vá em Settings → Webhooks do seu projeto GitLab
2. URL: `http://seu-servidor:5000/webhook/gitlab`
3. Trigger: `Merge request events`
4. Salve e teste

#### GLPI Webhook

1. Vá em Setup → Notifications → Webhooks
2. URL: `http://seu-servidor:5000/webhook/glpi`
3. Eventos: `Ticket update`
4. Salve e teste

## Limitações Atuais

### O que o bot faz:
- ✅ Sincronização bidirecional MR ↔ ticket
- ✅ Criação automática de tickets a partir de MRs
- ✅ Notificação de mudanças de status no MR
- ✅ Rastreamento via título formatado `[MR !42]`
- ✅ **NL Parser** - Converte mensagens em linguagem natural em tickets estruturados
- ✅ **Webhook /webhook/chat** - Recebe mensagens e cria tickets automaticamente

### O que o bot NÃO faz:
- ❌ **Query contextual** - Não responde perguntas como "qual o status da US-123?"
- ❌ **Interface de chat** - Não tem integração com Slack/Teams (apenas webhook HTTP)
- ❌ **Inteligência contextual** - Não busca dados históricos ou relacionados
- ❌ **Confirmação interativa** - Não espera confirmação do usuário antes de criar ticket (cria automaticamente se confiança for alta/média)

## Comparação com o Exemplo do Professor

| Característica | Professor (Slack ↔ Jira) | Nossa Resolução (GitLab ↔ GLPI) |
|---|---|---|
| **Ferramentas** | Slack + Jira | GitLab + GLPI |
| **Linguagem** | Node.js | Python |
| **NL Parsing** | ✅ Sim (Claude/Gemini) | ✅ Sim (OpenAI/Anthropic) |
| **Bidirecional** | ✅ Sim | ✅ Sim |
| **Query Contextual** | ❌ Não | ❌ Não |
| **Webhook Server** | ❌ Não (Make.com) | ✅ Sim (Flask) |
| **Parser CLI** | ❌ Não | ✅ Sim (--parse) |
| **Confirmação** | ✅ Sim (no Slack) | ❌ Não (automático) |

## Arquitetura do NL Parser

O parser de linguagem natural segue a mesma arquitetura do bot do professor:

```
1. Listener (Webhook / CLI)
   ↓
   Usuário: "Preciso investigar bug no login OAuth"
   
2. Parser (OpenAI/Anthropic com NL_PARSER_PROMPT)
   ↓
   JSON: {
     "type": "bug",
     "title": "Investigar bug no login OAuth",
     "priority": "2",
     "assignee": null,
     "description": "Investigar falha no fluxo...",
     "confidence": "high"
   }
   
3. Executor (GLPI API)
   ↓
   Ticket #5678 criado
   
4. Notificação (Response)
   ↓
   {"status": "ok", "ticket_id": 5678}
```

### Prompt NL_PARSER_PROMPT

O prompt é adaptado do `nl-to-workflow-prompt.md` do professor e inclui:

- **Campos de output**: type, title, priority, assignee, dueDate, category, etc
- **Regras de extração**: classificação de tipo, inferência de prioridade, regras para assignee
- **Casos especiais**: múltiplas ações, perguntas, mensagens insuficientes
- **Restrições**: nunca inventar assignees/datas, retornar apenas JSON

### Diferenças do Prompt do Professor

| Aspecto | Professor (Jira) | Nosso (GLPI) |
|---|---|---|
| **Prioridades** | Highest, High, Medium, Low | 1-6 (valores numéricos do GLPI) |
| **Tipos** | bug, task, feature, question, decision | Mesmo |
| **Contexto** | RouteWise (frota) | Genérico (adaptável) |
| **Modelo** | Claude (claude-sonnet-4-6) | OpenAI (gpt-4o-mini) ou Anthropic |

## Próximos Passos (Opcional)

### 1. Adicionar Interface de Chat

Atualmente o bot aceita mensagens apenas via webhook HTTP. Para integrar com Slack/Teams:

```python
# Exemplo: Slack Bot com @slack/bolt
from slack_bolt import App

app = App(token=os.environ["SLACK_BOT_TOKEN"])

@app.message("ticket:")
def handle_ticket_request(message, say):
    user_message = message["text"].replace("ticket:", "").strip()
    
    # Chama o parser
    parsed = parse_natural_language(user_message)
    
    # Confirmação antes de criar
    say(f"📋 Card identificado:\n{parsed['title']}\nConfirma criação? (sim/não)")
    
    # Aguarda confirmação...
```

### 2. Adicionar Query Contextual

Para responder perguntas sobre o estado do projeto, seria necessário:

1. **LLM com tools** (LangChain agents) que:
   - Interpreta pergunta em linguagem natural
   - Decide qual API chamar (GitLab ou GLPI)
   - Busca dados relevantes
   - Gera resposta contextual

**Exemplo de uso com query contextual:**
```
Usuário: "Quais MRs estão relacionados ao ticket #1234?"
Bot: "Encontrei 2 MRs vinculados ao ticket #1234:
      - MR !42: Implementar validação de CPF (aberto)
      - MR !38: Corrigir bug de login (merged)"
```

**Exemplo mais avançado:**
```
Usuário: "Qual o status da US-123 e quais tickets estão relacionados?"
Bot: "US-123 'Implementar autenticação' está em revisão (MR !45).
      Tickets relacionados:
      - #1230: Configurar OAuth (resolvido)
      - #1231: Implementar login (em andamento)
      - #1232: Testes de segurança (novo)"
```

### 3. Adicionar Confirmação Interativa

Atualmente o bot cria tickets automaticamente se a confiança for alta/média. Para adicionar confirmação:

```python
# No endpoint /webhook/chat
if parsed.get("confidence") in ["high", "medium"]:
    # Envia para canal de confirmação (Slack/Teams)
    send_confirmation_request(parsed, original_message)
    
    # Aguarda resposta do usuário
    # Se confirmado, cria ticket
    # Se negado, descarta
```

## Recursos Adicionais

- [GitLab API Documentation](https://docs.gitlab.com/ee/api/)
- [GLPI API Documentation](https://github.com/glpi-project/glpi/blob/master/apirest.md)
- [Flask Documentation](https://flask.palletsprojects.com/)

---

**Adaptado do template do professor Ahirton Lopes para o contexto IFSC**
