# Sprint 0 — Resumo Consolidado

**Data:** 29/09/2026
**Projeto:** Análise Documental — Processos Seletivos Acadêmicos

---

## Referência — Siglas, Escalas e Fórmulas

### Siglas e Definições

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

### Escalas

**Escala Fibonacci (Story Points):** 0.5, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

**Impact (RICE):** 3=massivo, 2=significativo, 1=médio, 0.5=baixo, 0.25=mínimo

**Confidence (RICE):** 100%=certeza absoluta, 80%=alta confiança, 50%=intuição, <50%=especulação

**Time Criticality (WSJF):** 1-10 (9-10=deadline fixo, 7-8=prazo importante, 5-6=benefício imediato, 3-4=pode esperar, 1-2=sem urgência)

**Business Value (WSJF):** 1-10 (9-10=essencial para OKR, 7-8=muito importante, 5-6=importante, 3-4=moderado, 1-2=baixo)

**Risk Reduction (WSJF):** 1-10 (9-10=pré-requisito para múltiplas USs, 7-8=pré-requisito para algumas USs, 5-6=desbloqueia 1 US, 3-4=risco baixo, 1-2=sem impacto)

**Job Size (WSJF):** 1-10 (1=muito pequeno, 2-3=pequeno, 4-5=médio, 6-7=grande, 8-10=muito grande)

---

### Fórmulas

**RICE Score:**
```
RICE = (Reach × Impact × Confidence) / Effort
```

**Cost of Delay:**
```
CoD = Business Value + Time Criticality + Risk Reduction
```

**WSJF:**
```
WSJF = Cost of Delay / Job Size
```

---

### Conversão Story Points → Tempo

| Story Points | Effort (pm) | Tempo real |
|--------------|-------------|------------|
| 1-2 | 0.1-0.2 | 2-4 dias |
| 3 | 0.25 | 1 semana |
| 5 | 0.5 | 2 semanas |
| 8 | 1.0 | 1 mês |
| 13 | 2.0 | 2 meses |

---

### Níveis de Complexidade

| Tipo de Tarefa | Simples | Médio | Complexo |
|----------------|---------|-------|----------|
| **CRUDs / Cadastros** | 1-2 pts | 3-5 pts | 8 pts |
| **Telas de Processamento** | 2-3 pts | 5-8 pts | 13 pts |
| **Entrada de Dados** | 1-2 pts | 3-5 pts | 8 pts |
| **Listas e Relatórios** | 1-2 pts | 3-5 pts | 8 pts |
| **Portal / Autoatendimento** | 1-2 pts | 3-5 pts | 8 pts |

**Critérios:**
- **Simples:** 1-2 campos, validações básicas, sem integrações
- **Médio:** 3-5 campos, regras de negócio simples, vínculo a 1 entidade
- **Complexo:** 6+ campos, cálculos/dependências, visualizador de documentos, múltiplas integrações

---

## Ranking Final (RICE + WSJF)

**Ordenação:** Por categoria (Must → Should → Could) e dentro de cada categoria por RICE Score descendente.

| US | Título | Categoria | Fase | RICE Score | WSJF | Story Points |
|----|--------|-----------|------|------------|------|--------------|
| US-16 | Candidato visualiza status e pontuação no portal | Must | 4 | 16000 | 8.3 | 5 |
| US-06 | Candidato declara pontuação ao enviar documentos | Must | 2 | 9600 | 5.0 | 8 |
| US-01 | Cadastrar critério "Análise Documental" no edital | Must | 1 | 150 | 11.5 | 2 |
| US-05 | Configurar tipo de documento com pontuação | Must | 1 | 150 | 10.5 | 2 |
| US-10 | Analista desclassifica candidato | Must | 4 | 100 | 9.5 | 2 |
| US-13 | Perfil "Analista de Documento" | Must | 1 | 70 | 7.7 | 5 |
| US-08 | Analista pontua documentos do candidato | Must | 3 | 18 | 3.3 | 13 |
| US-07 | Candidato altera documentos e pontuação dentro do prazo | Should | 3 | 10667 | 4.7 | 5 |
| US-02 | Configurar pesos de entrevista no edital | Should | 4 | 100 | 8.0 | 3 |
| US-03 | Cadastrar calendário de etapa por edital | Should | 5 | 80 | 5.0 | 5 |
| US-09 | Analista pontua entrevista do candidato | Should | 4 | 80 | 7.5 | 3 |
| US-11 | Lista de classificação com edição manual | Should | 4 | 32 | 3.0 | 8 |
| US-14 | Candidato interpõe recurso pelo portal | Could | 5 | 6667 | 4.0 | 5 |
| US-04 | Cadastrar calendário de etapa por curso/oferta | Could | 5 | 40 | 2.7 | 5 |
| US-15 | Analista julga recurso | Could | 5 | 20 | 2.6 | 8 |
| US-12 | Exportar classificação em CSV e HTML | Could | 5 | 17 | 3.3 | 5 |

---

## Fases de Implementação

### Fase 1 — Sem Dependências (implementar primeiro)

| US | Título | RICE Score | WSJF | Categoria | Story Points |
|----|--------|------------|------|-----------|--------------|
| US-01 | Cadastrar critério "Análise Documental" no edital | 150 | 11.5 | Must | 2 |
| US-05 | Configurar tipo de documento com pontuação | 150 | 10.5 | Must | 2 |
| US-13 | Perfil "Analista de Documento" | 70 | 7.7 | Must | 5 |

**Subtotal:** 3 USs, 9 Story Points

### Fase 2 — Depende da Fase 1

| US | Título | RICE Score | WSJF | Categoria | Story Points | Depende de |
|----|--------|------------|------|-----------|--------------|------------|
| US-06 | Candidato declara pontuação ao enviar documentos | 9600 | 5.0 | Must | 8 | US-01, US-05 |

**Subtotal:** 1 US, 8 Story Points

### Fase 3 — Depende da Fase 2

| US | Título | RICE Score | WSJF | Categoria | Story Points | Depende de |
|----|--------|------------|------|-----------|--------------|------------|
| US-07 | Candidato altera documentos e pontuação dentro do prazo | 10667 | 4.7 | Should | 5 | US-06 |
| US-08 | Analista pontua documentos do candidato | 18 | 3.3 | Must | 13 | US-06, US-13 |

**Subtotal:** 2 USs, 18 Story Points

### Fase 4 — Depende da Fase 3

| US | Título | RICE Score | WSJF | Categoria | Story Points | Depende de |
|----|--------|------------|------|-----------|--------------|------------|
| US-16 | Candidato visualiza status e pontuação no portal | 16000 | 8.3 | Must | 5 | US-10, US-11 |
| US-02 | Configurar pesos de entrevista no edital | 100 | 8.0 | Should | 3 | US-01 |
| US-10 | Analista desclassifica candidato | 100 | 9.5 | Must | 2 | US-08 |
| US-09 | Analista pontua entrevista do candidato | 80 | 7.5 | Should | 3 | US-02, US-08 |
| US-11 | Lista de classificação com edição manual | 32 | 3.0 | Should | 8 | US-08, US-09 |

**Subtotal:** 5 USs, 21 Story Points

### Fase 5 — Depende da Fase 4

| US | Título | RICE Score | WSJF | Categoria | Story Points | Depende de |
|----|--------|------------|------|-----------|--------------|------------|
| US-14 | Candidato interpõe recurso pelo portal | 6667 | 4.0 | Could | 5 | US-03 |
| US-03 | Cadastrar calendário de etapa por edital | 80 | 5.0 | Should | 5 | Nenhuma |
| US-04 | Cadastrar calendário de etapa por curso/oferta | 40 | 2.7 | Could | 5 | Nenhuma |
| US-15 | Analista julga recurso | 20 | 2.6 | Could | 8 | US-14, US-08 |
| US-12 | Exportar classificação em CSV e HTML | 17 | 3.3 | Could | 5 | US-11 |

**Subtotal:** 5 USs, 28 Story Points

---

**Resumo de Fases:**
- Fase 1: 3 USs (9 Story Points)
- Fase 2: 1 US (8 Story Points)
- Fase 3: 2 USs (18 Story Points)
- Fase 4: 5 USs (21 Story Points)
- Fase 5: 5 USs (28 Story Points)
- **Total: 5 fases, 16 USs, 84 Story Points**

---

## Ordem de Implementação Recomendada

1. **Fase 1:** US-01, US-05, US-13 (implementar primeiro — sem dependências)
2. **Fase 2:** US-06 (depois que Fase 1 estiver pronta)
3. **Fase 3:** US-07, US-08 (depois que Fase 2 estiver pronta)
4. **Fase 4:** US-16, US-02, US-10, US-09, US-11 (depois que Fase 3 estiver pronta)
5. **Fase 5:** US-14, US-03, US-04, US-15, US-12 (depois que Fase 4 estiver pronta)

---

## Distribuição por Categoria MoSCoW

- **Must:** 7 USs (37 Story Points)
  - US-01, US-05, US-06, US-08, US-10, US-13, US-16
- **Should:** 5 USs (24 Story Points)
  - US-02, US-03, US-07, US-09, US-11
- **Could:** 4 USs (23 Story Points)
  - US-04, US-12, US-14, US-15

---

## Capacidade do Time

- **Velocidade:** 40 Story Points/sprint
- **Sprints necessárias:** 84 ÷ 40 = 2.1 sprints ≈ **3 sprints** (com buffer)
- **Duração total estimada:** 6 semanas (3 sprints de 2 semanas)

---

## Flags e Riscos

### Flags de Confidence Baixa (< 70%)

- **US-08:** Confidence 60% — visualizador PDF inline precisa validação técnica antes de iniciar
- **US-12:** Confidence 50% — formato de referência das convocações pendente de recebimento
- **US-14:** Confidence 50% — recurso de recurso não definido (pode haver múltiplos níveis)
- **US-15:** Confidence 50% — efeitos exatos do deferimento/indeferimento não definidos

### Flags de Dependências Técnicas

- **US-08:** Visualizador PDF inline — validar biblioteca/componente (pdf.js, react-pdf, etc.)
- **US-13:** Modelo de permissões — verificar se suporta vinculação granular por oferta
- **US-06, US-08, US-11:** Base ENEM existente — mapear o que pode ser reaproveitado

### Flags de Decisão Pendente

- **US-13:** Quem cadastra o perfil Analista? Administrador ou Gestão Local?
- **US-14:** Pode haver recurso de recurso?
- **US-15:** A pontuação da entrevista também pode ser alterada no deferimento?

---

## OKRs do Projeto

1. **Retirar a etapa de avaliação de documentos que é feita fora do sistema** — migrar processo manual para digital
2. **Dar transparência ao candidato do processo de avaliação e resultados** — portal do candidato com status e pontuação

---

## Restrições Conhecidas

- Visualizador PDF inline precisa validação técnica
- Modelo de permissões pode não suportar vinculação granular por oferta
- Base ENEM existente — reaproveitamento não documentado
- Formato de referência das convocações pendente de recebimento

---

*Gerado pela skill backlog-scorer-skill em 29/09/2026*
