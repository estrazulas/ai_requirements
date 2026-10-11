"""
danger-gitlab-ifsc.py -- Governanca como Codigo para GitLab

Adaptado do danger-config-routewise.py para GitLab (git.ifsc.edu.br)
Substitui Jira por referencias a issues do GitLab (#numero)

===========================================================================
ARQUIVO DE CONFIGURACAO
===========================================================================

As regras de governanca estao no arquivo governance-config.json.
Edite esse arquivo para ajustar as regras sem alterar o script.

Parametros configuraveis:
    - gitlab_url: URL do seu GitLab
    - critical_paths: pastas que exigem revisao adicional
    - critical_approvers: quantos revisores sao necessarios
    - large_mr_threshold: limite de linhas antes do aviso
    - coverage_drop_threshold: queda de cobertura tolerada
    - issue_pattern: regex para validar referencia a issues
    - min_description_length: tamanho minimo da descricao

===========================================================================
COMO USAR: DOIS CENARIOS DE DEMO
===========================================================================

CENARIO 1 -- Rodando localmente (sem GitLab, sem internet, sem token)
----------------------------------------------------------------------
Este modo simula a execucao das regras contra um MR ficticio definido
em arquivo JSON. Ideal para testes offline.

Passos:

    1. Abra um terminal na pasta onde estao estes arquivos.

    2. Cenario que PASSA em todas as regras:

           python danger-gitlab-ifsc.py --local --mock mr-mock-sucesso.json

    3. Cenario que FALHA -- simula MR mal configurado:

           python danger-gitlab-ifsc.py --local --mock mr-mock-falha.json

CENARIO 2 -- Rodando no GitLab com MRs reais (via CI/CD)
----------------------------------------------------------------------
O script roda automaticamente no pipeline do GitLab CI/CD.

Passos:

    1. Copie este script e o governance-config.json para a raiz do seu repositorio.

    2. Crie ou edite .gitlab-ci.yml na raiz do projeto:

           governance-check:
             stage: test
             image: python:3.11-slim
             script:
               - pip install requests
               - python danger-gitlab-ifsc.py
             rules:
               - if: $CI_MERGE_REQUEST_IID
             allow_failure: false

    3. Edite o arquivo governance-config.json para o seu projeto:
       - critical_paths: pastas que exigem revisao adicional
       - critical_approvers: quantos revisores sao necessarios
       - large_mr_threshold: limite de linhas antes do aviso
       - coverage_drop_threshold: queda de cobertura tolerada

    4. Para cobertura de testes funcionar, gere o arquivo
       coverage/coverage-summary.json antes deste step no pipeline.

===========================================================================
FORMATO DO ARQUIVO DE MOCK
===========================================================================

    {
      "mr": {
        "title": "fix: corrige bug de conexao #42",
        "description": "Texto detalhado explicando o que muda e por que.",
        "changes_count": 359
      },
      "changed_files": [
        "src/integrations/gps/tracker-client.js",
        "src/api/routes/alerts.js"
      ],
      "approvals": [
        { "username": "priya-ti" },
        { "username": "carlos-ops" }
      ],
      "coverage": {
        "total": { "lines": { "pct": 81.4 } }
      },
      "base_coverage": {
        "total": { "lines": { "pct": 83.1 } }
      }
    }

===========================================================================
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# CARREGA CONFIGURACAO DO ARQUIVO governance-config.json
# ---------------------------------------------------------------------------

CONFIG_PATH = Path(__file__).parent / "governance-config.json"

if CONFIG_PATH.exists():
    CONFIG = json.loads(CONFIG_PATH.read_text())
else:
    print(f"Aviso: arquivo de configuracao nao encontrado: {CONFIG_PATH}")
    print("Usando configuracao padrao. Crie governance-config.json para personalizar.")
    CONFIG = {
        "gitlab_url": "https://git.ifsc.edu.br",
        "critical_paths": [],
        "critical_approvers": 2,
        "large_mr_threshold": 500,
        "coverage_drop_threshold": 5,
        "issue_pattern": r"#\d+",
        "min_description_length": 30,
    }

# ---------------------------------------------------------------------------
# ARGPARSE -- modo local vs modo CI
# ---------------------------------------------------------------------------

parser = argparse.ArgumentParser(description="Governance check para MRs do GitLab.")
parser.add_argument(
    "--local",
    action="store_true",
    help="Modo local: le dados do MR de um arquivo JSON (sem GitLab API).",
)
parser.add_argument(
    "--mock",
    default="mr-mock-sucesso.json",
    help="Caminho para o arquivo de mock (default: mr-mock-sucesso.json).",
)
args = parser.parse_args()

# ---------------------------------------------------------------------------
# COLETA DE DADOS DO MR
# ---------------------------------------------------------------------------

if args.local:
    mock_path = Path(args.mock)
    if not mock_path.exists():
        print(f"Arquivo de mock nao encontrado: {mock_path}")
        print("Execute no mesmo diretorio dos materiais ou passe --mock <caminho>.")
        sys.exit(1)

    data = json.loads(mock_path.read_text())
    mr_title = data["mr"]["title"]
    mr_description = data["mr"].get("description", "") or ""
    changes_count = data["mr"].get("changes_count", 0)
    changed_files = data.get("changed_files", [])
    approvals = len(data.get("approvals", []))
    coverage_data = data.get("coverage")
    base_coverage_data = data.get("base_coverage")

    print(f"[MODO LOCAL] Lendo MR: {mr_title}")
    print(f"Arquivos alterados: {len(changed_files)} | Aprovadores: {approvals} | Linhas: {changes_count}")
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
        print("Para rodar localmente use: python danger-gitlab-ifsc.py --local")
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
    changed_files = [c["new_path"] for c in mr_approvals.get("changes", [])]
    approvals = len([a for a in mr_approvals.get("approved_by", [])])
    coverage_data = None
    base_coverage_data = None

    coverage_path = Path("coverage/coverage-summary.json")
    base_path = Path("coverage/base-coverage.json")
    if coverage_path.exists():
        coverage_data = json.loads(coverage_path.read_text())
    if base_path.exists():
        base_coverage_data = json.loads(base_path.read_text())

# ---------------------------------------------------------------------------
# ACUMULA RESULTADOS
# ---------------------------------------------------------------------------

failures = []
warnings = []
messages = []

# ---------------------------------------------------------------------------
# REGRA 1 -- O MR deve referenciar uma issue do GitLab
# ---------------------------------------------------------------------------

issue_pattern = re.compile(CONFIG.get("issue_pattern", r"#\d+"))

if not issue_pattern.search(mr_title) and not issue_pattern.search(mr_description):
    failures.append(
        f"Referencia a issue nao encontrada. O titulo ou a descricao deve conter "
        f"o numero da issue (ex: #42). "
        f"Isso garante rastreabilidade entre o MR e o trabalho planejado."
    )

# ---------------------------------------------------------------------------
# REGRA 2 -- Arquivos criticos exigem pelo menos N aprovadores
# ---------------------------------------------------------------------------

critical_files = [
    f for f in changed_files
    if any(cp in f for cp in CONFIG["critical_paths"])
]

if critical_files:
    if approvals < CONFIG["critical_approvers"]:
        failures.append(
            f"Arquivo critico modificado com aprovadores insuficientes. "
            f"Este MR toca modulos de integracao ou arquivos sensiveis. "
            f"Necessario pelo menos {CONFIG['critical_approvers']} aprovadores "
            f"(atual: {approvals}). "
            f"Arquivos criticos: {', '.join(critical_files)}"
        )
    else:
        messages.append(
            f"Arquivo critico com {approvals} aprovadores -- "
            f"requisito de revisao atendido. ({', '.join(critical_files)})"
        )

# ---------------------------------------------------------------------------
# REGRA 3 -- MRs grandes recebem aviso
# ---------------------------------------------------------------------------

if changes_count > CONFIG["large_mr_threshold"]:
    warnings.append(
        f"MR grande detectado ({changes_count} linhas alteradas). "
        f"MRs acima de {CONFIG['large_mr_threshold']} linhas aumentam o risco de bugs. "
        f"Considere dividir em MRs menores ou agendar revisao dedicada."
    )

# ---------------------------------------------------------------------------
# REGRA 4 -- Cobertura de testes
# ---------------------------------------------------------------------------

if coverage_data:
    try:
        current_pct = coverage_data["total"]["lines"]["pct"]
        if base_coverage_data:
            base_pct = base_coverage_data["total"]["lines"]["pct"]
            drop = base_pct - current_pct
            if drop > CONFIG["coverage_drop_threshold"]:
                warnings.append(
                    f"Cobertura de testes caiu {drop:.1f} pontos "
                    f"(de {base_pct:.1f}% para {current_pct:.1f}%). "
                    f"Queda acima de {CONFIG['coverage_drop_threshold']}% indica "
                    f"codigo novo sem cobertura. Adicione testes ou justifique na descricao."
                )
            else:
                messages.append(
                    f"Cobertura de testes: {current_pct:.1f}% "
                    f"(queda de {drop:.1f}p em relacao a base {base_pct:.1f}%) -- "
                    f"dentro do limite aceitavel."
                )
        else:
            messages.append(
                f"Cobertura atual: {current_pct:.1f}%. "
                f"Cobertura base nao disponivel -- comparacao nao realizada."
            )
    except KeyError:
        warnings.append(
            "Formato do arquivo de cobertura invalido. "
            "Esperado: {'total': {'lines': {'pct': valor}}}."
        )
else:
    messages.append(
        "Dados de cobertura nao encontrados. "
        "Para ativar esta regra, gere coverage-summary.json no pipeline antes deste step."
    )

# ---------------------------------------------------------------------------
# REGRA 5 -- MRs sem descricao recebem aviso
# ---------------------------------------------------------------------------

min_desc_length = CONFIG.get("min_description_length", 30)

if len(mr_description.strip()) < min_desc_length:
    warnings.append(
        f"Descricao do MR muito curta ou ausente (minimo: {min_desc_length} caracteres). "
        f"Uma boa descricao explica o que muda e por que -- nao apenas lista arquivos. "
        f"Isso facilita revisao, rollback e historico do projeto."
    )

# ---------------------------------------------------------------------------
# EXIBE RESULTADO NO TERMINAL
# ---------------------------------------------------------------------------

SEP = "-" * 60

print(SEP)
print("GOVERNANCE CHECK -- RESULTADO")
print(SEP)

if failures:
    print(f"\nFALHAS ({len(failures)}) -- bloqueiam o merge:\n")
    for i, f in enumerate(failures, 1):
        print(f"  {i}. {f}")

if warnings:
    print(f"\nAVISOS ({len(warnings)}) -- nao bloqueiam:\n")
    for i, w in enumerate(warnings, 1):
        print(f"  {i}. {w}")

if messages:
    print(f"\nINFORMACAO ({len(messages)}):\n")
    for i, m in enumerate(messages, 1):
        print(f"  {i}. {m}")

print()
print(SEP)
status = "FALHOU" if failures else "OK"
print(f"Status final: {status}")
print(f"Regras verificadas: referencia a issue, aprovadores para arquivos criticos,")
print(f"tamanho do MR, cobertura de testes e qualidade da descricao.")
print(SEP)

# ---------------------------------------------------------------------------
# POSTA COMENTARIO NO MR (apenas modo CI)
# ---------------------------------------------------------------------------

if not args.local:
    lines = ["**Governance Check (GitLab) -- Resultado**", ""]
    if failures:
        lines.append(f"**FALHAS ({len(failures)}) -- bloqueiam o merge:**")
        for f in failures:
            lines.append(f"- FALHA: {f}")
        lines.append("")
    if warnings:
        lines.append(f"**AVISOS ({len(warnings)}) -- nao bloqueiam:**")
        for w in warnings:
            lines.append(f"- AVISO: {w}")
        lines.append("")
    if messages:
        lines.append("**Informacoes:**")
        for m in messages:
            lines.append(f"- {m}")
        lines.append("")
    lines.append(f"Status final: **{status}**")
    post_note("\n".join(lines))

# ---------------------------------------------------------------------------
# CODIGO DE SAIDA: 1 se houver falhas (trava o merge via GitLab CI)
# ---------------------------------------------------------------------------

if failures:
    sys.exit(1)
