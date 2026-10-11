# Governança como Código para GitLab (git.ifsc.edu.br)

Script Python de governança automatizada para Merge Requests no GitLab, adaptado do Danger.js original.

## O que o script verifica

| Regra | Tipo | Critério |
|---|---|---|
| **Referência a issue** | Falha (bloqueia) | Título ou descrição deve conter `#NÚMERO` |
| **Aprovadores para arquivos críticos** | Falha (bloqueia) | Arquivos sensíveis exigem 2 aprovadores |
| **Tamanho do MR** | Aviso | Acima de 500 linhas gera recomendação |
| **Cobertura de testes** | Aviso | Queda acima de 5 pontos percentuais |
| **Descrição do MR** | Aviso | Menos de 30 caracteres gera aviso |

**Falhas bloqueiam o merge** (exit code 1). Avisos apenas alertam.

## Arquivos incluídos

- `danger-gitlab-ifsc.py` — Script principal de governança
- `governance-config.json` — Arquivo de configuração das regras (edite este!)
- `mr-mock-sucesso.json` — Exemplo de MR que passa em todas as regras
- `mr-mock-falha.json` — Exemplo de MR que falha em múltiplas regras
- `compliance-checker.py` — Checklist de compliance com IA (OpenAI/Anthropic)

## Personalizando as regras (sem alterar o script)

Edite o arquivo `governance-config.json` para ajustar as regras de governança ao seu projeto:

```json
{
  "gitlab_url": "https://git.ifsc.edu.br",
  
  "critical_paths": [
    "src/integrations/gps",
    "src/services/notifications",
    "src/api/routes",
    "migrations/",
    ".env",
    "docker-compose"
  ],
  
  "critical_approvers": 2,
  "large_mr_threshold": 500,
  "coverage_drop_threshold": 5,
  "issue_pattern": "#\\d+",
  "min_description_length": 30
}
```

### Parâmetros configuráveis

| Parâmetro | Descrição | Padrão |
|---|---|---|
| `gitlab_url` | URL do seu GitLab | `https://git.ifsc.edu.br` |
| `critical_paths` | Pastas que exigem revisores adicionais | Veja exemplo acima |
| `critical_approvers` | Número mínimo de aprovadores para arquivos críticos | `2` |
| `large_mr_threshold` | Limite de linhas antes de avisar sobre MR grande | `500` |
| `coverage_drop_threshold` | Queda de cobertura (%) que gera aviso | `5` |
| `issue_pattern` | Regex para validar referência a issues | `#\d+` |
| `min_description_length` | Tamanho mínimo da descrição do MR | `30` |

### Exemplos de personalização

**Usar padrão diferente para issues (ex: `ISSUE-123`):**

```json
{
  "issue_pattern": "ISSUE-\\d+"
}
```

**Aumentar limite de linhas para MRs grandes:**

```json
{
  "large_mr_threshold": 1000
}
```

**Adicionar mais caminhos críticos:**

```json
{
  "critical_paths": [
    "src/auth/",
    "src/payments/",
    "migrations/",
    ".env"
  ]
}
```

**Reduzir número de aprovadores para 1:**

```json
{
  "critical_approvers": 1
}
```

**Desativar verificação de caminhos críticos (lista vazia):**

```json
{
  "critical_paths": []
}
```

## Como usar localmente (testes offline)

### MR que passa em todas as regras

```bash
python danger-gitlab-ifsc.py --local --mock mr-mock-sucesso.json
```

**Saída esperada:**

```
[MODO LOCAL] Lendo MR: fix: corrige bug de conexao GPS #42
Arquivos alterados: 3 | Aprovadores: 2 | Linhas: 359

------------------------------------------------------------
GOVERNANCE CHECK -- RESULTADO
------------------------------------------------------------

INFORMACAO (3):

  1. Arquivo critico com 2 aprovadores -- requisito de revisao atendido.
  2. Cobertura de testes: 81.4% (queda de 1.7p em relacao a base 83.1%) -- dentro do limite aceitavel.
  3. Dados de cobertura encontrados e validados.

------------------------------------------------------------
Status final: OK
------------------------------------------------------------
```

### MR que falha em múltiplas regras

```bash
python danger-gitlab-ifsc.py --local --mock mr-mock-falha.json
```

**Saída esperada:**

```
[MODO LOCAL] Lendo MR: fix: corrige bug de conexao GPS
Arquivos alterados: 3 | Aprovadores: 1 | Linhas: 635

------------------------------------------------------------
GOVERNANCE CHECK -- RESULTADO
------------------------------------------------------------

FALHAS (2) -- bloqueiam o merge:

  1. Referencia a issue nao encontrada. O titulo ou a descricao deve conter
     o numero da issue (ex: #42).
  2. Arquivo critico modificado com aprovadores insuficientes.
     Necessario pelo menos 2 aprovadores (atual: 1).
     Arquivos criticos: src/integrations/gps/tracker-client.js, ...

AVISOS (2) -- nao bloqueiam:

  1. MR grande detectado (635 linhas alteradas). MRs acima de 500 linhas
     aumentam o risco de bugs. Considere dividir em MRs menores.
  2. Cobertura de testes caiu 11.1 pontos (de 83.1% para 72.0%).
     Queda acima de 5% indica codigo novo sem cobertura.

------------------------------------------------------------
Status final: FALHOU
------------------------------------------------------------
```

## Como usar no GitLab CI/CD

### 1. Copie o script para seu repositório

```bash
cp danger-gitlab-ifsc.py /caminho/do/seu/projeto/
```

### 2. Crie ou edite `.gitlab-ci.yml` na raiz do projeto

```yaml
stages:
  - test

governance-check:
  stage: test
  image: python:3.11-slim
  script:
    - pip install requests
    - python danger-gitlab-ifsc.py
  rules:
    - if: $CI_MERGE_REQUEST_IID
  allow_failure: false
```

### 3. Ajuste as regras para seu projeto

Edite o bloco `CONFIG` no início do script:

```python
CONFIG = {
    "gitlab_url": "https://git.ifsc.edu.br",
    
    "critical_paths": [
        "src/integrations/gps",      # ajuste para seus caminhos
        "src/services/notifications",
        "migrations/",
        ".env",
    ],
    
    "critical_approvers": 2,          # número de aprovadores necessários
    "large_mr_threshold": 500,        # limite de linhas
    "coverage_drop_threshold": 5,     # queda tolerada (%)
}
```

## Exemplos práticos de Merge Requests

### Exemplo 1: MR que PASSA (bom)

**Título:**
```
feat: adiciona validação de CPF #123
```

**Descrição:**
```markdown
Este MR implementa a validação de CPF no formulário de cadastro.

Mudanças:
- Adicionada função de validação de CPF
- Integrada com o formulário de cadastro
- Testes unitários cobrindo casos válidos e inválidos

Testes:
- npm test passando
- Cobertura mantida em 85%

Relacionado: #123
```

**Resultado:** ✅ PASSA (tem `#123`, descrição detalhada)

---

### Exemplo 2: MR que FALHA (ruim)

**Título:**
```
fix: arruma bug
```

**Descrição:**
```
arrumado
```

**Resultado:** ❌ FALHA
- Sem referência a issue (precisa de `#NÚMERO`)
- Descrição muito curta (< 30 caracteres)

---

### Exemplo 3: MR com arquivos críticos

**Título:**
```
refactor: melhora conexão com banco #456
```

**Arquivos alterados:**
```
migrations/001_add_users.sql
src/services/database.js
```

**Aprovadores:** 1 (junior-dev)

**Resultado:** ❌ FALHA
- Arquivos críticos (`migrations/`) exigem **2 aprovadores**
- Apenas 1 aprovador no momento

**Como resolver:** Peça para outro desenvolvedor sênior aprovar o MR.

---

### Exemplo 4: MR grande

**Título:**
```
feat: novo módulo de relatórios #789
```

**Linhas alteradas:** 650

**Resultado:** ⚠️ AVISO
- MR acima de 500 linhas
- Não bloqueia, mas recomenda dividir em MRs menores

---

### Exemplo 5: MR com queda de cobertura

**Título:**
```
fix: corrige cálculo de impostos #321
```

**Cobertura atual:** 72%  
**Cobertura base:** 83%  
**Queda:** 11 pontos

**Resultado:** ⚠️ AVISO
- Queda acima de 5 pontos percentuais
- Recomenda adicionar testes para o código novo

## Variáveis de ambiente do GitLab CI

O script usa automaticamente estas variáveis (disponíveis no CI):

| Variável | Descrição |
|---|---|
| `CI_JOB_TOKEN` | Token de autenticação (automático) |
| `CI_PROJECT_ID` | ID do projeto (automático) |
| `CI_MERGE_REQUEST_IID` | Número do MR (automático) |
| `CI_API_V4_URL` | URL da API GitLab (automático) |

## Personalizando as regras

### Mudar o padrão de referência a issues

Se seu projeto usa outro padrão (ex: `ISSUE-123`), edite a Regra 1:

```python
# Original (GitLab padrão)
gitlab_pattern = re.compile(r"#\d+")

# Personalizado
gitlab_pattern = re.compile(r"ISSUE-\d+")
```

### Adicionar mais caminhos críticos

```python
"critical_paths": [
    "src/integrations/gps",
    "src/services/notifications",
    "src/auth/",              # adicionado
    "src/payments/",          # adicionado
    "migrations/",
    ".env",
    "docker-compose",
],
```

### Desativar verificação de cobertura

Comente ou remova a Regra 4 no script.

## Integração com cobertura de testes

Para ativar a verificação de cobertura, gere o arquivo antes do governance check:

```yaml
# .gitlab-ci.yml
test:
  stage: test
  script:
    - npm test -- --coverage --coverageReporters=json-summary
    - pip install requests
    - python danger-gitlab-ifsc.py
  artifacts:
    paths:
      - coverage/
```

## Solução de problemas

### "Variáveis CI_JOB_TOKEN, CI_PROJECT_ID e CI_MERGE_REQUEST_IID são obrigatórias"

Você está rodando fora do GitLab CI. Use o modo local:

```bash
python danger-gitlab-ifsc.py --local --mock mr-mock-sucesso.json
```

### "Arquivo de mock não encontrado"

Verifique se está no diretório correto ou passe o caminho completo:

```bash
python danger-gitlab-ifsc.py --local --mock /caminho/completo/mr-mock-sucesso.json
```

### Script falha mas não deveria

Verifique se o MR tem referência a issue no título ou descrição (`#NÚMERO`).

## Recursos adicionais

- [Documentação oficial do GitLab CI/CD](https://docs.gitlab.com/ee/ci/)
- [GitLab API - Merge Requests](https://docs.gitlab.com/ee/api/merge_requests.html)
- [Merge Request Approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)

---

## Compliance Checker com IA

Além da governança automatizada (regras fixas), o projeto inclui um **compliance checker com IA** que gera checklists de conformidade contextuais para cada MR.

### Arquivo incluído

- `compliance-checker.py` — Script que chama uma IA (OpenAI/Anthropic) para gerar checklist de compliance

### Como funciona

O script:
1. Lê o contexto do MR (título, descrição, arquivos alterados, aprovadores)
2. Monta um prompt estruturado com o template do professor (`compliance-checklist-prompt.md`)
3. Chama a API da IA (OpenAI GPT-4o-mini por padrão)
4. Posta o checklist gerado como comentário no MR

### Como usar localmente

```bash
# 1. Copie o arquivo .env.example para .env
cp .env.example .env

# 2. Edite o .env e adicione sua chave da API
# OPENAI_API_KEY=sk-your-key-here

# 3. Instale as dependências
pip install openai requests python-dotenv

# 4. Roda com mock
python compliance-checker.py --local --mock mr-mock-sucesso.json
```

**Saída esperada:**

```
============================================================
COMPLIANCE CHECK -- GERANDO CHECKLIST COM IA
============================================================

[OPENAI] Usando modelo gpt-4o-mini...

### BLOQUEADORES
1. **[Técnico]** Referência a issue obrigatória — MR deve conter #NÚMERO no título ou descrição.
   - Critério: Regex `#\d+` encontra match no título ou descrição.

2. **[Aprovação]** Arquivos críticos exigem 2 aprovadores — MR toca `src/integrations/gps` e `src/api/routes`.
   - Critério: MR tem 2 approvals com status "approved".

### VERIFICAÇÕES OPERACIONAIS
1. **[Operacional]** MR com 359 linhas — abaixo do limite de 500, mas considere dividir se possível.
2. **[Técnico]** Cobertura caiu 1.7 pontos (83.1% → 81.4%) — dentro do limite de 5 pontos.

### INFORMATIVOS
1. **[Rastreabilidade]** Registrar hash do commit e autor do MR para auditoria.
2. **[Documentação]** Atualizar changelog com referência ao MR.

============================================================
```

### Como usar no GitLab CI/CD

```yaml
# .gitlab-ci.yml
stages:
  - test
  - compliance

# 1. Governança automatizada (regras fixas)
governance-check:
  stage: test
  image: python:3.11-slim
  script:
    - pip install requests
    - python danger-gitlab-ifsc.py
  rules:
    - if: $CI_MERGE_REQUEST_IID

# 2. Compliance com IA (checklist contextual)
compliance-review:
  stage: compliance
  image: python:3.11-slim
  script:
    - pip install openai requests python-dotenv
    - python compliance-checker.py
  rules:
    - if: $CI_MERGE_REQUEST_IID
  variables:
    OPENAI_API_KEY: $OPENAI_API_KEY  # configure em CI/CD > Variables
  allow_failure: true  # não bloqueia se a IA falhar
```

**Configuração no GitLab:**

1. Vá em **Settings > CI/CD > Variables**
2. Adicione `OPENAI_API_KEY` com sua chave da API
3. Marque como **Masked** e **Protected**

**Nota:** No CI/CD, o script lê a variável de ambiente diretamente (não precisa do arquivo `.env`).

### Usando Anthropic (Claude) em vez de OpenAI

Edite o arquivo `.env`:

```bash
ANTHROPIC_API_KEY=sk-ant-your-key-here
AI_PROVIDER=anthropic
AI_MODEL=claude-3-5-sonnet-20241022
```

Depois execute:

```bash
pip install anthropic requests python-dotenv
python compliance-checker.py --local --mock mr-mock-sucesso.json
```

No CI/CD:

```yaml
compliance-review:
  variables:
    AI_PROVIDER: "anthropic"
    AI_MODEL: "claude-3-5-sonnet-20241022"
    ANTHROPIC_API_KEY: $ANTHROPIC_API_KEY
```

---

## Agente LangChain Integrado com CI/CD

Para cenários mais complexos, use um **agente LangChain** que busca contexto em documentação interna, verifica políticas de segurança e toma decisões autônomas.

### Quando usar LangChain vs chamada direta

| Cenário | Recomendação |
|---|---|
| Regras fixas (título, aprovadores, tamanho) | Script Python puro (`danger-gitlab-ifsc.py`) |
| Checklist contextual simples | Chamada direta à API da IA (`compliance-checker.py`) |
| Precisa buscar em docs internos, ADRs, políticas | Agente LangChain |
| Precisa memória de decisões anteriores | Agente LangChain |
| Precisa consultar múltiplas fontes (Jira, GitLab, banco) | Agente LangChain |

### Exemplo de implementação com LangChain

```python
# agente_compliance.py
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

# 1. RAG: busca em documentação interna
def search_internal_docs(query):
    """Busca em ADRs, políticas de segurança, LGPD"""
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.load_local("./docs_index", embeddings)
    docs = vectorstore.similarity_search(query, k=3)
    return "\n".join([d.page_content for d in docs])

# 2. Consulta políticas de segurança
def check_security_policy(file_path):
    """Verifica se arquivo requer aprovação especial"""
    critical_patterns = ["migrations/", ".env", "src/auth/"]
    if any(p in file_path for p in critical_patterns):
        return "ALERTA: Arquivo crítico requer aprovação do time de segurança."
    return "OK"

# 3. Consulta GitLab API para contexto adicional
def get_mr_history(project_id):
    """Busca MRs anteriores para contexto"""
    # Implemente chamada à API do GitLab
    return "Último MR similar: #42 - aprovado após 2 dias de revisão"

# 4. Configura agente
tools = [
    Tool(
        name="search_docs",
        func=search_internal_docs,
        description="Busca em documentação interna (ADRs, políticas, LGPD)",
    ),
    Tool(
        name="check_security",
        func=check_security_policy,
        description="Verifica política de segurança para arquivos",
    ),
    Tool(
        name="get_history",
        func=get_mr_history,
        description="Busca histórico de MRs anteriores",
    ),
]

llm = OpenAI(temperature=0.3)
agent = initialize_agent(tools, llm, verbose=True)

# 5. Executa agente com contexto do MR
prompt = f"""
Analise este Merge Request e gere checklist de compliance:
- Título: {mr_title}
- Arquivos: {changed_files}
- Descrição: {mr_description}

Use as ferramentas para buscar contexto relevante antes de gerar o checklist.
"""

checklist = agent.run(prompt)
```

### Integração no CI/CD com LangChain

```yaml
# .gitlab-ci.yml
compliance-agent:
  stage: compliance
  image: python:3.11-slim
  script:
    - pip install langchain openai faiss-cpu requests
    - python agente_compliance.py
  rules:
    - if: $CI_MERGE_REQUEST_IID
  variables:
    OPENAI_API_KEY: $OPENAI_API_KEY
  allow_failure: true
```

### Exemplo prático: Agente detecta LGPD automaticamente

**Cenário:** MR altera `src/users/location-tracker.py`

**Agente executa:**
1. **Tool `search_docs`** → encontra ADR-007: "Dados de localização são dados pessoais LGPD"
2. **Tool `check_security`** → detecta arquivo em `src/users/` (crítico)
3. **Tool `get_history`** → encontra MR #42 que teve problema similar

**Checklist gerado pelo agente:**

```markdown
### BLOQUEADORES
1. **[Legal]** Base legal LGPD para dados de localização — verificar se há termo de ciência dos motoristas.
   - Critério: Documento assinado anexado ao MR ou referência a ADR-007.

2. **[Segurança]** Arquivo `src/users/location-tracker.py` é crítico — requer aprovação do time de segurança.
   - Critério: Approval de @security-team no MR.

3. **[Aprovação]** MR similar (#42) teve problema de performance — verificar se teste de carga foi executado.
   - Critério: Resultado de teste de carga anexado ao MR.

### VERIFICAÇÕES OPERACIONAIS
1. **[Operacional]** Comunicar time jurídico sobre novo tratamento de dados de localização.
2. **[Técnico]** Verificar se logs não expõem dados pessoais (PII).

### INFORMATIVOS
1. **[Rastreabilidade]** Atualizar RoPA (Art. 37 LGPD) com nova finalidade de tratamento.
2. **[Documentação]** Referenciar ADR-007 na descrição do MR.
```

### Vantagens do agente LangChain

- **Contexto rico:** busca em documentação interna, ADRs, políticas
- **Memória:** lembra decisões anteriores do projeto
- **Autonomia:** decide quando acionar cada ferramenta
- **Personalização:** adapta checklist ao contexto específico

### Desvantagens

- **Custo:** chamadas múltiplas à API da IA (tools + agente)
- **Complexidade:** requer manutenção do vectorstore e tools
- **Latência:** mais lento que chamada direta (30-60s vs 5-10s)
- **Dependência:** requer `langchain`, `faiss-cpu`, embeddings

### Quando NÃO usar LangChain

- Regras simples e fixas → use script Python puro
- Não tem documentação interna para buscar → chamada direta basta
- Orçamento limitado de API → chamada direta é mais barata
- Precisa de resposta rápida (< 10s) → chamada direta

---

## Comparação das três abordagens

| Abordagem | Arquivo | Custo | Velocidade | Complexidade | Quando usar |
|---|---|---|---|---|---|
| **Regras fixas** | `danger-gitlab-ifsc.py` | Zero | < 1s | Baixa | Governança básica de PRs |
| **IA direta** | `compliance-checker.py` | Baixo (~$0.01/MR) | 5-10s | Média | Checklists contextuais |
| **Agente LangChain** | `agente_compliance.py` | Médio (~$0.05/MR) | 30-60s | Alta | Contexto rico, RAG, memória |

**Recomendação:** comece com `danger-gitlab-ifsc.py` (regras fixas). Adicione `compliance-checker.py` (IA direta) se precisar de checklists contextuais. Use LangChain apenas se tiver documentação interna extensa e precisar de RAG.

---

**Adaptado do Danger.js original por Ahirton Lopes · PM AI Toolkit**  
**Versão GitLab para git.ifsc.edu.br**
