# MoSCoW — MUST HAVE

> Sem isso o projeto falha → sempre incluir no scoring

---

## User Stories Incluídas

| US | Título | Sprint Sugerida |
|----|--------|-----------------|
| US-01 | Cadastrar critério "Análise Documental" no edital | Sprint 1 |
| US-05 | Configurar tipo de documento com pontuação | Sprint 1 |
| US-06 | Candidato declara pontuação ao enviar documentos | Sprint 2 |
| US-08 | Analista pontua documentos do candidato | Sprint 2 |
| US-13 | Perfil "Analista de Documento" | Sprint 1 |

---

## Tabela RICE

| Item | Reach | Impact | Confidence | Effort (pm) | RICE Score |
|------|-------|--------|------------|-------------|------------|
| US-01 — Critério AD no edital | 50 | 3 | 100% | 0.5 | 300.0 |
| US-05 — Tipo documento pontuação | 3 | 2 | 100% | 0.3 | 20.0 |
| US-06 — Candidato declara pontuação | 200 | 3 | 80% | 1.0 | 480.0 |
| US-08 — Analista pontua documentos | 30 | 3 | 80% | 2.0 | 36.0 |
| US-13 — Perfil Analista | 30 | 3 | 80% | 0.5 | 144.0 |

---

## Tabela WSJF

| Item | BV | TC | RR | CoD | Job Size | WSJF |
|------|----|----|----|-----|----------|------|
| US-01 — Critério AD no edital | 9 | 8 | 10 | 27 | 2 | 13.5 |
| US-05 — Tipo documento pontuação | 8 | 5 | 8 | 21 | 1 | 21.0 |
| US-06 — Candidato declara pontuação | 10 | 8 | 9 | 27 | 3 | 9.0 |
| US-08 — Analista pontua documentos | 10 | 9 | 8 | 27 | 5 | 5.4 |
| US-13 — Perfil Analista | 9 | 7 | 9 | 25 | 2 | 12.5 |

---

## Ranking Combinado (Must Have)

| Posição | Item | RICE | WSJF | Justificativa |
|---------|------|------|------|---------------|
| 1 | **US-01 — Critério AD no edital** | 300.0 | 13.5 | Habilita todo o fluxo. WSJF alto (RR=10 desbloqueia tudo) |
| 2 | **US-06 — Candidato declara pontuação** | 480.0 | 9.0 | Elimina conferência manual de tetos (KR1). Maior RICE |
| 3 | **US-13 — Perfil Analista** | 144.0 | 12.5 | Habilita US-08, US-09, US-10, US-15. RR alto |
| 4 | **US-05 — Tipo documento pontuação** | 20.0 | 21.0 | Base para US-06. WSJF mais alto (21.0) |
| 5 | **US-08 — Analista pontua documentos** | 36.0 | 5.4 | Coração do fluxo, mas effort alto e dependências técnicas |

---

## Justificativas

**US-01 — Critério AD no edital**
- **Impact 3 (massivo):** habilita todo o fluxo de análise documental. Sem isso, nada existe.
- **Confidence 100%:** extensão de combobox existente, sem risco técnico.
- **Business Value 9:** contribuição direta para KR1 (eliminar etapas manuais) e KR2 (100% no sistema).
- **Risk Reduction 10:** desbloqueia todas as outras USs do fluxo.

**US-05 — Tipo documento pontuação**
- **Impact 2 (significativo):** define quais documentos requerem pontuação. Base para US-06.
- **Confidence 100%:** extensão do CRUD existente de tipos de documento.
- **Business Value 8:** necessário para validação de tetos (KR1).
- **Risk Reduction 8:** desbloqueia US-06.

**US-06 — Candidato declara pontuação**
- **Impact 3 (massivo):** elimina conferência manual de tetos (KR1). Candidato declara, sistema valida em tempo real.
- **Confidence 80%:** requisito claro, mas depende de US-01 e US-05. Validação técnica de tetos precisa ser testada.
- **Business Value 10:** contribuição máxima para KR1 (eliminar conferência de tetos).
- **Risk Reduction 9:** desbloqueia US-08 (analista vê pontuação declarada).

**US-08 — Analista pontua documentos**
- **Impact 3 (massivo):** coração do fluxo de análise. Sem isso, analista não trabalha no sistema.
- **Confidence 80%:** visualizador PDF inline precisa validação técnica. Se não for viável, effort aumenta.
- **Business Value 10:** contribuição máxima para KR2 (100% das análises no sistema).
- **Risk Reduction 8:** desbloqueia US-09, US-10, US-11, US-15.

**US-13 — Perfil Analista**
- **Impact 3 (massivo):** habilita US-08, US-09, US-10, US-15. Sem perfil, analistas não acessam sistema.
- **Confidence 80%:** decisão pendente sobre quem cadastra (admin vs. gestão local). Modelo de permissões precisa suportar vinculação a oferta.
- **Business Value 9:** necessário para separação de responsabilidades.
- **Risk Reduction 9:** desbloqueia 4 USs do fluxo de análise.

---

## Flags

**US-08 — Analista pontua documentos:** visualizador PDF inline precisa validação técnica → time de engenharia precisa validar biblioteca (pdf.js, react-pdf) antes de estimar effort com precisão.

**US-13 — Perfil Analista:** decisão pendente sobre quem cadastra (pergunta 5 do documento) → stakeholder precisa decidir se é admin/setor solicitante ou gestão local. Modelo de permissões precisa suportar vinculação granular por oferta.

**US-06 — Dependência não mapeada:** base existente de "pontuação declarada + correção" (ENEM) precisa ser mapeada → time de engenharia precisa validar o que pode ser reaproveitado e o que precisa ser reescrito.

---

## Dependências Internas

```
US-01 (critério) → US-06 (declara pontuação)
US-05 (tipo documento) → US-06 (declara pontuação)
US-13 (perfil analista) → US-08 (analista pontua)
US-06 (declara pontuação) → US-08 (analista pontua)
```

**Ordem de desenvolvimento recomendada:**
1. US-01 + US-05 + US-13 (paralelo, sem dependências entre si)
2. US-06 (depende de US-01 e US-05)
3. US-08 (depende de US-06 e US-13)

---

*Data: 25/09/2026*
*OKR: Eliminar processo manual de análise documental por planilhas*
