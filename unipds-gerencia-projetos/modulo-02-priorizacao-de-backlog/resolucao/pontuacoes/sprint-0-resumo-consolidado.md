# Sprint 0 — Resumo Consolidado

**Data:** 25/09/2026
**Projeto:** Análise Documental — Processos Seletivos Acadêmicos

## OKR do Projeto

**Objetivo:** Eliminar a análise documental por planilhas e garantir transparência total ao candidato sobre o processo de avaliação.

**Key Results:**
- KR1: 100% das análises documentais realizadas dentro do sistema (zero planilhas)
- KR2: Candidato acompanha pontuação, status e recurso em tempo real pelo portal

## Ranking Final (RICE + WSJF)

| # | US | Título | Categoria | RICE | WSJF | CoD | Prioridade | Sprint |
|---|----|--------|-----------|------|------|-----|------------|--------|
| 1 | US-10 | Analista desclassifica candidato | Should | 13333.33 | 15.00 | 15 | CRÍTICA | 1 |
| 2 | US-14 | Candidato interpõe recurso | Should | 10666.67 | 9.50 | 19 | CRÍTICA | 1 |
| 3 | US-16 | Candidato visualiza status no portal | Should | 10666.67 | 9.50 | 19 | CRÍTICA | 1 |
| 4 | US-06 | Candidato declara pontuação | Must | 5333.33 | 5.00 | 20 | CRÍTICA | 1 |
| 5 | US-07 | Candidato altera documentos no prazo | Could | 5333.33 | 5.50 | 11 | ALTA | 2 |
| 6 | US-15 | Analista julga recurso | Should | 4000.00 | 3.80 | 19 | ALTA | 2 |
| 7 | US-08 | Analista pontua documentos | Must | 2400.00 | 3.29 | 23 | ALTA | 2 |
| 8 | US-05 | Tipo de documento com pontuação | Must | 200.00 | 21.00 | 21 | MÉDIA | 1 |
| 9 | US-01 | Critério AD no edital | Must | 150.00 | 11.00 | 22 | MÉDIA | 1 |
| 10 | US-02 | Pesos de entrevista | Should | 66.67 | 13.00 | 13 | BAIXA | 3 |
| 11 | US-13 | Perfil Analista de Documento | Must | 52.50 | 7.00 | 21 | BAIXA | 1 |
| 12 | US-03 | Calendário por edital | Should | 50.00 | 6.50 | 13 | BAIXA | 3 |
| 13 | US-04 | Calendário por oferta | Should | 50.00 | 6.50 | 13 | BAIXA | 3 |
| 14 | US-09 | Analista pontua entrevista | Should | 50.00 | 6.50 | 13 | BAIXA | 3 |
| 15 | US-11 | Lista de classificação editável | Should | 26.67 | 4.25 | 17 | BAIXA | 3 |
| 16 | US-12 | Exportar classificação CSV e HTML | Could | 20.00 | 5.50 | 11 | BAIXA | 4 |

## Distribuição por Categoria MoSCoW

- **Must:** 5 USs (26 story points)
  - US-01, US-05, US-06, US-08, US-13
- **Should:** 9 USs (30 story points)
  - US-02, US-03, US-04, US-09, US-10, US-11, US-14, US-15, US-16
- **Could:** 2 USs (6 story points)
  - US-07, US-12

## Capacidade do Time

- **Velocidade:** 120 story points/sprint (60 pts/semana)
- **Capacidade estimada:** ~4.0 pm por sprint
- **Esforço total ajustado:** 7.4 pm
- **Sprints necessárias:** ~2 sprints para Must + Should

## Flags e Riscos

### Flags de Confidence Baixa

- **US-08 — Analista pontua documentos:** Confidence 60% — visualizador PDF inline não validado tecnicamente → time precisa validar biblioteca (pdf.js, react-pdf) antes de iniciar.

- **US-13 — Perfil Analista de Documento:** Confidence 70% — modelo de permissões atual pode não suportar vinculação granular por oferta → time precisa verificar schema antes de iniciar.

- **US-15 — Analista julga recurso:** Confidence 70% — efeitos exatos do deferimento/indeferimento pendentes (pergunta 8) → stakeholder precisa decidir antes de iniciar.

- **US-12 — Exportar classificação:** Confidence 60% — formato de referência das convocações pendente (pergunta 4) → setor solicitante precisa fornecer exemplos.

### Dependências Críticas

- **US-08 depende de US-13:** US-13 está rankeada abaixo de US-08 no RICE, mas deve ser desenvolvida antes ou em paralelo.

### Perguntas Pendentes (do documento de requisitos)

1. Critérios para listas intermediárias de convocação para entrevista
2. Nivelamento — escopo e funcionamento
3. Critério de desempate
4. Referência de relatórios de convocação (impacta US-12)
5. Quem cadastra o perfil "Analista de Documento"?
6. Notificação por e-mail — confirma que fica fora desta demanda?
7. Recurso de recurso — é possível?
8. Efeitos do deferimento e indeferimento (impacta US-15)
9. Formato das notificações de recurso
10. Múltiplos avaliadores por candidato
11. Local de definição de horários e instruções de convocação
12. Quem cadastra os avaliadores?
13. Ausências nas convocações

## Recomendações de Execução

### Sprint 1 — Fundamentos e Transparência
Focar em USs que habilitam o fluxo básico e transparência ao candidato:
- US-01 (critério AD) — habilita o fluxo
- US-05 (tipo de documento) — base de dados
- US-06 (declarar pontuação) — entrada do candidato
- US-13 (perfil analista) — habilita análise
- US-10 (desclassificar) — fluxo básico
- US-14 (recurso) — transparência
- US-16 (visualizar status) — transparência

### Sprint 2 — Análise e Recursos
Implementar o coração do sistema:
- US-08 (pontuar documentos) — validação técnica prévia
- US-15 (julgar recurso) — depende de decisão sobre efeitos
- US-07 (alterar documentos) — conveniência

### Sprint 3 — Configurações e Complementos
- US-02 (pesos entrevista)
- US-03, US-04 (calendários)
- US-09 (pontuar entrevista)
- US-11 (lista editável)

### Sprint 4 — Exportações
- US-12 (CSV/HTML) — depende de formato de referência

---

*Gerado pela skill backlog-scorer-skill em 25/09/2026*
