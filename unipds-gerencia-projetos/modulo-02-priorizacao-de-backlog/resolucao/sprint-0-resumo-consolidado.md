# MoSCoW — Resumo Consolidado

> Priorização do backlog com filtragem MoSCoW + RICE Score + WSJF

---

## Visão Geral

| Categoria | Qtd USs | Esforço Total (pm) | % do Esforço | Sprint Sugerido |
|-----------|---------|-------------------|--------------|-----------------|
| **Must Have** | 5 | 4.3 | 27% | Sprint 1-2 |
| **Should Have** | 7 | 3.8 | 24% | Sprint 3-4 |
| **Could Have** | 4 | 2.5 | 16% | Sprint 5+ |
| **Won't Have** | 0 | 0 | 0% | — |
| **Total** | 16 | 10.6 | 67% | — |

*Nota: 33% do esforço restante refere-se a funcionalidades fora do escopo (nivelamento, convocação para entrevista, notificações, etc.) que dependem de definições pendentes.*

---

## Distribuição por Sprint

### Sprint 1-2 (Must Have — 27% do esforço)

| Ordem | US | Título | Effort (pm) |
|-------|----|--------|-------------|
| 1 | US-01 | Cadastrar critério "Análise Documental" no edital | 0.5 |
| 2 | US-05 | Configurar tipo de documento com pontuação | 0.3 |
| 3 | US-13 | Perfil "Analista de Documento" | 0.5 |
| 4 | US-06 | Candidato declara pontuação ao enviar documentos | 1.0 |
| 5 | US-08 | Analista pontua documentos do candidato | 2.0 |

**Objetivo:** habilitar o fluxo básico de análise documental no sistema.

---

### Sprint 3-4 (Should Have — 24% do esforço)

| Ordem | US | Título | Effort (pm) |
|-------|----|--------|-------------|
| 6 | US-02 | Configurar pesos de entrevista no edital | 0.3 |
| 7 | US-03 | Cadastrar calendário de etapa por edital | 0.5 |
| 8 | US-04 | Cadastrar calendário de etapa por curso/oferta | 0.5 |
| 9 | US-09 | Analista pontua entrevista do candidato | 0.5 |
| 10 | US-10 | Analista desclassifica candidato | 0.3 |
| 11 | US-11 | Lista de classificação com edição manual | 1.0 |
| 12 | US-16 | Candidato visualiza status e pontuação no portal | 0.5 |

**Objetivo:** completar o fluxo de análise, classificação e transparência ao candidato.

---

### Sprint 5+ (Could Have — 16% do esforço)

| Ordem | US | Título | Effort (pm) |
|-------|----|--------|-------------|
| 13 | US-07 | Candidato altera documentos e pontuação dentro do prazo | 0.5 |
| 14 | US-14 | Candidato interpõe recurso pelo portal | 0.5 |
| 15 | US-15 | Analista julga recurso | 1.0 |
| 16 | US-12 | Exportar classificação em CSV e HTML | 0.5 |

**Objetivo:** adicionar flexibilidade, direito ao contraditório e exportação para publicação.

---

## Top 5 Prioridades (Ranking Combinado)

| Posição | US | Categoria | RICE | WSJF | Justificativa |
|---------|----|-----------|------|------|---------------|
| 1 | US-16 | Should | 1200.0 | 13.0 | Maior RICE. KR3 (transparência). Todos candidatos visualizam |
| 2 | US-14 | Could | 800.0 | 10.5 | Direito ao contraditório. Alto alcance |
| 3 | US-06 | Must | 480.0 | 9.0 | Elimina conferência manual de tetos (KR1) |
| 4 | US-07 | Could | 400.0 | 7.0 | Flexibilidade para candidato |
| 5 | US-02 | Should | 333.3 | 18.0 | Automatiza cálculo manual. WSJF alto |

---

## Flags Críticas (Pendências)

| US | Flag | Ação Necessária |
|----|------|-----------------|
| US-08 | Visualizador PDF inline | Time de engenharia valida biblioteca (pdf.js, react-pdf) |
| US-13 | Quem cadastra analista? | Stakeholder decide (pergunta 5) |
| US-12 | Formato de relatórios | Setor solicitante fornece exemplos de convocações |
| US-14 | Recurso de recurso? | Stakeholder decide (pergunta 7) |
| US-15 | Efeitos do deferimento | Stakeholder define (pergunta 8) |
| US-06, US-08, US-11 | Base existente (ENEM) | Time de engenharia mapeia reaproveitamento |

---

## Arquivos Gerados

- `moscow-must-have.md` — 5 USs essenciais para o fluxo funcionar
- `moscow-should-have.md` — 7 USs importantes para completar o fluxo
- `moscow-could-have.md` — 4 USs desejáveis se houver capacidade
- `moscow-wont-have.md` — 0 USs excluídas + funcionalidades fora do escopo

---

## Próximos Passos

1. **Resolver pendências** com stakeholder (perguntas 1, 2, 3, 5, 7, 8, 10)
2. **Validar viabilidade técnica** do visualizador PDF (US-08)
3. **Mapear base existente** (ENEM) para reaproveitamento (US-06, US-08, US-11)
4. **Receber exemplos** de convocações publicadas (US-12)
5. **Iniciar Sprint 1** com US-01 + US-05 + US-13 (paralelo)

---

*Data: 25/09/2026*
*OKR: Eliminar processo manual de análise documental por planilhas*
*Skill: Backlog Scorer (RICE + WSJF) · Ahirton Lopes · PM AI Toolkit*
