# MoSCoW — COULD HAVE

> Desejável → incluir apenas se sobrar capacidade

---

## User Stories Incluídas

| US | Título | Sprint Sugerida |
|----|--------|-----------------|
| US-07 | Candidato altera documentos e pontuação dentro do prazo | Sprint 5 |
| US-12 | Exportar classificação em CSV e HTML | Sprint 5 |
| US-14 | Candidato interpõe recurso pelo portal | Sprint 5 |
| US-15 | Analista julga recurso | Sprint 5 |

---

## Tabela RICE

| Item | Reach | Impact | Confidence | Effort (pm) | RICE Score |
|------|-------|--------|------------|-------------|------------|
| US-07 — Candidato altera dentro prazo | 200 | 1 | 100% | 0.5 | 400.0 |
| US-12 — Exportar CSV/HTML | 10 | 2 | 80% | 0.5 | 32.0 |
| US-14 — Candidato interpõe recurso | 200 | 2 | 100% | 0.5 | 800.0 |
| US-15 — Analista julga recurso | 30 | 2 | 80% | 1.0 | 48.0 |

---

## Tabela WSJF

| Item | BV | TC | RR | CoD | Job Size | WSJF |
|------|----|----|----|-----|----------|------|
| US-07 — Candidato altera dentro prazo | 5 | 6 | 3 | 14 | 2 | 7.0 |
| US-12 — Exportar CSV/HTML | 8 | 9 | 3 | 20 | 2 | 10.0 |
| US-14 — Candidato interpõe recurso | 8 | 8 | 5 | 21 | 2 | 10.5 |
| US-15 — Analista julga recurso | 8 | 8 | 6 | 22 | 3 | 7.3 |

---

## Ranking Combinado (Could Have)

| Posição | Item | RICE | WSJF | Justificativa |
|---------|------|------|------|---------------|
| 1 | **US-14 — Candidato interpõe recurso** | 800.0 | 10.5 | Alto RICE (direito ao contraditório, KR3). WSJF alto |
| 2 | **US-07 — Candidato altera dentro prazo** | 400.0 | 7.0 | Alto RICE (flexibilidade para candidato). Complemento de US-06 |
| 3 | **US-15 — Analista julga recurso** | 48.0 | 7.3 | Complemento de US-14. Effort moderado |
| 4 | **US-12 — Exportar CSV/HTML** | 32.0 | 10.0 | Elimina geração manual de listas (KR1). WSJF alto mas RICE baixo |

---

## Justificativas

**US-14 — Candidato interpõe recurso**
- **Impact 2 (significativo):** direito ao contraditório, essencial para processo justo. Complementa US-16 (transparência).
- **Confidence 100%:** requisito claro, mas depende de calendário de recurso (US-03/US-04).
- **Business Value 8:** necessário para direito ao contraditório (compliance).
- **Time Criticality 8:** prazos de recurso são curtos e definidos em edital.
- **Risk Reduction 5:** desbloqueia US-15 (julgamento de recurso).

**US-07 — Candidato altera dentro prazo**
- **Impact 1 (médio):** flexibilidade para candidato corrigir informações antes do encerramento.
- **Confidence 100%:** controle de edição baseado em data, sem risco técnico.
- **Business Value 5:** melhora UX mas não é vital (candidato pode fazer nova inscrição se necessário).
- **Time Criticality 6:** precisa estar pronto antes do prazo de inscrição.
- **Risk Reduction 3:** complemento de US-06, não desbloqueia nada crítico.

**US-15 — Analista julga recurso**
- **Impact 2 (significativo):** centraliza informações para decisão de recurso.
- **Confidence 80%:** requisito claro, mas efeitos exatos do deferimento/indeferimento não definidos (pergunta 8).
- **Business Value 8:** necessário para fluxo de recurso (complemento de US-14).
- **Time Criticality 8:** prazos de julgamento são curtos e definidos em edital.
- **Risk Reduction 6:** desbloqueia recálculo de pontuação após recurso.

**US-12 — Exportar CSV/HTML**
- **Impact 2 (significativo):** elimina geração manual de listas (KR1). Mantém processo existente de publicação.
- **Confidence 80%:** requisito claro, mas formato depende de referência das convocações publicadas (pergunta 4).
- **Business Value 8:** necessário para publicação no site institucional.
- **Time Criticality 9:** prazo externo (edital) exige publicação rápida.
- **Risk Reduction 3:** não desbloqueia nada crítico (publicação pode ser feita manualmente se necessário).

---

## Flags

**US-14 — Candidato interpõe recurso:** pode haver recurso de recurso? (pergunta 7) → stakeholder precisa decidir. Se sim, fluxo precisa prever múltiplos níveis.

**US-15 — Analista julga recurso:** efeitos exatos do deferimento/indeferimento não definidos (pergunta 8) → stakeholder precisa definir se pontuação de entrevista também pode ser alterada, se há mudança de posição na lista, etc.

**US-12 — Exportar CSV/HTML:** formato depende de referência das convocações publicadas (pergunta 4) → setor solicitante precisa fornecer exemplos das convocações atuais para modelar CSV/HTML.

**US-07 — Candidato altera dentro prazo:** não há flags técnicas, mas depende de US-06 (Must) estar pronta.

---

## Dependências Internas

```
US-06 (declara pontuação - Must) → US-07 (altera dentro prazo)
US-03/US-04 (calendários - Should) → US-14 (interpõe recurso)
US-14 (interpõe recurso) → US-15 (julga recurso)
US-11 (lista editável - Should) → US-12 (exporta CSV/HTML)
US-08 + US-15 → US-12 (exporta CSV/HTML)
```

**Ordem de desenvolvimento recomendada:**
1. US-07 (depende de US-06 do Must)
2. US-14 (depende de US-03/US-04 do Should)
3. US-15 (depende de US-14)
4. US-12 (depende de US-11 do Should)

---

## Recomendação

Estas USs devem ser incluídas apenas se houver capacidade após a entrega do Must + Should. Se houver restrição de tempo/orçamento, priorize:

1. **US-14 + US-15** (recurso) — direito ao contraditório é importante para compliance
2. **US-07** (alteração dentro do prazo) — melhora UX do candidato
3. **US-12** (exportação) — pode ser feito manualmente se necessário

---

*Data: 25/09/2026*
*OKR: Eliminar processo manual de análise documental por planilhas*
