# Sprints 1-2 — Must Have

**Data:** 29/09/2026
**Categoria:** Must (essencial para MVP)

---

## User Stories

### US-01 — Cadastrar critério "Análise Documental" no edital

- **RICE Score:** 150
- **WSJF:** 11.5
- **Story Points:** 2
- **Fase de Implementação:** 1
- **Critérios de Aceite:**
  - Selecionar "Análise Documental" no campo critério de seleção
  - Campo "Pontuação máxima total" torna-se obrigatório
  - Editar edital existente com alerta sobre desconsideração de dados importados
- **Dependências:** Nenhuma
- **Justificativa:** Habilita o fluxo principal de análise documental

---

### US-05 — Configurar tipo de documento com pontuação

- **RICE Score:** 150
- **WSJF:** 10.5
- **Story Points:** 2
- **Fase de Implementação:** 1
- **Critérios de Aceite:**
  - Marcar "Requer pontuação?" e definir teto de pontos
  - Tipo sem pontuação não exibe campo no formulário
- **Dependências:** Nenhuma
- **Justificativa:** Essencial para diferenciação de documentos pontuáveis

---

### US-06 — Candidato declara pontuação ao enviar documentos

- **RICE Score:** 9600
- **WSJF:** 5.0
- **Story Points:** 8
- **Fase de Implementação:** 2
- **Critérios de Aceite:**
  - Declarar pontuação dentro do teto
  - Sistema exibe "Soma atual: X de Y"
  - Bloqueia se soma ultrapassa teto do edital
  - Bloqueia se pontuação ultrapassa teto do tipo de documento
- **Dependências:** US-01, US-05
- **Justificativa:** Coração do fluxo de inscrição com pontuação
- **Flag:** Confidence 80% — base ENEM não mapeada

---

### US-08 — Analista pontua documentos do candidato

- **RICE Score:** 18
- **WSJF:** 3.3
- **Story Points:** 13
- **Fase de Implementação:** 3
- **Critérios de Aceite:**
  - Atribuir pontuação documental com justificativa obrigatória
  - Visualizar documentos do candidato com visualizador PDF
  - Registro de auditoria (quem, quando)
- **Dependências:** US-06, US-13
- **Justificativa:** Coração do fluxo de análise documental
- **Flag:** Confidence 60% — visualizador PDF inline precisa validação técnica

---

### US-10 — Analista desclassifica candidato

- **RICE Score:** 100
- **WSJF:** 9.5
- **Story Points:** 2
- **Fase de Implementação:** 4
- **Critérios de Aceite:**
  - Desclassificar com motivo obrigatório
  - Confirmação antes de eliminar
  - Status "Eliminado" visível no portal
- **Dependências:** US-08
- **Justificativa:** Essencial para fluxo de eliminação

---

### US-13 — Perfil "Analista de Documento"

- **RICE Score:** 70
- **WSJF:** 7.7
- **Story Points:** 5
- **Fase de Implementação:** 1
- **Critérios de Aceite:**
  - Cadastrar usuário com perfil "Analista de Documento"
  - Vincular a oferta específica
  - Analista vê apenas candidatos da oferta vinculada
  - Analista não acessa menu administrativo
- **Dependências:** Nenhuma
- **Justificativa:** Essencial para segurança e separação de responsabilidades
- **Flag:** Confidence 70% — modelo de permissões pode não suportar vinculação granular

---

### US-16 — Candidato visualiza status e pontuação no portal

- **RICE Score:** 16000
- **WSJF:** 8.3
- **Story Points:** 5
- **Fase de Implementação:** 4
- **Critérios de Aceite:**
  - Antes da data de publicação: "Aguardando análise documental"
  - Após publicação — classificado: pontuação final e "Classificado em Xº lugar"
  - Após publicação — eliminado: status "Eliminado" com motivo
- **Dependências:** US-10, US-11
- **Justificativa:** Essencial para OKR de transparência

---

## Resumo por Fase

### Fase 1 — Sem Dependências

| US | Título | RICE | WSJF | Story Points |
|----|--------|------|------|--------------|
| US-01 | Cadastrar critério AD | 150 | 11.5 | 2 |
| US-05 | Configurar tipo documento | 150 | 10.5 | 2 |
| US-13 | Perfil Analista | 70 | 7.7 | 5 |
| **Subtotal** | | | | **9** |

### Fase 2 — Depende da Fase 1

| US | Título | RICE | WSJF | Story Points | Depende de |
|----|--------|------|------|--------------|------------|
| US-06 | Candidato declara pontuação | 9600 | 5.0 | 8 | US-01, US-05 |
| **Subtotal** | | | | **8** |

### Fase 3 — Depende da Fase 2

| US | Título | RICE | WSJF | Story Points | Depende de |
|----|--------|------|------|--------------|------------|
| US-08 | Analista pontua documentos | 18 | 3.3 | 13 | US-06, US-13 |
| **Subtotal** | | | | **13** |

### Fase 4 — Depende da Fase 3

| US | Título | RICE | WSJF | Story Points | Depende de |
|----|--------|------|------|--------------|------------|
| US-16 | Candidato visualiza status | 16000 | 8.3 | 5 | US-10, US-11 |
| US-10 | Desclassificar candidato | 100 | 9.5 | 2 | US-08 |
| **Subtotal** | | | | **7** |

---

## Resumo Geral

- **Total de USs Must:** 7
- **Total de Story Points:** 37
- **Fases necessárias:** 4
- **Ordem de implementação:** US-01 → US-05 → US-13 → US-06 → US-08 → US-10 → US-16

---

## Flags e Riscos

### Dependências Técnicas Pendentes

1. **Visualizador PDF inline** (US-08)
   - Validar biblioteca/componente (pdf.js, react-pdf, etc.)
   - Viabilidade técnica não confirmada

2. **Modelo de permissões** (US-13)
   - Verificar se suporta vinculação granular por oferta
   - Se não suportar, implementação pode ser mais complexa

3. **Base ENEM existente** (US-06, US-08)
   - Mapear o que pode ser reaproveitado
   - Reaproveitamento não documentado

### Decisões Pendentes

1. **Quem cadastra o perfil Analista?** (US-13)
   - Administrador ou Gestão Local?
   - Impacta modelo de permissões

---

*Gerado pela skill backlog-scorer-skill em 29/09/2026*
