# Backlog Scorer — Guia de Uso

## O que é OKR?

**OKR** = **Objectives and Key Results** (Objetivos e Resultados-Chave)

Framework de metas criado pela Intel e popularizado pelo Google.

**Estrutura:**
- **Objective (O)**: o quê você quer alcançar — qualitativo, inspirador, ambicioso
- **Key Results (KRs)**: como você mede o progresso — 2-5 por objetivo, quantitativos, com prazo

**Exemplo:**
- O: Melhorar a experiência do usuário no app
  - KR1: Reduzir tempo médio de carregamento de 3s para 1s
  - KR2: Aumentar NPS de 30 para 50
  - KR3: Reduzir churn mensal de 8% para 4%

**Características:**
- Ciclos curtos (trimestrais geralmente)
- Metas ambiciosas — 70% de atingimento é considerado sucesso
- Transparentes: todos veem os OKRs da empresa
- Separados de avaliação de desempenho (para incentivar ambição)

**Diferença para KPI:** KPI mede operação contínua (ex: uptime 99,9%); OKR é para mudança/melhoria pontual.

---

## O que é MoSCoW?

MoSCoW é uma técnica de priorização com 4 categorias:

- **M — Must have**: essencial para entrega (sem isso, o projeto falha)
- **S — Should have**: importante, mas não vital (adiável com workaround)
- **C — Could have**: desejável, só se sobrar tempo/recurso
- **W — Won't have (this time)**: fora do escopo atual, registrado para o futuro

**Uso típico no backlog:**
1. Classifique cada item em uma das 4 categorias.
2. Garanta que "Must" não ultrapasse ~60% do esforço — se passar, o escopo está inflado.
3. Negocie "Should" e "Could" conforme capacidade do sprint/release.
4. "Won't" vai para o backlog futuro, não é descartado.

**Dicas práticas:**
- "Must" precisa ser realmente indispensável — se tudo é Must, nada é.
- Envolve stakeholders na classificação, não só devs.
- Combine com estimativas (story points) para validar viabilidade.

---

## O que são RICE Score e WSJF?

Após filtrar o backlog com MoSCoW (Must + Should), você precisa **ordenar** esses itens para saber qual implementar primeiro. É aqui que entram o RICE Score e o WSJF — dois frameworks quantitativos que transformam priorização subjetiva em decisão auditável.

### RICE Score

**O que é:** Framework criado pela Intercom para priorizar features baseado em 4 dimensões mensuráveis.

**Fórmula:**
```
RICE Score = (Reach × Impact × Confidence) / Effort
```

**Componentes:**

| Dimensão | O que mede | Escala | Como estimar |
|----------|------------|--------|--------------|
| **Reach** (Alcance) | Quantos usuários/transações serão afetados por mês | Número absoluto | Ex: 500 candidatos/mês |
| **Impact** (Impacto) | Quão significativo é o efeito para cada usuário | 3=massivo, 2=significativo, 1=médio, 0.5=baixo, 0.25=mínimo | Ex: 3 se reduz tempo de 15 dias para 5 dias |
| **Confidence** (Confiança) | Quão certo você está das estimativas | 100%=evidências sólidas, 80%=indicadores razoáveis, 50%=intuição | Ex: 80% se há dados históricos similares |
| **Effort** (Esforço) | Quanto tempo vai levar em pessoa-mês | Número absoluto | Ex: 2 pessoa-mês |

**Exemplo de cálculo:**
```
US-01 (Cadastrar critério):
- Reach: 500 candidatos/mês
- Impact: 3 (massivo — sem isso, não há fluxo)
- Confidence: 100% (requisito claro, sem ambiguidade)
- Effort: 0.25 pessoa-mês (3 story points)

RICE = (500 × 3 × 1.0) / 0.25 = 6.000
```

**Quando usar RICE:**
- Comparar features com naturezas diferentes (ex: nova feature vs. melhoria de performance)
- Quando você tem dados de uso real (Reach) e estimativas de esforço (Effort)
- Para justificar priorização com números auditáveis

---

### WSJF (Weighted Shortest Job First)

**O que é:** Framework do SAFe (Scaled Agile Framework) que prioriza baseado no **custo do atraso** dividido pelo tamanho do job.

**Fórmula:**
```
WSJF = Cost of Delay / Job Size

Onde:
Cost of Delay = Business Value + Time Criticality + Risk Reduction
```

**Componentes:**

| Dimensão | O que mede | Escala | Como estimar |
|----------|------------|--------|--------------|
| **Business Value** (Valor de Negócio) | Contribuição direta para o OKR | 1-10 | Ex: 10 se é essencial para o OKR |
| **Time Criticality** (Urgência Temporal) | O valor decai se atrasar? Há prazo externo? | 1-10 | Ex: 9 se há deadline regulatório |
| **Risk Reduction** (Redução de Risco) | Desbloqueia outros itens ou reduz risco técnico/compliance? | 1-10 | Ex: 8 se é pré-requisito para 5 outras USs |
| **Job Size** (Tamanho do Job) | Esforço relativo (escala relativa) | 1-10 | Ex: 2 se é pequeno, 8 se é grande |

**Exemplo de cálculo:**
```
US-01 (Cadastrar critério):
- Business Value: 10 (essencial para o OKR)
- Time Criticality: 5 (sem deadline externo, mas habilita o fluxo)
- Risk Reduction: 8 (pré-requisito para US-02, US-05, US-06)
- Job Size: 2 (pequeno — 3 story points)

Cost of Delay = 10 + 5 + 8 = 23
WSJF = 23 / 2 = 11.5
```

**Quando usar WSJF:**
- Quando há dependências entre itens (Risk Reduction alto)
- Quando há prazos externos (Time Criticality alto)
- Quando o valor de negócio varia significativamente entre itens
- Para maximizar o valor entregue por unidade de tempo

**Exemplos de Time Criticality alto:**
- **Mudança na legislação:** Nova lei exige adequação do sistema até data X (ex: LGPD, Lei de Cotas, reforma tributária). Se não entregar no prazo, há multa ou sanção.
- **Cobrança de órgãos reguladores:** MEC, TCU, ANVISA ou outro órgão exige implementação de funcionalidade até data específica sob pena de penalidade.
- **Prazo de edital:** Sistema precisa estar pronto antes da publicação do edital (data fixa e impreterível).
- **Sazonalidade:** Funcionalidade necessária para período específico (ex: matrículas no início do semestre, fechamento fiscal no fim do ano).
- **Janela de oportunidade:** Mercado ou concorrente criou expectativa — atrasar significa perder vantagem competitiva.

---

### RICE vs. WSJF — Quando usar cada um?

| Critério | RICE | WSJF |
|----------|------|------|
| **Foco** | Maximizar impacto por esforço | Minimizar custo do atraso |
| **Melhor para** | Comparar features heterogêneas | Priorizar dentro de um épico |
| **Dependências** | Não considera explicitamente | Considera (Risk Reduction) |
| **Prazos externos** | Não considera explicitamente | Considera (Time Criticality) |
| **Dados necessários** | Reach (usuários afetados) | Business Value (contribuição OKR) |

**Recomendação:** use **ambos em conjunto**. O RICE dá uma visão de eficiência (impacto/esforço), o WSJF dá uma visão de urgência (valor/tempo). O ranking combinado dos dois fornece uma priorização mais robusta.

---

### Como se aplicam na tomada de decisão?

**Cenário:** Você tem 10 User Stories classificadas como Must + Should pelo MoSCoW. Qual implementar primeiro?

**Sem RICE/WSJF:**
- Decisão baseada em opinião ("acho que US-01 é mais importante")
- Viés de âncora (a primeira estimativa vira consenso)
- Difícil justificar para stakeholders

**Com RICE/WSJF:**
- Cada US tem score calculado com critérios explícitos
- Ranking auditável (posso explicar por que US-01 tem prioridade sobre US-08)
- Flags automáticos para incerteza (Confidence < 70%)
- Decisão defendível em reunião de stakeholders

**Exemplo de ranking combinado:**

| US | RICE Score | WSJF | Ranking Combinado |
|----|------------|------|-------------------|
| US-01 | 6.000 | 11.5 | 1º (maior WSJF) |
| US-05 | 4.500 | 9.2 | 2º |
| US-06 | 3.800 | 7.8 | 3º |
| US-08 | 2.100 | 8.5 | 4º (WSJF alto compensa RICE baixo) |

**Decisão:** US-01 tem prioridade máxima porque:
- RICE alto: impacto massivo em 500 usuários/mês
- WSJF alto: desbloqueia 3 outras USs (Risk Reduction = 8)
- Confidence 100%: sem ambiguidade técnica

---

## O que inserir no Backlog Scorer?

### 1. CONTEXTO DE NEGÓCIO

**OKR** — O objetivo estratégico que justifica o projeto:
```
OKR Q4: Implementar fluxo de análise documental para processos seletivos até dezembro de 2026, reduzindo tempo de classificação de 15 dias para 5 dias úteis.
```

**Perfil da empresa/produto** — Domínio, porte, usuários principais:
```
Perfil: Sistema acadêmico de gestão de processos seletivos para cursos de qualificação, especialização e mestrado. Usuários: setor solicitante (admin), candidatos (portal), analistas de documento (coordenadores de curso).
```

**Restrições conhecidas** — Dependências técnicas, decisões pendentes, integrações:
```
Restrições: 
- Dependência de base existente (ENEM) para pontuação declarada — reaproveitamento não mapeado
- Visualizador PDF inline precisa validação técnica
- Decisão pendente: quem cadastra analista (pergunta 5 do documento)
- Formato de exportação depende de referência das convocações atuais
```

### 2. BACKLOG DE INPUT (filtragem automática pelo MoSCoW)

**Copie e referencie o documento de requisitos já mapeados:**

O documento de análise de requisitos contém todas as User Stories mapeadas. A skill vai automaticamente classificar cada US pelo MoSCoW e mostrar a classificação para sua confirmação antes de executar o scoring.

**A skill classifica em:**

| Categoria | Critério | Ação |
|-----------|----------|------|
| **Must** | Sem isso o projeto falha; não há workaround | Sempre inclui no scoring |
| **Should** | Importante; existe workaround temporário | Inclui no scoring |
| **Could** | Desejável; pode ser feito manualmente | Exclui do scoring inicial |
| **Won't** | Fora do escopo atual | Exclui do scoring |

**Exemplo de classificação automática:**

| US | Título | Categoria | Justificativa |
|----|--------|-----------|---------------|
| US-01 | Cadastrar critério | Must | Sem critério, o fluxo não existe |
| US-02 | Configurar pesos | Should | Cálculo manual é workaround viável |
| US-03 | Calendário por edital | Could | Datas podem ser fixas inicialmente |

**Documento de referência:** `../analise-requisitos-analise-documental.md` (diretório pai)

---

## Fluxo de Uso da Skill

1. **Execute a skill:**
   ```
   Use a skill backlog-scorer-skill
   ```

2. **Informe os dados solicitados:**
   - OKR do projeto
   - Perfil da empresa/produto
   - Restrições conhecidas
   - User Stories (copie do documento de análise de requisitos)

3. **A skill vai automaticamente:**
   - Classificar cada US pelo MoSCoW (Must/Should/Could/Won't)
   - Mostrar a classificação em tabela para sua confirmação
   - Aguardar sua aprovação antes de prosseguir
   - Calcular RICE Score e WSJF apenas para Must + Should
   - Gerar ranking combinado
   - Apontar flags de risco/incerteza

4. **Revise o output** e ajuste conforme necessário antes de publicar o ranking.

---

## Exemplo de Uso

**Input:**
```
OKR: Implementar fluxo de análise documental para processos seletivos até dezembro de 2026, reduzindo tempo de classificação de 15 dias para 5 dias úteis.

Perfil: Sistema acadêmico de gestão de processos seletivos para cursos de qualificação, especialização e mestrado. Usuários: setor solicitante (admin), candidatos (portal), analistas de documento (coordenadores de curso).

Restrições: 
- Dependência de base existente (ENEM) para pontuação declarada
- Visualizador PDF inline precisa validação técnica
- Decisão pendente: quem cadastra analista

User Stories:
[Copie do arquivo analise-requisitos-analise-documental.md todas as USs]
```

**Output da skill (automático):**

1. Primeiro, a skill mostra a filtragem MoSCoW:
```
## Filtragem MoSCoW — Confirmação Necessária

| US | Título | Categoria | Justificativa |
|----|--------|-----------|---------------|
| US-01 | Cadastrar critério | Must | Sem critério, o fluxo não existe |
| US-02 | Configurar pesos | Should | Cálculo manual é workaround viável |
| US-03 | Calendário por edital | Could | Datas podem ser fixas inicialmente |
| US-05 | Tipo de documento | Must | Sem tipos, não há pontuação |
| ... | ... | ... | ... |

Total: 5 Must, 5 Should, 6 Could, 0 Won't

Para o scoring, usarei apenas: Must + Should (10 histórias)

Confirma esta classificação? (Sim/Não/Ajustar)
```

2. Após confirmação, a skill executa o RICE/WSJF apenas nas Must + Should

**Output esperado:**
- Tabela RICE com Reach, Impact, Confidence, Effort e Score
- Tabela WSJF com Business Value, Time Criticality, Risk Reduction, Cost of Delay, Job Size e WSJF
- Ranking combinado em ordem decrescente
- Justificativas para Impact e Confidence
- Flags para itens com incerteza alta

---

*Baseado no template original de Ahirton Lopes · PM AI Toolkit*
