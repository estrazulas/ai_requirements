# Módulo 10: Portfolio e OKRs - OKR Aligner
> **UNIPDS: Ferramentas de IA para Gestão de Projetos**
> **Prof. Ahirton Lopes, Ph.D.**

---

## Visão Geral

O **OKR Aligner** é um framework de 3 partes para alinhar estratégia de produto com OKRs mensuráveis. Fluxo completo:

1. **Parte A** — Valida qualidade dos OKRs (baseline, métrica, prazo)
2. **Parte B** — Classifica backlog segundo alinhamento com OKRs
3. **Parte C** — Scorecard executivo de portfólio multi-projeto

---

## Parte A: Validação de OKRs

### O que faz
Avalia se seus OKRs estão bem formulados antes de comprometer publicamente. Identifica gaps estruturais: baseline ausente, métrica vaga, prazo indefinido.

### Quando usar
- Antes de iniciar qualquer ciclo de OKRs
- Quando você tem objetivos qualitativos mas precisa transformá-los em KRs mensuráveis
- Antes de rodar a Parte B (alinhamento de backlog)

### Critérios de validação
Para cada Key Result, avalie:
- ✅ **Mensurável** — tem número/indicador claro (não "melhorar" sem percentual)
- ✅ **Baseline declarada** — valor atual explícito (sem baseline, não há como verificar atingimento)
- ✅ **Prazo definido** — data específica ou coincide com ciclo declarado
- ✅ **Responsável implícito** — time/pessoa dona do resultado
- ✅ **Independente de output** — mede resultado de negócio (outcome), não entrega (output)
- ✅ **Verificável por terceiro** — auditor externo consegue verificar se foi atingido

### Exemplo do nosso projeto

**Objetivo:** Migrar análise documental do processo manual para o sistema

**KR 1.1:** % editais processados pelo sistema
- Baseline: 0% (todos manuais hoje)
- Alvo: 80%
- Prazo: março 2027
- Status: ✅ todos os critérios atendidos

**KR 1.2:** Tempo médio de análise por candidato
- Baseline: 30 dias
- Alvo: 7 dias
- Prazo: março 2027
- Status: ✅ todos os critérios atendidos

**Objetivo:** Dar transparência ao candidato sobre avaliação e resultados

**KR 2.1:** % candidatos que consultam o portal
- Baseline: 0% (portal não existe)
- Alvo: 60%
- Prazo: março 2027
- Status: ✅ todos os critérios atendidos

**KR 2.2:** Chamados sobre status (ligações/emails)
- Baseline: 50/mês
- Alvo: 0
- Prazo: março 2027
- Status: ✅ todos os critérios atendidos

**KR 2.3:** Tempo para candidato ver resultado após publicação
- Baseline: 30 dias
- Alvo: 1 dia
- Prazo: março 2027
- Status: ✅ todos os critérios atendidos

### Output esperado
Para cada ❌ identificado: descreva o problema específico e sugira reformulação corrigida.

**Exemplo de gap identificado (se baseline estivesse ausente):**
> ❌ **Baseline não declarada** — qual é o tempo atual de análise por candidato? Sem baseline, o atingimento de "7 dias" não é verificável. Reformulação sugerida: "Reduzir tempo médio de análise de [30 dias] para [7 dias] até março 2027."

---

## Parte B: Alinhamento Backlog × OKRs

### O que faz
Classifica cada item do backlog segundo grau de alinhamento com OKRs do ciclo. Identifica itens que consomem capacidade sem contribuir para estratégia.

### Quando usar
- Depois de validar OKRs na Parte A
- Quando precisa decidir o que priorizar no próximo ciclo/sprint
- Para defender remoção/postergação de itens com argumento estratégico

### 4 categorias de classificação

| Categoria | Definição |
|---|---|
| **Alinhado Diretamente** | Contribui de forma direta e mensurável para pelo menos um KR |
| **Alinhado Indiretamente** | Viabiliza um item diretamente alinhado, mas não move o KR por si só |
| **Não Alinhado** | Não tem relação clara com nenhum OKR do ciclo atual |
| **Épico Futuro sem OKR** | Tem valor potencial mas sem OKR correspondente neste ciclo |

### Exemplo do nosso projeto

**Input:** 16 user stories do backlog de processos seletivos acadêmicos

**Output:**

| Item | Status | Alinhamento | OKR Relacionado | Justificativa |
|---|---|---|---|---|
| US-01 Cadastrar critério AD no edital | ativo | **Alinhado Diretamente** | OKR 1 / KR 1.1 | Habilita fluxo digital — sem isso, edital não usa sistema |
| US-08 Analista pontua documentos | ativo | **Alinhado Diretamente** | OKR 1 / KR 1.1 + KR 1.2 | Coração da análise digital + redução de tempo 30→7 dias |
| US-16 Candidato visualiza status | ativo | **Alinhado Diretamente** | OKR 2 / KR 2.1 + KR 2.2 + KR 2.3 | Portal + transparência + redução de chamados + tempo 30→1 dia |
| US-13 Perfil Analista de Documento | ativo | **Alinhado Indiretamente** | OKR 1 | Viabiliza US-08 (segurança) mas não move KR por si só |
| US-12 Exportar classificação CSV/HTML | ativo | **Não Alinhado** | — | Automação de publicação externa — não move nenhum KR |

### Resumo de distribuição
- **Alinhados Diretamente:** 8 itens (50%)
- **Alinhados Indiretamente:** 6 itens (37,5%)
- **Não Alinhados:** 1 item (6,25%)
- **Épicos Futuros sem OKR:** 0 itens

### Recomendações geradas

**1. Itens candidatos à postergação:**
- **US-12 (Exportar CSV/HTML)** — Não Alinhado. Publicação externa continua funcionando manualmente. Mover para Q2 2027.
- **Convergência de frameworks:** Se aplicarmos WSJF (Módulo 2), US-12 teria Business Value baixo (2) e Time Criticality baixa (2). Quando dois frameworks independentes chegam à mesma conclusão, recomendação de postergar é fortíssima.

**2. Alertas de dependência:**
- **US-13 → US-08:** US-13 (perfil analista) é pré-requisito de segurança para US-08. Se US-13 atrasar, US-08 bloqueia, e todo épico E4 fica em risco.
- **US-08/US-11 → US-14/US-16:** Portal do candidato depende de dados gerados pela análise. Garantir que US-08 entre em produção antes ou junto com US-14/US-16.

**3. Itens de alta alavancagem (movem múltiplos KRs):**
- **US-08** → KR 1.1 + KR 1.2 (maior ROI estratégico)
- **US-16** → KR 2.1 + KR 2.2 + KR 2.3 (maior ROI estratégico)

### Curadoria — Pontos de discussão

**Ponto 1 — Convergência de frameworks:**
US-12 rejeitada por dois frameworks independentes (OKR Aligner + WSJF). Argumento defensável: não é opinião, é convergência de evidência.

**Ponto 2 — Cadeia de dependência crítica:**
US-13 → US-08 é exatamente o tipo de risco que OKR Aligner torna visível — raramente aparece em reunião de priorização manual.

**Ponto 3 — Classificação limítrofe:**
US-07 (candidato altera documentos) foi classificada como Alinhada Indiretamente. Poderia ser Direta se argumento for "reduz retrabalho do analista". Decisão é humana, framework informa.

---

## Parte C: Scorecard de Portfólio Multi-Projeto

### O que faz
Consolida dados de múltiplos projetos em scorecard executivo de saúde estratégica. Aplica rúbrica de semáforo (🟢🟡🔴) baseada em progresso dos KRs.

### Quando usar
- Quando você gerencia mais de um projeto simultaneamente
- Para reunião de portfólio com gestor/diretoria
- Para identificar riscos transversais (recursos compartilhados)

### Rúbrica de semáforo

| Status | Critério |
|---|---|
| 🟢 **Verde** | Todos os KRs com progresso >= 60% do proporcional ao tempo decorrido do ciclo E nenhum blocker sem dono |
| 🟡 **Amarelo** | Pelo menos um KR entre 40% e 60% do proporcional OU blocker ativo com dono e plano de mitigação |
| 🔴 **Vermelho** | Qualquer KR abaixo de 40% do proporcional OU qualquer blocker sem dono identificado |

**Regra de cálculo:** Progresso proporcional se calcula contra tempo decorrido do ciclo. Ex: 50% do ciclo decorrido → KR esperado em >= 30% para ser Verde (regra dos 60%).

### Exemplo hipotético (se tivéssemos 3 projetos)

**Cenário:**
- **Projeto 1:** Processos Seletivos (análise documental) — ciclo Q1 2027, hoje: fevereiro (~33% decorrido)
  - KR 1.1: 80% editais digitais — progresso: 20% (25% do alvo)
  - KR 1.2: Tempo 30→7 dias — progresso: 22 dias (27% do alvo)
  - Blocker: visualizador PDF pendente de validação técnica — dono: time de engenharia, POC em andamento
  
- **Projeto 2:** Portal do Aluno (nova interface) — ciclo Q1 2027
  - KR: aumentar NPS de 35 para 50 — progresso: NPS atual 42 (43% do alvo)
  - Sem blockers — no prazo
  
- **Projeto 3:** Integração com Sistema Financeiro — ciclo Q1 2027
  - KR: reduzir tempo de conciliação de 2h para 15min — progresso: parado há 3 semanas
  - Blocker: API do sistema financeiro não documentada — SEM dono definido

**Output do scorecard:**

| Projeto | Status | Dimensão crítica | Motivo | Próxima ação |
|---|---|---|---|---|
| Processos Seletivos | 🟡 Amarelo | Cronograma | KRs em 25-27% do alvo (esperado 30%) | Acelerar validação do visualizador PDF — dono: engenharia |
| Portal do Aluno | 🟢 Verde | — | No prazo, sem blockers | Continuar execução |
| Integração Financeiro | 🔴 Vermelho | Blocker sem dono | API não documentada, parado há 3 semanas | **Decisão urgente:** atribuir dono para desbloquear API |

**Riscos transversais:**
- Time de engenharia atende os 3 projetos (Processos Seletivos: visualizador PDF; Portal: frontend; Integração: backend)
- **Ponto único de falha:** se engenharia priorizar Integração Financeiro, Processos Seletivos e Portal atrasam

**Foco da reunião de portfólio (máximo 3 itens):**
1. Atribuir dono para API do sistema financeiro (blocker crítico — Projeto 3 🔴)
2. Decidir se realoca dev de backend da Integração para Processos Seletivos (risco de atraso — Projeto 1 🟡)
3. Confirmar prazo de validação do visualizador PDF (dependência crítica — Projeto 1 🟡)

**Regra de ouro:** Se nenhum projeto estiver Vermelho, reunião pode ser substituída por envio assíncrono do dashboard — silêncio significa OK.

---

## Notas de Design

### Por que separar em Parte A e Parte B?
Validação dos OKRs deve acontecer antes do alinhamento — um OKR com baseline ausente invalida toda análise de alinhamento subsequente.

### Por que a distinção Output × Outcome importa no backlog?
"Entregar módulo de análise" é output. "Reduzir tempo de análise de 30 para 7 dias" é outcome. Alinhamento correto mapeia features para outcomes, não para outros outputs.

### Por que a Parte C é separada?
Scorecard de portfólio é para gestores com múltiplos projetos. Se você gerencia apenas 1 projeto, Partes A e B são suficientes.

---

## Arquivos deste repositório

- `okr-alinhamento-backlog.md` — Partes A e B aplicadas ao projeto de processos seletivos acadêmicos
- `okr-aligner-prompt.md` (na raiz do módulo) — Prompts originais do professor com exemplos RouteWise

---

*Documento gerado em 2026-10-11 como parte do Módulo 10 - Portfolio e OKRs*
*Prof. Ahirton Lopes, Ph.D. — UNIPDS: Ferramentas de IA para Gestão de Projetos*
