"""
compliance-checker.py -- Checklist de Compliance com IA para GitLab

Gera checklist de conformidade automatizado usando IA (OpenAI/Anthropic)
integrado com Merge Requests do GitLab.

===========================================================================
COMO USAR
===========================================================================

CENARIO 1 -- Modo local (testes offline com mock)
----------------------------------------------------------------------

    python compliance-checker.py --local --mock mr-mock-sucesso.json

CENARIO 2 -- Modo CI/CD (GitLab)
----------------------------------------------------------------------

    python compliance-checker.py

Variaveis de ambiente obrigatorias no CI:
    - OPENAI_API_KEY ou ANTHROPIC_API_KEY
    - CI_JOB_TOKEN (automatico do GitLab)
    - CI_PROJECT_ID (automatico)
    - CI_MERGE_REQUEST_IID (automatico)

CENARIO 3 -- Agente LangChain (avancado)
----------------------------------------------------------------------

    python compliance-checker.py --agent

Requer: pip install langchain openai

===========================================================================
"""

import argparse
import json
import os
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# CONFIGURACAO
# ---------------------------------------------------------------------------

CONFIG = {
    "gitlab_url": "https://git.ifsc.edu.br",
    "ai_provider": os.environ.get("AI_PROVIDER", "openai"),  # openai ou anthropic
    "model": os.environ.get("AI_MODEL", "gpt-4o-mini"),  # ou claude-3-5-sonnet-20241022
}

# ---------------------------------------------------------------------------
# TEMPLATE DE PROMPT (do compliance-checklist-prompt.md)
# ---------------------------------------------------------------------------

PROMPT_TEMPLATE = """Voce e um especialista em governanca de projetos de software e compliance de pipeline de desenvolvimento. Sua funcao e gerar checklists de conformidade especificos para o contexto fornecido - priorizando clareza, acionabilidade e rastreabilidade.

---

## TIPO DE EVENTO

Deploy em producao via Merge Request

---

## CONTEXTO DO PROJETO

- Titulo do MR: {title}
- Descricao: {description}
- Arquivos alterados: {changed_files}
- Numero de aprovadores: {approvals}
- Linhas alteradas: {changes_count}

---

## ANALISE SOLICITADA

Gere um checklist estruturado em tres categorias:

### BLOQUEADORES
Itens que impedem o merge de acontecer se nao estiverem OK.
- Maximo de 5 itens
- Cada item deve ter: **[categoria]** + descricao da verificacao + criterio de "passou"
- Categorias sugeridas: [Tecnico] [Legal] [Seguranca] [Operacional] [Aprovacao]

### VERIFICACOES OPERACIONAIS
Itens que devem ser verificados mas nao bloqueiam - geram risco se ignorados.
- Maximo de 5 itens
- Mesmo formato: categoria + descricao + criterio de verificacao

### INFORMATIVOS
Itens de rastreabilidade e documentacao que devem ser registrados.
- Maximo de 4 itens
- Nao sao checagens - sao registros obrigatorios para auditoria

---

## RESTRICOES DE COMPORTAMENTO

- O checklist deve ser especifico para o contexto - nao generico
- Cada item BLOQUEADOR deve ter um criterio de "passou" objetivo e verificavel
- Limite total: no maximo 14 itens (5 + 5 + 4)
- Responda em portugues
"""

# ---------------------------------------------------------------------------
# ARGPARSE
# ---------------------------------------------------------------------------

parser = argparse.ArgumentParser(description="Compliance checker com IA para GitLab MRs.")
parser.add_argument(
    "--local",
    action="store_true",
    help="Modo local: le dados do MR de um arquivo JSON.",
)
parser.add_argument(
    "--mock",
    default="mr-mock-sucesso.json",
    help="Caminho para o arquivo de mock.",
)
parser.add_argument(
    "--agent",
    action="store_true",
    help="Usar agente LangChain (requer langchain instalado).",
)
args = parser.parse_args()

# ---------------------------------------------------------------------------
# COLETA DE DADOS DO MR
# ---------------------------------------------------------------------------

if args.local:
    mock_path = Path(args.mock)
    if not mock_path.exists():
        print(f"Arquivo de mock nao encontrado: {mock_path}")
        sys.exit(1)

    data = json.loads(mock_path.read_text())
    mr_title = data["mr"]["title"]
    mr_description = data["mr"].get("description", "") or ""
    changes_count = data["mr"].get("changes_count", 0)
    changed_files = data.get("changed_files", [])
    approvals = len(data.get("approvals", []))

    print(f"[MODO LOCAL] Lendo MR: {mr_title}")
    print()

else:
    try:
        import requests
    except ImportError:
        print("Dependencia ausente: pip install requests")
        sys.exit(1)

    TOKEN = os.environ.get("CI_JOB_TOKEN") or os.environ.get("GITLAB_TOKEN", "")
    PROJECT_ID = os.environ.get("CI_PROJECT_ID", "")
    MR_IID = os.environ.get("CI_MERGE_REQUEST_IID", "")
    GITLAB_URL = os.environ.get("CI_API_V4_URL", f"{CONFIG['gitlab_url']}/api/v4")

    if not TOKEN or not PROJECT_ID or not MR_IID:
        print("Erro: variaveis CI_JOB_TOKEN, CI_PROJECT_ID e CI_MERGE_REQUEST_IID sao obrigatorias.")
        print("Para rodar localmente use: python compliance-checker.py --local")
        sys.exit(1)

    HEADERS = {"PRIVATE-TOKEN": TOKEN}
    BASE_URL = f"{GITLAB_URL}/projects/{PROJECT_ID}"

    def get(endpoint):
        r = requests.get(f"{BASE_URL}{endpoint}", headers=HEADERS)
        r.raise_for_status()
        return r.json()

    def post_note(body):
        requests.post(
            f"{BASE_URL}/merge_requests/{MR_IID}/notes",
            headers=HEADERS,
            json={"body": body},
        )

    mr = get(f"/merge_requests/{MR_IID}")
    mr_files = get(f"/merge_requests/{MR_IID}/changes")
    mr_approvals = get(f"/merge_requests/{MR_IID}/approvals")

    mr_title = mr.get("title", "")
    mr_description = mr.get("description", "") or ""
    changes_count = mr.get("changes_count", 0)
    changed_files = [c["new_path"] for c in mr_files.get("changes", [])]
    approvals = len([a for a in mr_approvals.get("approved_by", [])])

# ---------------------------------------------------------------------------
# MONTA PROMPT
# ---------------------------------------------------------------------------

prompt = PROMPT_TEMPLATE.format(
    title=mr_title,
    description=mr_description,
    changed_files=", ".join(changed_files),
    approvals=approvals,
    changes_count=changes_count,
)

# ---------------------------------------------------------------------------
# CHAMA IA
# ---------------------------------------------------------------------------

def call_openai(prompt):
    try:
        import openai
    except ImportError:
        print("Dependencia ausente: pip install openai")
        sys.exit(1)

    api_key = os.environ.get("OPENAI_API_KEY", "")
    if not api_key:
        print("Erro: OPENAI_API_KEY nao configurada.")
        sys.exit(1)

    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=CONFIG["model"],
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return response.choices[0].message.content


def call_anthropic(prompt):
    try:
        import anthropic
    except ImportError:
        print("Dependencia ausente: pip install anthropic")
        sys.exit(1)

    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        print("Erro: ANTHROPIC_API_KEY nao configurada.")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model=CONFIG["model"],
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text


def call_langchain_agent(prompt, changed_files):
    try:
        from langchain.agents import initialize_agent, Tool
        from langchain.llms import OpenAI
    except ImportError:
        print("Dependencia ausente: pip install langchain openai")
        sys.exit(1)

    api_key = os.environ.get("OPENAI_API_KEY", "")
    if not api_key:
        print("Erro: OPENAI_API_KEY nao configurada.")
        sys.exit(1)

    # Tools do agente (exemplos - personalize para seu contexto)
    def search_internal_docs(query):
        """Busca em documentacao interna (ADRs, politicas)"""
        # Implemente RAG aqui com vectorstore
        return "Documentacao interna: LGPD aplicavel para dados de localizacao."

    def check_security_policy(file_path):
        """Verifica politica de seguranca para arquivo"""
        if "migrations/" in file_path or ".env" in file_path:
            return "ALERTA: Arquivo critico requer aprovacao de seguranca."
        return "OK"

    tools = [
        Tool(
            name="search_docs",
            func=search_internal_docs,
            description="Busca em documentacao interna do projeto",
        ),
        Tool(
            name="check_security",
            func=check_security_policy,
            description="Verifica politica de seguranca para arquivos",
        ),
    ]

    llm = OpenAI(api_key=api_key, temperature=0.3)
    agent = initialize_agent(tools, llm, verbose=True)

    # Adiciona contexto dos arquivos ao prompt
    enhanced_prompt = f"{prompt}\n\nArquivos para analise: {', '.join(changed_files)}"
    return agent.run(enhanced_prompt)


# ---------------------------------------------------------------------------
# EXECUTA
# ---------------------------------------------------------------------------

print("=" * 60)
print("COMPLIANCE CHECK -- GERANDO CHECKLIST COM IA")
print("=" * 60)
print()

if args.agent:
    print("[AGENTE LANGCHAIN] Usando agente com ferramentas...")
    checklist = call_langchain_agent(prompt, changed_files)
elif CONFIG["ai_provider"] == "anthropic":
    print(f"[ANTHROPIC] Usando modelo {CONFIG['model']}...")
    checklist = call_anthropic(prompt)
else:
    print(f"[OPENAI] Usando modelo {CONFIG['model']}...")
    checklist = call_openai(prompt)

print()
print(checklist)
print()
print("=" * 60)

# ---------------------------------------------------------------------------
# POSTA NO MR (apenas modo CI)
# ---------------------------------------------------------------------------

if not args.local:
    comment = f"**Compliance Checklist (IA) -- {CONFIG['model']}**\n\n{checklist}"
    post_note(comment)
    print("\n[OK] Checklist postado no Merge Request.")
