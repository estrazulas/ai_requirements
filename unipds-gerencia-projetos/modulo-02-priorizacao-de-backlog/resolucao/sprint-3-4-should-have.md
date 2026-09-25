# MoSCoW — SHOULD HAVE

> Importante mas não vital → incluir no scoring

---

## User Stories Incluídas

| US | Título | Sprint Sugerida |
|----|--------|-----------------|
| US-02 | Configurar pesos de entrevista no edital | Sprint 3 |
| US-03 | Cadastrar calendário de etapa por edital | Sprint 3 |
| US-04 | Cadastrar calendário de etapa por curso/oferta | Sprint 3 |
| US-09 | Analista pontua entrevista do candidato | Sprint 4 |
| US-10 | Analista desclassifica candidato | Sprint 4 |
| US-11 | Lista de classificação com edição manual | Sprint 4 |
| US-16 | Candidato visualiza status e pontuação no portal | Sprint 4 |

---

## Tabela RICE

| Item | Reach | Impact | Confidence | Effort (pm) | RICE Score |
|------|-------|--------|------------|-------------|------------|
| US-02 — Pesos entrevista | 50 | 2 | 100% | 0.3 | 333.3 |
| US-03 — Calendário por edital | 50 | 2 | 100% | 0.5 | 200.0 |
| US-04 — Calendário por oferta | 50 | 2 | 100% | 0.5 | 200.0 |
| US-09 — Analista pontua entrevista | 30 | 2 | 100% | 0.5 | 120.0 |
| US-10 — Analista desclassifica | 30 | 2 | 100% | 0.3 | 200.0 |
| US-11 — Lista classificação editável | 10 | 3 | 100% | 1.0 | 30.0 |
| US-16 — Candidato visualiza status | 200 | 3 | 100% | 0.5 | 1200.0 |

---

## Tabela WSJF

| Item | BV | TC | RR | CoD | Job Size | WSJF |
|------|----|----|----|-----|----------|------|
| US-02 — Pesos entrevista | 7 | 6 | 5 | 18 | 1 | 18.0 |
| US-03 — Calendário por edital | 6 | 7 | 4 | 17 | 2 | 8.5 |
| US-04 — Calendário por oferta | 6 | 7 | 4 | 17 | 2 | 8.5 |
| US-09 — Analista pontua entrevista | 7 | 7 | 5 | 19 | 2 | 9.5 |
| US-10 — Analista desclassifica | 8 | 7 | 4 | 19 | 1 | 19.0 |
| US-11 — Lista classificação editável | 9 | 8 | 6 | 23 | 3 | 7.7 |
| US-16 — Candidato visualiza status | 10 | 9 | 7 | 26 | 2 | 13.0 |

---

## Ranking Combinado (Should Have)

| Posição | Item | RICE | WSJF | Justificativa |
|---------|------|------|------|---------------|
| 1 | **US-16 — Candidato visualiza status** | 1200.0 | 13.0 | Maior RICE absoluto. KR3 (transparência). Alto alcance, impacto massivo |
| 2 | **US-02 — Pesos entrevista** | 333.3 | 18.0 | Automatiza cálculo manual propenso a erros (KR1). WSJF alto |
| 3 | **US-10 — Analista desclassifica** | 200.0 | 19.0 | Essencial para fluxo de eliminação. WSJF mais alto |
| 4 | **US-03 — Calendário por edital** | 200.0 | 8.5 | Centraliza datas (KR1). Necessário para US-14, US-16 |
| 5 | **US-04 — Calendário por oferta** | 200.0 | 8.5 | Mesma importância de US-03, mas para editais heterogêneos |
| 6 | **US-09 — Analista pontua entrevista** | 120.0 | 9.5 | Complemento de US-08 para editais com entrevista |
| 7 | **US-11 — Lista classificação editável** | 30.0 | 7.7 | Permite correções antes de exportar |

---

## Justificativas

**US-16 — Candidato visualiza status**
- **Impact 3 (massivo):** atende KR3 diretamente (transparência). Todos os candidatos visualizam resultado. Elimina necessidade de consultar setor solicitante.
- **Confidence 100%:** requisito claro, sem ambiguidade técnica.
- **Business Value 10:** contribuição máxima para KR3 (100% candidatos visualizam em 24h).
- **Time Criticality 9:** prazo externo (edital) exige que resultados sejam visíveis rapidamente.

**US-02 — Pesos entrevista**
- **Impact 2 (significativo):** automatiza cálculo manual propenso a erros (KR1). Importante para editais com entrevista.
- **Confidence 100%:** campos condicionais + validação de soma 100%, sem risco técnico.
- **Business Value 7:** elimina etapa manual de cálculo ponderado.
- **Risk Reduction 5:** desbloqueia US-09 (cálculo com pesos).

**US-03 — Calendário por edital**
- **Impact 2 (significativo):** centraliza datas (KR1). Necessário para controle de prazos de análise, recurso e publicação.
- **Confidence 100%:** CRUD com validação de datas, sem risco técnico.
- **Business Value 6:** necessário para KR1 (eliminar etapas manuais de controle de prazo).
- **Risk Reduction 4:** desbloqueia US-14 (recurso) e US-16 (visualização respeitando datas).

**US-04 — Calendário por oferta**
- **Impact 2 (significativo):** mesma importância de US-03, mas para editais com cursos em campuses diferentes.
- **Confidence 100%:** mesma estrutura de US-03, com vínculo a oferta.
- **Business Value 6:** atende realidade de editais heterogêneos.
- **Risk Reduction 4:** desbloqueia US-14 e US-16 para ofertas específicas.

**US-09 — Analista pontua entrevista**
- **Impact 2 (significativo):** compõe a pontuação final para editais com entrevista.
- **Confidence 100%:** campo condicional + cálculo ponderado, sem risco técnico.
- **Business Value 7:** necessário para editais com entrevista (complemento de US-08).
- **Risk Reduction 5:** desbloqueia cálculo de pontuação final com pesos.

**US-10 — Analista desclassifica**
- **Impact 2 (significativo):** atende requisito de eliminação com justificativa.
- **Confidence 100%:** campo de motivo + confirmação, sem risco técnico.
- **Business Value 8:** necessário para fluxo de eliminação (auditabilidade).
- **Risk Reduction 4:** desbloqueia US-16 (status "Eliminado" visível no portal).

**US-11 — Lista de classificação editável**
- **Impact 3 (massivo):** permite correções pontuais antes da publicação com auditoria completa.
- **Confidence 100%:** lista tabular + edição inline + auditoria, sem risco técnico.
- **Business Value 9:** necessário para correções antes de exportar (US-12).
- **Risk Reduction 6:** desbloqueia US-12 (exportação) e garante auditabilidade.

---

## Flags

**US-03 e US-04 — Calendários:** não há flags técnicas, mas dependem de decisão sobre escopo (por edital vs. por oferta). Recomenda-se implementar ambas para cobrir todos os cenários.

**US-16 — Candidato visualiza status:** sistema NÃO publica listas, apenas exibe status individual. Publicação externa no site institucional permanece com setor solicitante → confirmar se isso atende KR3 (transparência).

**US-11 — Lista classificação editável:** classificação NÃO é automática — botões manuais para processar. Auditoria completa (quem, quando, por quê) é obrigatória.

---

## Dependências Internas

```
US-02 (pesos) → US-09 (pontua entrevista)
US-03/US-04 (calendários) → US-16 (visualiza status)
US-08 (analista pontua - Must) → US-09 (pontua entrevista)
US-08 (analista pontua - Must) → US-10 (desclassifica)
US-08 + US-09 → US-11 (lista editável)
US-10 + US-11 → US-16 (visualiza status)
```

**Ordem de desenvolvimento recomendada:**
1. US-02 + US-03 + US-04 (paralelo, sem dependências entre si)
2. US-09 + US-10 (paralelo, dependem de US-08 do Must)
3. US-11 (depende de US-08 e US-09)
4. US-16 (depende de US-10 e US-11)

---

*Data: 25/09/2026*
*OKR: Eliminar processo manual de análise documental por planilhas*
