# Guia de Referência Rápida — Priorização de Backlog

> Documento genérico de referência para priorização de backlog com RICE Score e WSJF.
> Válido para qualquer projeto de software.

---

## 1. SIGLAS E DEFINIÇÕES

| Sigla | Significado | Definição |
|-------|-------------|-----------|
| **RICE** | Reach, Impact, Confidence, Effort | Framework da Intercom para priorizar features baseado em 4 dimensões mensuráveis |
| **WSJF** | Weighted Shortest Job First | Framework do SAFe que prioriza baseado no custo do atraso dividido pelo tamanho do job |
| **OKR** | Objectives and Key Results | Framework de metas: objetivo qualitativo + resultados-chave quantitativos |
| **MoSCoW** | Must, Should, Could, Won't | Técnica de priorização com 4 categorias para filtrar backlog |
| **BV** | Business Value | Valor de negócio — contribuição direta para o OKR (escala 1-10) |
| **TC** | Time Criticality | Urgência temporal — o valor decai se atrasar? (escala 1-10) |
| **RR** | Risk Reduction | Redução de risco — desbloqueia outros itens ou reduz risco técnico? (escala 1-10) |
| **CoD** | Cost of Delay | Custo do atraso — soma de BV + TC + RR |
| **SP** | Story Points | Medida relativa de complexidade/esforço (escala Fibonacci) |
| **pm** | pessoa-mês | Unidade de esforço — 1 pessoa trabalhando por 1 mês (≈ 20 dias úteis) |

---

## 2. ESCALAS

### 2.1 Escala Fibonacci (Story Points)

**Sequência:** 0.5, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

**Por que não linear (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)?**
- Escala linear dá falsa precisão ("é 7 ou 8 pontos?")
- Fibonacci força decisões claras ("é 5 ou 8 pontos?" — diferença de 60%)
- Quanto maior o número, maior a incerteza

**Regra:** Se uma User Story ultrapassar 13 Story Points, decomponha em histórias menores.

---

### 2.2 Impact (RICE)

**O que mede:** Quão significativo é o efeito para cada usuário afetado.

| Valor | Significado | Exemplo |
|-------|-------------|---------|
| **3** | Massivo | Sem isso, o fluxo não existe; impacto crítico no negócio |
| **2** | Significativo | Melhoria substancial, mas existe workaround |
| **1** | Médio | Melhoria incremental, impacto moderado |
| **0.5** | Baixo | Melhoria marginal, poucos usuários afetados |
| **0.25** | Mínimo | Impacto quase imperceptível |

**Exemplo:**
- US que habilita fluxo principal: Impact = 3
- US que automatiza cálculo manual: Impact = 2
- US que melhora UX de um formulário: Impact = 1

---

### 2.3 Confidence (RICE)

**O que mede:** Quão certo você está das estimativas de Reach, Impact e Effort.

| % | Significado | Quando usar |
|---|-------------|-------------|
| **100%** | Certeza absoluta | Requisitos claros, time já fez feature similar, dados históricos disponíveis |
| **80%** | Alta confiança | Requisitos bem definidos, alguma experiência prévia, indicadores razoáveis |
| **50%** | Intuição | Feature nova, sem dados históricos, dependências não mapeadas |
| **< 50%** | Especulação | Muita incerteza, dependências externas não validadas, tecnologia desconhecida |

**Na fórmula RICE:** Confidence age como um "desconto" — se você não tem certeza, o score cai proporcionalmente.

**Exemplo:**
- CRUD simples que o time já fez: Confidence = 100%
- Tela com lógica complexa mas requisitos claros: Confidence = 80%
- Feature com visualizador PDF (tecnologia desconhecida): Confidence = 50-60%

---

### 2.4 Time Criticality (WSJF)

**O que mede:** Quão urgente é entregar essa US. O valor de negócio decai com o tempo?

| Valor | Significado | Exemplo |
|-------|-------------|---------|
| **9-10** | Deadline fixo e impreterível | Mudança na legislação (LGPD), cobrança de órgão regulador (MEC, TCU), prazo de edital |
| **7-8** | Prazo importante mas com flexibilidade | Lançamento de produto, evento sazonal (matrículas, Black Friday) |
| **5-6** | Benefício de entregar logo, sem pressão externa | Melhoria competitiva, redução de custo operacional |
| **3-4** | Pode esperar sem perda significativa | Feature desejável, melhoria incremental |
| **1-2** | Sem urgência — valor não decai com o tempo | Refatoração interna, melhoria de código |

**Exemplo:**
- Lei exige implementação até março/2027: TC = 9
- Próximo edital publica em abril: TC = 8
- Melhoria competitiva sem prazo: TC = 5
- Refatoração interna: TC = 2

---

### 2.5 Business Value (WSJF)

**O que mede:** Contribuição direta para o OKR do projeto.

| Valor | Significado | Exemplo |
|-------|-------------|---------|
| **9-10** | Essencial para o OKR | Sem isso, o objetivo estratégico não é alcançado |
| **7-8** | Muito importante | Contribui significativamente, mas não é crítico |
| **5-6** | Importante | Contribui moderadamente para o OKR |
| **3-4** | Moderado | Contribui pouco, mas ainda tem valor |
| **1-2** | Baixo | Contribuição mínima ou indireta |

**Exemplo:**
- US que habilita fluxo principal do OKR: BV = 10
- US que automatiza processo manual: BV = 7
- US que melhora UX: BV = 4

---

### 2.6 Risk Reduction (WSJF)

**O que mede:** Desbloqueia outros itens ou reduz risco técnico/compliance?

| Valor | Significado | Exemplo |
|-------|-------------|---------|
| **9-10** | Pré-requisito para múltiplas USs | Desbloqueia 5+ outras histórias; reduz risco crítico de compliance |
| **7-8** | Pré-requisito para algumas USs | Desbloqueia 2-4 outras histórias; reduz risco técnico significativo |
| **5-6** | Desbloqueia 1 US ou reduz risco moderado | Pré-requisito para 1 história; reduz risco moderado |
| **3-4** | Reduz risco baixo | Melhora testabilidade ou manutenibilidade |
| **1-2** | Sem impacto em risco | Não desbloqueia nada, não reduz risco |

**Exemplo:**
- US que cria base de dados para 5 outras USs: RR = 9
- US que implementa API usada por 3 telas: RR = 7
- US que é independente: RR = 2

---

### 2.7 Job Size (WSJF)

**O que mede:** Esforço relativo (escala relativa 1-10).

| Valor | Significado | Story Points equivalente |
|-------|-------------|--------------------------|
| **1** | Muito pequeno | 1-2 SP |
| **2-3** | Pequeno | 3-5 SP |
| **4-5** | Médio | 5-8 SP |
| **6-7** | Grande | 8-13 SP |
| **8-10** | Muito grande | 13+ SP |

**Exemplo:**
- CRUD simples: Job Size = 2
- Tela com validações: Job Size = 5
- Tela complexa com visualizador: Job Size = 8

---

## 3. FÓRMULAS

### 3.1 RICE Score

```
RICE Score = (Reach × Impact × Confidence) / Effort
```

**Onde:**
- **Reach:** Quantos usuários/transações serão afetados por mês (número absoluto)
- **Impact:** 3=massivo, 2=significativo, 1=médio, 0.5=baixo, 0.25=mínimo
- **Confidence:** 100%=certeza absoluta, 80%=alta confiança, 50%=intuição
- **Effort:** Esforço em pessoa-mês (pm)

**Exemplo de cálculo:**

```
US-01: Cadastrar critério AD no edital
- Reach: 10 (10 editais/mês)
- Impact: 3 (massivo — habilita o fluxo principal)
- Confidence: 100% (CRUD simples, time já fez)
- Effort: 0.2 pm (2 Story Points)

RICE = (10 × 3 × 1.0) / 0.2 = 150
```

```
US-06: Candidato declara pontuação ao enviar documentos
- Reach: 2000 (2000 candidatos/mês)
- Impact: 3 (massivo — coração do fluxo de inscrição)
- Confidence: 80% (base ENEM existe, mas reaproveitamento não mapeado)
- Effort: 0.5 pm (8 Story Points)

RICE = (2000 × 3 × 0.8) / 0.5 = 9600
```

---

### 3.2 Cost of Delay (WSJF)

```
Cost of Delay = Business Value + Time Criticality + Risk Reduction
```

**Onde:**
- **Business Value:** 1-10 (contribuição para o OKR)
- **Time Criticality:** 1-10 (urgência temporal)
- **Risk Reduction:** 1-10 (desbloqueia outros itens ou reduz risco)

**Exemplo de cálculo:**

```
US-01: Cadastrar critério AD no edital
- Business Value: 10 (essencial para o OKR)
- Time Criticality: 5 (sem deadline externo, mas habilita o fluxo)
- Risk Reduction: 8 (pré-requisito para US-02, US-05, US-06)

Cost of Delay = 10 + 5 + 8 = 23
```

---

### 3.3 WSJF

```
WSJF = Cost of Delay / Job Size
```

**Onde:**
- **Cost of Delay:** BV + TC + RR (calculado acima)
- **Job Size:** 1-10 (esforço relativo)

**Exemplo de cálculo:**

```
US-01: Cadastrar critério AD no edital
- Cost of Delay: 23 (calculado acima)
- Job Size: 2 (pequeno — 2 Story Points)

WSJF = 23 / 2 = 11.5
```

---

## 4. TABELAS DE CONVERSÃO

### 4.1 Story Points → Pessoa-mês

| Story Points | Effort (pm) | Tempo real (1 pessoa) |
|--------------|-------------|------------------------|
| 0.5 | 0.05 | 1 dia |
| 1 | 0.1 | 2 dias |
| 2 | 0.2 | 4 dias |
| 3 | 0.25 | 1 semana (5 dias) |
| 5 | 0.5 | 2 semanas (10 dias) |
| 8 | 1.0 | 1 mês (20 dias) |
| 13 | 2.0 | 2 meses (40 dias) |
| 21 | 3.0 | 3 meses (60 dias) |

**Conversão:**
- 1 pm = 1 pessoa trabalhando por 1 mês (≈ 20 dias úteis)
- 0.5 pm = 1 pessoa trabalhando por 2 semanas (≈ 10 dias úteis)
- 0.25 pm = 1 pessoa trabalhando por 1 semana (≈ 5 dias úteis)

---

### 4.2 Capacidade do Time → Sprints necessárias

```
Sprints necessárias = Total de Story Points ÷ Velocidade do Time (SP/sprint)
```

**Exemplo:**

```
Backlog: 84 Story Points
Velocidade do time: 40 SP/sprint

Sprints = 84 ÷ 40 = 2.1 sprints ≈ 3 sprints (com buffer)
```

---

## 5. NÍVEIS DE COMPLEXIDADE

### 5.1 Tabela de Referência por Tipo de Tarefa

| Tipo de Tarefa | Simples | Médio | Complexo |
|----------------|---------|-------|----------|
| **CRUDs / Cadastros** | 1-2 pts | 3-5 pts | 8 pts |
| **Telas de Processamento** | 2-3 pts | 5-8 pts | 13 pts |
| **Entrada de Dados** | 1-2 pts | 3-5 pts | 8 pts |
| **Listas e Relatórios** | 1-2 pts | 3-5 pts | 8 pts |
| **Portal / Autoatendimento** | 1-2 pts | 3-5 pts | 8 pts |

---

### 5.2 Critérios para Classificar Complexidade

| Critério | Simples | Médio | Complexo |
|----------|---------|-------|----------|
| **Número de campos** | 1-2 | 3-5 | 6+ |
| **Validações** | Nenhuma/pouca | Regras de negócio simples | Cálculos/dependências |
| **Campos condicionais** | Nenhum | Alguns | Muitos com lógica |
| **Integrações** | Nenhuma | Vínculo a 1 entidade | Múltiplas dependências |
| **Visualização** | Sem visualizador | Sem visualizador | Visualizador de documentos |

---

### 5.3 Exemplos Práticos

**Exemplo 1: CRUD Simples**
```
US-01: Cadastrar critério AD no edital
- Tipo: CRUD
- Campos: 1-2 (combobox + checkbox)
- Validações: Exclusividade com outro critério
- Classificação: Simples → 2 Story Points
```

**Exemplo 2: Tela de Processamento Complexa**
```
US-08: Analista pontua documentos do candidato
- Tipo: Tela de Processamento
- Campos: 6+ (pontuação, justificativa, visualizador, lista)
- Validações: Cálculo ponderado, auditoria
- Integrações: Visualizador PDF, base de documentos
- Classificação: Complexo → 13 Story Points
```

**Exemplo 3: Entrada de Dados Média**
```
US-07: Candidato altera documentos e pontuação dentro do prazo
- Tipo: Entrada de Dados
- Campos: 3-5 (arquivo, pontuação, validação de prazo)
- Validações: Controle de edição baseado em data
- Classificação: Médio → 5 Story Points
```

---

## 6. EXEMPLOS DE CÁLCULO COMPLETO

### 6.1 Exemplo RICE Completo

**Cenário:** 3 User Stories para priorizar

| US | Título | Reach | Impact | Confidence | Effort (pm) | RICE Score |
|----|--------|-------|--------|------------|-------------|------------|
| US-01 | Cadastrar critério AD | 10 | 3 | 100% | 0.2 | 150 |
| US-06 | Candidato declara pontuação | 2000 | 3 | 80% | 0.5 | 9600 |
| US-08 | Analista pontua documentos | 10 | 3 | 60% | 1.0 | 18 |

**Cálculos:**

```
US-01: RICE = (10 × 3 × 1.0) / 0.2 = 150
US-06: RICE = (2000 × 3 × 0.8) / 0.5 = 9600
US-08: RICE = (10 × 3 × 0.6) / 1.0 = 18
```

**Ranking por RICE:**
1. US-06 (9600) — maior alcance e impacto
2. US-01 (150) — essencial mas baixo alcance
3. US-08 (18) — complexa com baixa confiança

---

### 6.2 Exemplo WSJF Completo

**Cenário:** 3 User Stories para priorizar

| US | Título | BV | TC | RR | CoD | Job Size | WSJF |
|----|--------|----|----|----|----|----------|------|
| US-01 | Cadastrar critério AD | 10 | 5 | 8 | 23 | 2 | 11.5 |
| US-06 | Candidato declara pontuação | 10 | 6 | 9 | 25 | 5 | 5.0 |
| US-08 | Analista pontua documentos | 10 | 6 | 10 | 26 | 8 | 3.3 |

**Cálculos:**

```
US-01: CoD = 10 + 5 + 8 = 23 → WSJF = 23 / 2 = 11.5
US-06: CoD = 10 + 6 + 9 = 25 → WSJF = 25 / 5 = 5.0
US-08: CoD = 10 + 6 + 10 = 26 → WSJF = 26 / 8 = 3.3
```

**Ranking por WSJF:**
1. US-01 (11.5) — alto valor, baixa urgência, mas desbloqueia muitas USs e é pequeno
2. US-06 (5.0) — alto valor e urgência, mas tamanho médio
3. US-08 (3.3) — alto valor e urgência, mas muito grande

---

### 6.3 Exemplo de Ranking Combinado

**Cenário:** Combinar RICE e WSJF para priorização final

| US | RICE Score | WSJF | Ranking Combinado | Justificativa |
|----|------------|------|-------------------|---------------|
| US-01 | 150 | 11.5 | 1º | WSJF alto compensa RICE baixo — desbloqueia outras USs |
| US-06 | 9600 | 5.0 | 2º | RICE muito alto, WSJF moderado |
| US-08 | 18 | 3.3 | 3º | Ambos baixos — complexa e com incerteza |

**Decisão:** US-01 tem prioridade máxima porque:
- WSJF alto (11.5): desbloqueia 3 outras USs (Risk Reduction = 8)
- É pequena (Job Size = 2): entrega valor rápido
- Confidence 100%: sem ambiguidade técnica

---

## 7. COMO PRIORIZAR — PASSO A PASSO

### 7.1 Fluxo de Priorização

1. **Filtrar com MoSCoW** — Classificar cada US em Must/Should/Could/Won't
2. **Calibrar estimativas** (opcional) — Ajustar Reach, Effort, Confidence, Time Criticality com contexto da equipe
3. **Calcular RICE** — Para todas as USs Must + Should + Could
4. **Calcular WSJF** — Para todas as USs Must + Should + Could
5. **Gerar ranking combinado** — Ordenar por RICE e WSJF, com desempate por WSJF
6. **Organizar em fases** — Ordenação topológica baseada em dependências
7. **Exportar resultado** — Gerar arquivos com priorização final

---

### 7.2 Critérios de Decisão

**Quando priorizar por RICE:**
- Comparar features com naturezas diferentes (ex: nova feature vs. melhoria de performance)
- Quando você tem dados de uso real (Reach) e estimativas de esforço (Effort)
- Para maximizar impacto por esforço

**Quando priorizar por WSJF:**
- Quando há dependências entre itens (Risk Reduction alto)
- Quando há prazos externos (Time Criticality alto)
- Para minimizar custo do atraso

**Recomendação:** Use **ambos em conjunto**. O RICE dá uma visão de eficiência (impacto/esforço), o WSJF dá uma visão de urgência (valor/tempo).

---

### 7.3 Flags de Risco

**Gerar flag quando:**
- Confidence < 70% — incerteza alta nas estimativas
- Dependência técnica não resolvida — ex: visualizador PDF pendente
- Effort potencialmente subestimado — ex: tela complexa sem validação técnica

**Formato do flag:**
```
[NOME DO ITEM]: [descrição do problema] → [o que é necessário antes de priorizar]
```

**Exemplo:**
```
US-08: Confidence 60% — visualizador PDF inline precisa validação técnica → Validar biblioteca/componente antes de iniciar
```

---

## 8. REFERÊNCIAS

- **RICE Score:** Framework criado pela Intercom
- **WSJF:** Framework do SAFe (Scaled Agile Framework)
- **MoSCoW:** Técnica de priorização com 4 categorias
- **Fibonacci:** Sequência usada em Planning Poker para estimativa relativa

---

*Documento genérico — válido para qualquer projeto de software*
*Baseado no template de Ahirton Lopes · PM AI Toolkit*
