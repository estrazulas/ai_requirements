# Sprints 1-2 — Must Have

**Data:** 25/09/2026
**Categoria:** Must (essencial para MVP)

## User Stories

### US-01 — Critério AD no edital
- **RICE Score:** 150.00
- **WSJF:** 11.00
- **Cost of Delay:** 22
- **Story Points:** 3
- **Effort:** 0.20 pm
- **Sprint:** 1
- **Prioridade:** MÉDIA
- **Critérios de Aceite:**
  - Selecionar "Análise Documental" no campo critério de seleção
  - Campo "Pontuação máxima total" torna-se obrigatório
  - Editar edital existente com alerta sobre dados importados
- **Dependências:** Nenhuma
- **Flags:** Nenhuma

---

### US-05 — Tipo de documento com pontuação
- **RICE Score:** 200.00
- **WSJF:** 21.00
- **Cost of Delay:** 21
- **Story Points:** 2
- **Effort:** 0.15 pm
- **Sprint:** 1
- **Prioridade:** MÉDIA
- **Critérios de Aceite:**
  - Marcar "Requer pontuação?" e definir teto de pontos
  - Tipo sem pontuação não exibe campo no formulário
  - Teto global sobrescrito por tipo de documento
- **Dependências:** Nenhuma
- **Flags:** Nenhuma

---

### US-06 — Candidato declara pontuação
- **RICE Score:** 5333.33
- **WSJF:** 5.00
- **Cost of Delay:** 20
- **Story Points:** 5
- **Effort:** 0.60 pm
- **Sprint:** 1
- **Prioridade:** CRÍTICA
- **Critérios de Aceite:**
  - Declarar pontuação dentro do teto do edital
  - Sistema exibe soma acumulada em tempo real
  - Bloqueia se soma ultrapassa teto do edital
  - Bloqueia se pontuação ultrapassa teto do tipo de documento
- **Dependências:** US-01, US-05
- **Flags:** Nenhuma

---

### US-08 — Analista pontua documentos
- **RICE Score:** 2400.00
- **WSJF:** 3.29
- **Cost of Delay:** 23
- **Story Points:** 8
- **Effort:** 1.50 pm
- **Sprint:** 2
- **Prioridade:** ALTA
- **Critérios de Aceite:**
  - Atribuir pontuação documental com justificativa obrigatória
  - Visualizar documentos do candidato com pontuação declarada
  - Registro de auditoria (quem, quando)
- **Dependências:** US-06, US-13
- **Flags:**
  - ⚠️ Confidence 60% — visualizador PDF inline não validado tecnicamente
  - Time precisa validar biblioteca (pdf.js, react-pdf) antes de iniciar

---

### US-13 — Perfil Analista de Documento
- **RICE Score:** 52.50
- **WSJF:** 7.00
- **Cost of Delay:** 21
- **Story Points:** 3
- **Effort:** 0.40 pm
- **Sprint:** 1
- **Prioridade:** BAIXA
- **Critérios de Aceite:**
  - Cadastrar usuário com perfil "Analista de Documento" vinculado a oferta
  - Analista vê apenas candidatos da oferta vinculada
  - Analista não acessa menu administrativo
- **Dependências:** Nenhuma
- **Flags:**
  - ⚠️ Confidence 70% — modelo de permissões pode não suportar vinculação por oferta
  - Time precisa verificar schema antes de iniciar
  - ⚠️ Pergunta pendente: quem cadastra o analista? (pergunta 5)

---

## Resumo Must Have

| US | Título | RICE | WSJF | SP | Sprint | Prioridade |
|----|--------|------|------|----|----|------------|
| US-06 | Candidato declara pontuação | 5333.33 | 5.00 | 5 | 1 | CRÍTICA |
| US-08 | Analista pontua documentos | 2400.00 | 3.29 | 8 | 2 | ALTA |
| US-05 | Tipo de documento com pontuação | 200.00 | 21.00 | 2 | 1 | MÉDIA |
| US-01 | Critério AD no edital | 150.00 | 11.00 | 3 | 1 | MÉDIA |
| US-13 | Perfil Analista de Documento | 52.50 | 7.00 | 3 | 1 | BAIXA |

**Total Must Have:** 5 USs, 21 story points, 2.85 pm

---

*Gerado pela skill backlog-scorer-skill em 25/09/2026*
