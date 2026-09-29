# Sprint 5 — Could Have

**Data:** 29/09/2026
**Categoria:** Could (desejável se houver capacidade)

---

## User Stories

### US-04 — Cadastrar calendário de etapa por curso/oferta

- **RICE Score:** 40
- **WSJF:** 2.7
- **Story Points:** 5
- **Fase de Implementação:** 5
- **Critérios de Aceite:**
  - Cadastrar calendário com escopo "Por curso/oferta"
  - Cada oferta pode ter datas distintas
  - Mesma estrutura da US-03, com vínculo a oferta
- **Dependências:** Nenhuma
- **Justificativa:** Atende realidade de editais com cursos em campi diferentes
- **Workaround:** Pode começar com escopo por edital (US-03)

---

### US-12 — Exportar classificação em CSV e HTML

- **RICE Score:** 17
- **WSJF:** 3.3
- **Story Points:** 5
- **Fase de Implementação:** 5
- **Critérios de Aceite:**
  - Exportar CSV com: inscrição, nome, pontuações, status
  - Exportar HTML formatado para publicação no site
- **Dependências:** US-11
- **Justificativa:** Mantém processo existente de publicação
- **Workaround:** Pode ser feito manualmente
- **Flag:** Confidence 50% — formato de referência das convocações pendente

---

### US-14 — Candidato interpõe recurso pelo portal

- **RICE Score:** 6667
- **WSJF:** 4.0
- **Story Points:** 5
- **Fase de Implementação:** 5
- **Critérios de Aceite:**
  - Enviar recurso dentro do prazo com justificativa e PDF
  - Sistema registra recurso com data/hora
  - Status muda para "Recurso em análise"
  - Fora do prazo: opção não disponível
- **Dependências:** US-03 (calendário de recurso)
- **Justificativa:** Direito do candidato ao contraditório
- **Workaround:** Pode ser feito por e-mail/formulário externo
- **Flag:** Confidence 50% — recurso de recurso não definido

---

### US-15 — Analista julga recurso

- **RICE Score:** 20
- **WSJF:** 2.6
- **Story Points:** 8
- **Fase de Implementação:** 5
- **Critérios de Aceite:**
  - Visualizar documentos originais, pontuação anterior, justificativa do candidato e PDF de manifestação
  - Deferir: nova pontuação + justificativa, sistema recalcula
  - Indeferir: mantém pontuação + justificativa
  - Registro de auditoria (quem, quando, decisão)
- **Dependências:** US-14, US-08
- **Justificativa:** Centraliza informações para decisão
- **Workaround:** Complementa US-14
- **Flag:** Confidence 50% — efeitos exatos do deferimento/indeferimento não definidos

---

## Resumo por Fase

### Fase 5 — Depende da Fase 4

| US | Título | RICE | WSJF | Story Points | Depende de |
|----|--------|------|------|--------------|------------|
| US-14 | Candidato interpõe recurso | 6667 | 4.0 | 5 | US-03 |
| US-04 | Calendário por oferta | 40 | 2.7 | 5 | Nenhuma |
| US-15 | Analista julga recurso | 20 | 2.6 | 8 | US-14, US-08 |
| US-12 | Exportar CSV/HTML | 17 | 3.3 | 5 | US-11 |
| **Subtotal** | | | | **23** |

---

## Resumo Geral

- **Total de USs Could:** 4
- **Total de Story Points:** 23
- **Fases necessárias:** 1 (Fase 5)
- **Ordem de implementação:** US-14 → US-04 → US-15 → US-12

---

## Workarounds Disponíveis

| US | Workaround | Impacto |
|----|------------|---------|
| US-04 | Usar apenas calendário por edital | Perde flexibilidade por oferta |
| US-12 | Exportação manual | Perde automação, mas funcional |
| US-14 | Recurso por e-mail | Perde integração, mas viável |
| US-15 | Julgamento fora do sistema | Perde centralização, mas viável |

---

## Flags e Riscos

### Dependências Técnicas

- **US-14:** Depende de calendário de recurso (US-03)
- **US-15:** Depende de US-14 (recurso) e US-08 (análise)

### Decisões Pendentes

1. **Recurso de recurso** (US-14)
   - É possível o candidato interpor recurso contra a decisão do primeiro recurso?
   - Se sim, fluxo precisa prever múltiplos níveis

2. **Efeitos do deferimento/indeferimento** (US-15)
   - A pontuação da entrevista também pode ser alterada no deferimento?
   - No indeferimento, a pontuação permanece exatamente a mesma?
   - Há efeito colateral (mudança de posição na lista)?

3. **Formato de referência** (US-12)
   - Receber convocações publicadas como referência para modelar CSV/HTML
   - Sem referência, formato pode não atender necessidades de publicação

### Confidence Baixa

- **US-12:** Confidence 50% — formato pendente
- **US-14:** Confidence 50% — recurso de recurso não definido
- **US-15:** Confidence 50% — efeitos do deferimento não definidos

---

## Recomendação

**Implementar apenas se houver capacidade após Must e Should.**

Se o time não conseguir entregar todas as USs Could na sprint, priorizar:
1. **US-14** (RICE 6667) — direito do candidato ao contraditório
2. **US-04** (RICE 40) — flexibilidade por oferta
3. **US-15** (RICE 20) — julgamento centralizado
4. **US-12** (RICE 17) — exportação automática

---

*Gerado pela skill backlog-scorer-skill em 29/09/2026*
