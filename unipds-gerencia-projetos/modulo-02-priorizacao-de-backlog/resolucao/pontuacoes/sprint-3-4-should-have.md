# Sprints 3-4 — Should Have

**Data:** 29/09/2026
**Categoria:** Should (importante, mas com workaround)

---

## User Stories

### US-02 — Configurar pesos de entrevista no edital

- **RICE Score:** 100
- **WSJF:** 8.0
- **Story Points:** 3
- **Fase de Implementação:** 4
- **Critérios de Aceite:**
  - Configurar pesos quando edital terá entrevista
  - Sistema valida que soma é 100%
  - Exibe erro "A soma dos pesos deve ser 100%" se não somar
- **Dependências:** US-01
- **Justificativa:** Automatiza cálculo manual propenso a erros
- **Workaround:** Cálculo manual é viável

---

### US-03 — Cadastrar calendário de etapa por edital

- **RICE Score:** 80
- **WSJF:** 5.0
- **Story Points:** 5
- **Fase de Implementação:** 5
- **Critérios de Aceite:**
  - Cadastrar calendário por edital com datas de início, fim e publicação
  - Validação: data de publicação deve ser posterior à data de fim
  - Calendário reutilizável em vários editais
- **Dependências:** Nenhuma
- **Justificativa:** Centraliza datas para editais homogêneos
- **Workaround:** Datas podem ser gerenciadas fora do sistema inicialmente

---

### US-07 — Candidato altera documentos e pontuação dentro do prazo

- **RICE Score:** 10667
- **WSJF:** 4.7
- **Story Points:** 5
- **Fase de Implementação:** 3
- **Critérios de Aceite:**
  - Alterar documento e pontuação dentro do prazo
  - Sistema recalcula soma acumulada
  - Após encerramento do prazo: campos somente leitura
- **Dependências:** US-06
- **Justificativa:** Flexibilidade para o candidato corrigir informações
- **Workaround:** Pode ser feito manualmente (cancelar/reinscrever)

---

### US-09 — Analista pontua entrevista do candidato

- **RICE Score:** 80
- **WSJF:** 7.5
- **Story Points:** 3
- **Fase de Implementação:** 4
- **Critérios de Aceite:**
  - Edital com entrevista: analista pontua ambas as etapas
  - Sistema calcula pontuação final com pesos
  - Edital sem entrevista: campo não visível, final = documental
- **Dependências:** US-02, US-08
- **Justificativa:** Compõe a pontuação final
- **Workaround:** Condicional ao edital ter entrevista

---

### US-11 — Lista de classificação com edição manual de pontuação final

- **RICE Score:** 32
- **WSJF:** 3.0
- **Story Points:** 8
- **Fase de Implementação:** 4
- **Critérios de Aceite:**
  - Visualizar lista com pontuação final
  - Editar pontuação com justificativa obrigatória
  - Registro de auditoria (quem, quando, por quê)
- **Dependências:** US-08, US-09
- **Justificativa:** Permite correções antes da publicação
- **Workaround:** Correções podem ser feitas fora do sistema

---

## Resumo por Fase

### Fase 3 — Depende da Fase 2

| US | Título | RICE | WSJF | Story Points | Depende de |
|----|--------|------|------|--------------|------------|
| US-07 | Alterar documentos no prazo | 10667 | 4.7 | 5 | US-06 |
| **Subtotal** | | | | **5** |

### Fase 4 — Depende da Fase 3

| US | Título | RICE | WSJF | Story Points | Depende de |
|----|--------|------|------|--------------|------------|
| US-02 | Configurar pesos entrevista | 100 | 8.0 | 3 | US-01 |
| US-09 | Analista pontua entrevista | 80 | 7.5 | 3 | US-02, US-08 |
| US-11 | Lista de classificação | 32 | 3.0 | 8 | US-08, US-09 |
| **Subtotal** | | | | **14** |

### Fase 5 — Depende da Fase 4

| US | Título | RICE | WSJF | Story Points | Depende de |
|----|--------|------|------|--------------|------------|
| US-03 | Calendário por edital | 80 | 5.0 | 5 | Nenhuma |
| **Subtotal** | | | | **5** |

---

## Resumo Geral

- **Total de USs Should:** 5
- **Total de Story Points:** 24
- **Fases necessárias:** 3 (Fase 3, 4 e 5)
- **Ordem de implementação:** US-07 → US-02 → US-09 → US-11 → US-03

---

## Workarounds Disponíveis

| US | Workaround | Impacto |
|----|------------|---------|
| US-02 | Cálculo manual dos pesos | Propenso a erros, mas viável |
| US-03 | Datas gerenciadas fora do sistema | Perde integração, mas funcional |
| US-07 | Cancelar e reinscrever | Inconveniente para o candidato |
| US-09 | Não pontuar entrevista (se não houver) | Apenas editais sem entrevista |
| US-11 | Correções fora do sistema | Perde auditoria no sistema |

---

## Flags e Riscos

### Dependências Técnicas

- **US-09:** Depende de US-02 (pesos) e US-08 (análise documental)
- **US-11:** Depende de US-08 e US-09 — precisa que análise esteja completa

### Decisões Pendentes

- Nenhuma decisão pendente crítica para USs Should

---

*Gerado pela skill backlog-scorer-skill em 29/09/2026*
