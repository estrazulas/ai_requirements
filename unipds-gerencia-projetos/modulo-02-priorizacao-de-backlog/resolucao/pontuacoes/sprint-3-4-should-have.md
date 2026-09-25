# Sprints 3-4 — Should Have

**Data:** 25/09/2026
**Categoria:** Should (importante, mas com workaround)

## User Stories

### US-10 — Analista desclassifica candidato
- **RICE Score:** 13333.33
- **WSJF:** 15.00
- **Cost of Delay:** 15
- **Story Points:** 2
- **Effort:** 0.15 pm
- **Sprint:** 1
- **Prioridade:** CRÍTICA
- **Critérios de Aceite:**
  - Desclassificar candidato com motivo obrigatório
  - Confirmação antes de eliminar
  - Status "Eliminado" com motivo registrado
- **Dependências:** US-08
- **Flags:** Nenhuma

---

### US-14 — Candidato interpõe recurso
- **RICE Score:** 10666.67
- **WSJF:** 9.50
- **Cost of Delay:** 19
- **Story Points:** 3
- **Effort:** 0.30 pm
- **Sprint:** 1
- **Prioridade:** CRÍTICA
- **Critérios de Aceite:**
  - Enviar recurso dentro do prazo com justificativa e PDF
  - Status muda para "Recurso em análise"
  - Bloqueia recurso fora do prazo
- **Dependências:** Calendário de recurso (US-03/US-04)
- **Flags:**
  - ⚠️ Pergunta pendente: pode haver recurso de recurso? (pergunta 7)

---

### US-16 — Candidato visualiza status no portal
- **RICE Score:** 10666.67
- **WSJF:** 9.50
- **Cost of Delay:** 19
- **Story Points:** 3
- **Effort:** 0.30 pm
- **Sprint:** 1
- **Prioridade:** CRÍTICA
- **Critérios de Aceite:**
  - Visualizar "Aguardando análise" antes da data de publicação
  - Visualizar pontuação final e status após publicação
  - Visualizar motivo de eliminação
- **Dependências:** US-10, US-11, US-15
- **Flags:** Nenhuma

---

### US-15 — Analista julga recurso
- **RICE Score:** 4000.00
- **WSJF:** 3.80
- **Cost of Delay:** 19
- **Story Points:** 5
- **Effort:** 0.70 pm
- **Sprint:** 2
- **Prioridade:** ALTA
- **Critérios de Aceite:**
  - Visualizar documentos originais, recurso e decisão em tela única
  - Deferir com nova pontuação e recálculo
  - Indeferir mantendo pontuação anterior
  - Registro de auditoria completo
- **Dependências:** US-14, US-08
- **Flags:**
  - ⚠️ Confidence 70% — efeitos exatos do deferimento/indeferimento pendentes (pergunta 8)

---

### US-02 — Pesos de entrevista
- **RICE Score:** 66.67
- **WSJF:** 13.00
- **Cost of Delay:** 13
- **Story Points:** 2
- **Effort:** 0.15 pm
- **Sprint:** 3
- **Prioridade:** BAIXA
- **Critérios de Aceite:**
  - Configurar pesos quando edital terá entrevista
  - Validação de soma = 100%
  - Erro se pesos não somam 100%
- **Dependências:** US-01
- **Flags:** Nenhuma

---

### US-03 — Calendário por edital
- **RICE Score:** 50.00
- **WSJF:** 6.50
- **Cost of Delay:** 13
- **Story Points:** 3
- **Effort:** 0.20 pm
- **Sprint:** 3
- **Prioridade:** BAIXA
- **Critérios de Aceite:**
  - Cadastrar calendário com tipo, escopo "Por edital", datas
  - Validação: data de publicação posterior à data de fim
  - Calendário reutilizável em vários editais
- **Dependências:** Nenhuma
- **Flags:** Nenhuma

---

### US-04 — Calendário por oferta
- **RICE Score:** 50.00
- **WSJF:** 6.50
- **Cost of Delay:** 13
- **Story Points:** 3
- **Effort:** 0.20 pm
- **Sprint:** 3
- **Prioridade:** BAIXA
- **Critérios de Aceite:**
  - Cadastrar calendário com escopo "Por curso/oferta"
  - Cada oferta possui calendário independente
- **Dependências:** Nenhuma
- **Flags:** Nenhuma

---

### US-09 — Analista pontua entrevista
- **RICE Score:** 50.00
- **WSJF:** 6.50
- **Cost of Delay:** 13
- **Story Points:** 3
- **Effort:** 0.20 pm
- **Sprint:** 3
- **Prioridade:** BAIXA
- **Critérios de Aceite:**
  - Edital com entrevista: pontua ambas as etapas
  - Edital sem entrevista: campo não visível
  - Cálculo automático com pesos do edital
- **Dependências:** US-02, US-08
- **Flags:** Nenhuma

---

### US-11 — Lista de classificação editável
- **RICE Score:** 26.67
- **WSJF:** 4.25
- **Cost of Delay:** 17
- **Story Points:** 5
- **Effort:** 0.60 pm
- **Sprint:** 3
- **Prioridade:** BAIXA
- **Critérios de Aceite:**
  - Visualizar lista com pontuação final
  - Editar pontuação com justificativa obrigatória
  - Registro de auditoria (quem, quando, por quê)
- **Dependências:** US-08, US-09
- **Flags:** Nenhuma

---

## Resumo Should Have

| US | Título | RICE | WSJF | SP | Sprint | Prioridade |
|----|--------|------|------|----|----|------------|
| US-10 | Analista desclassifica candidato | 13333.33 | 15.00 | 2 | 1 | CRÍTICA |
| US-14 | Candidato interpõe recurso | 10666.67 | 9.50 | 3 | 1 | CRÍTICA |
| US-16 | Candidato visualiza status no portal | 10666.67 | 9.50 | 3 | 1 | CRÍTICA |
| US-15 | Analista julga recurso | 4000.00 | 3.80 | 5 | 2 | ALTA |
| US-02 | Pesos de entrevista | 66.67 | 13.00 | 2 | 3 | BAIXA |
| US-03 | Calendário por edital | 50.00 | 6.50 | 3 | 3 | BAIXA |
| US-04 | Calendário por oferta | 50.00 | 6.50 | 3 | 3 | BAIXA |
| US-09 | Analista pontua entrevista | 50.00 | 6.50 | 3 | 3 | BAIXA |
| US-11 | Lista de classificação editável | 26.67 | 4.25 | 5 | 3 | BAIXA |

**Total Should Have:** 9 USs, 29 story points, 2.90 pm

---

*Gerado pela skill backlog-scorer-skill em 25/09/2026*
