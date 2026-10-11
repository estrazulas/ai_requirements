# Simulação Local dos Scripts de Governança

Este guia explica como testar os scripts de governança localmente usando arquivos de mock, sem precisar do GitLab ou de MRs reais.

## Pré-requisitos

### 1. Configurar ambiente virtual

```bash
cd modulo-08-governanca-e-compliance/resolucao

# Executa o script de setup (cria venv e instala dependências)
./setup.sh

# Ou manualmente:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configurar chave da API (apenas para compliance-checker)

Edite o arquivo `.env` e adicione sua chave:

```bash
# Para OpenAI
OPENAI_API_KEY=sk-your-key-here

# Ou para Anthropic
ANTHROPIC_API_KEY=sk-ant-your-key-here
AI_PROVIDER=anthropic
```

**Nota:** O script `danger-gitlab-ifsc.py` não precisa de API key.

---

## Cenário 1: MR que PASSA em todas as regras

### Arquivo: `mr-mock-sucesso.json`

Este mock representa um Merge Request bem configurado:

- **Título:** `fix: corrige bug de conexao GPS #42` (tem referência a issue)
- **Descrição:** Detalhada, com mais de 30 caracteres
- **Linhas alteradas:** 359 (abaixo do limite de 500)
- **Aprovadores:** 2 (Priya e Carlos)
- **Arquivos críticos:** Sim (`src/integrations/gps`, `src/api/routes`)
- **Cobertura:** 81.4% (queda de 1.7 pontos, dentro do limite de 5)

### Testando o script de governança

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

  1. Arquivo critico com 2 aprovadores -- requisito de revisao atendido. (src/integrations/gps/tracker-client.js, src/api/routes/alerts.js)
  2. Cobertura de testes: 81.4% (queda de 1.7p em relacao a base 83.1%) -- dentro do limite aceitavel.
  3. Dados de cobertura encontrados e validados.

------------------------------------------------------------
Status final: OK
------------------------------------------------------------
```

**Interpretação:** ✅ Todas as regras passaram. O MR pode ser mergeado.

### Testando o compliance-checker com IA

```bash
python compliance-checker.py --local --mock mr-mock-sucesso.json
```

**Saída esperada (exemplo):**

```
============================================================
COMPLIANCE CHECK -- GERANDO CHECKLIST COM IA
============================================================

[OPENAI] Usando modelo gpt-4o-mini...

### BLOQUEADORES
1. **[Aprovação]** Arquivos críticos modificados exigem 2 aprovadores — MR toca `src/integrations/gps` e `src/api/routes`.
   - Critério: MR tem 2 approvals confirmados.

2. **[Técnico]** Referência a issue obrigatória — MR contém `#42` no título.
   - Critério: Regex `#\d+` encontra match.

### VERIFICAÇÕES OPERACIONAIS
1. **[Operacional]** MR com 359 linhas — abaixo do limite de 500, mas considere dividir se possível.
2. **[Técnico]** Cobertura caiu 1.7 pontos (83.1% → 81.4%) — dentro do limite de 5 pontos.

### INFORMATIVOS
1. **[Rastreabilidade]** Registrar hash do commit e autor do MR para auditoria.
2. **[Documentação]** Atualizar changelog com referência ao MR #42.

============================================================

[OK] Checklist postado no Merge Request.
```

**Interpretação:** ✅ IA gerou checklist contextual confirmando que o MR está em conformidade.

---

## Cenário 2: MR que FALHA em múltiplas regras

### Arquivo: `mr-mock-falha.json`

Este mock representa um Merge Request mal configurado:

- **Título:** `fix: corrige bug de conexao GPS` (sem referência a issue)
- **Descrição:** `corrigido` (apenas 1 palavra, menos de 30 caracteres)
- **Linhas alteradas:** 635 (acima do limite de 500)
- **Aprovadores:** 1 (apenas junior-dev, precisa de 2 para arquivos críticos)
- **Arquivos críticos:** Sim (`src/integrations/gps`, `src/services/notifications`)
- **Cobertura:** 72.0% (queda de 11.1 pontos, acima do limite de 5)

### Testando o script de governança

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

  1. Referencia a issue nao encontrada. O titulo ou a descricao deve conter o numero da issue (ex: #42). Isso garante rastreabilidade entre o MR e o trabalho planejado.
  2. Arquivo critico modificado com aprovadores insuficientes. Este MR toca modulos de integracao ou arquivos sensiveis. Necessario pelo menos 2 aprovadores (atual: 1). Arquivos criticos: src/integrations/gps/tracker-client.js, src/integrations/gps/guard-filter.js, src/services/notifications/email.js

AVISOS (2) -- nao bloqueiam:

  1. MR grande detectado (635 linhas alteradas). MRs acima de 500 linhas aumentam o risco de bugs. Considere dividir em MRs menores ou agendar revisao dedicada.
  2. Cobertura de testes caiu 11.1 pontos (de 83.1% para 72.0%). Queda acima de 5% indica codigo novo sem cobertura. Adicione testes ou justifique na descricao.

------------------------------------------------------------
Status final: FALHOU
------------------------------------------------------------
```

**Interpretação:** ❌ 2 falhas bloqueiam o merge. O MR não pode ser mergeado até que:
1. Adicione referência a issue no título ou descrição (ex: `#42`)
2. Obtenha mais 1 aprovador (total de 2) para arquivos críticos

**Como resolver:**
- Edite o título para: `fix: corrige bug de conexao GPS #42`
- Peça para outro desenvolvedor aprovar o MR
- Considere dividir o MR em partes menores (635 linhas é muito)
- Adicione testes para melhorar a cobertura

### Testando o compliance-checker com IA

```bash
python compliance-checker.py --local --mock mr-mock-falha.json
```

**Saída esperada (exemplo):**

```
============================================================
COMPLIANCE CHECK -- GERANDO CHECKLIST COM IA
============================================================

[OPENAI] Usando modelo gpt-4o-mini...

### BLOQUEADORES
1. **[Técnico]** Referência a issue obrigatória — MR não contém `#NÚMERO` no título ou descrição.
   - Critério: Regex `#\d+` deve encontrar match.

2. **[Aprovação]** Arquivos críticos exigem 2 aprovadores — MR toca `src/integrations/gps` e `src/services/notifications` mas tem apenas 1 approval.
   - Critério: MR precisa de 2 approvals com status "approved".

### VERIFICAÇÕES OPERACIONAIS
1. **[Operacional]** MR com 635 linhas — acima do limite de 500. Considere dividir em MRs menores.
2. **[Técnico]** Cobertura caiu 11.1 pontos (83.1% → 72.0%) — acima do limite de 5 pontos. Adicione testes para o código novo.
3. **[Documentação]** Descrição muito curta ("corrigido") — explique o que muda e por que.

### INFORMATIVOS
1. **[Rastreabilidade]** Atualizar descrição do MR com contexto detalhado.
2. **[Qualidade]** Adicionar testes unitários para melhorar cobertura.

============================================================

[OK] Checklist postado no Merge Request.
```

**Interpretação:** ❌ IA identificou os mesmos problemas e gerou recomendações contextuais.

---

## Personalizando as regras

Edite o arquivo `governance-config.json` para ajustar as regras:

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

### Exemplo: Permitir MRs maiores

```json
{
  "large_mr_threshold": 1000
}
```

Depois teste novamente:

```bash
python danger-gitlab-ifsc.py --local --mock mr-mock-falha.json
```

Agora o aviso de "MR grande" não aparecerá (635 < 1000).

### Exemplo: Usar padrão diferente para issues

Se seu projeto usa `ISSUE-123` em vez de `#123`:

```json
{
  "issue_pattern": "ISSUE-\\d+"
}
```

Edite o `mr-mock-sucesso.json`:

```json
{
  "mr": {
    "title": "fix: corrige bug de conexao GPS ISSUE-42",
    ...
  }
}
```

Teste:

```bash
python danger-gitlab-ifsc.py --local --mock mr-mock-sucesso.json
```

---

## Criando seus próprios mocks

Copie um dos arquivos existentes e edite:

```bash
cp mr-mock-sucesso.json meu-mock.json
```

Edite `meu-mock.json`:

```json
{
  "mr": {
    "title": "feat: nova funcionalidade #99",
    "description": "Implementa nova funcionalidade de relatórios...",
    "changes_count": 250
  },
  "changed_files": [
    "src/features/reports.js",
    "tests/features/reports.test.js"
  ],
  "approvals": [
    { "username": "revisor-1" }
  ],
  "coverage": {
    "total": { "lines": { "pct": 85.0 } }
  },
  "base_coverage": {
    "total": { "lines": { "pct": 85.0 } }
  }
}
```

Teste:

```bash
python danger-gitlab-ifsc.py --local --mock meu-mock.json
python compliance-checker.py --local --mock meu-mock.json
```

---

## Resumo dos comandos

### Script de governança (regras fixas, sem IA)

```bash
# MR que passa
python danger-gitlab-ifsc.py --local --mock mr-mock-sucesso.json

# MR que falha
python danger-gitlab-ifsc.py --local --mock mr-mock-falha.json
```

### Compliance-checker (com IA, precisa de API key)

```bash
# MR que passa
python compliance-checker.py --local --mock mr-mock-sucesso.json

# MR que falha
python compliance-checker.py --local --mock mr-mock-falha.json
```

### Sair do ambiente virtual

```bash
deactivate
```

---

## Próximos passos

Depois de testar localmente, veja o `README.md` para:
- Configurar no GitLab CI/CD
- Usar agente LangChain com RAG
- Personalizar regras avançadas
