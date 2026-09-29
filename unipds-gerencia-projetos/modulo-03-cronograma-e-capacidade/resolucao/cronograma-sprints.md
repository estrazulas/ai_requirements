# Cronograma de Sprints — Projeto Análise Documental

**Data de Criação:** 29/09/2026
**Data de Início:** 30/09/2026
**Término Estimado:** Dezembro/2026

---

## Contexto do Time

### Composição

| Papel | Senioridade | Foco Técnico | Horas/Sprint |
|-------|-------------|--------------|--------------|
| Dev 1 | Sênior | Full Stack (Backend + Frontend) | 36.4h |
| Dev 2 | Sênior | Full Stack (Backend + Frontend) | 36.4h |
| Dev 3 | Pleno | Backend + Frontend | 36.4h |

### Capacidade

- **Duração da Sprint:** 14 dias (2 semanas)
- **Horas por dia:** 4h/pessoa
- **Capacidade nominal por sprint:** 14 dias × 4h = 56h/pessoa
- **Capacidade real (65%):** 56h × 0.65 = **36.4h/pessoa/sprint**
- **Capacidade total do time:** 3 pessoas × 36.4h = **109.2h/sprint**
- **Velocidade estimada:** 40 Story Points/sprint

### Período do Projeto

- **Início:** 30/09/2026
- **Término estimado:** Dezembro/2026
- **Duração total:** ~3 meses = **6 sprints**
- **Férias:** Nenhuma programada no curto prazo

---

## Feriados no Período

### Novembro 2026

| Data | Dia da Semana | Feriado | Impacto |
|------|---------------|---------|---------|
| 02/11 | Segunda | Finados | -1 dia útil |
| 15/11 | Domingo | Proclamação da República | Sem impacto (domingo) |
| 20/11 | Sexta | Dia da Consciência Negra | -1 dia útil |

**Total de feriados em novembro:** 2 dias úteis perdidos

### Ajuste de Capacidade em Novembro

- **Sprints em novembro:** Sprint 5 (02/11 - 13/11) e Sprint 6 (16/11 - 27/11)
- **Sprint 5:** Perde 1 dia (02/11) → capacidade reduzida em ~7.3h
- **Sprint 6:** Perde 1 dia (20/11) → capacidade reduzida em ~7.3h

---

## Backlog de Input

| US | Título | Story Points | Effort (h) | Fase | Categoria |
|----|--------|--------------|------------|------|-----------|
| US-01 | Cadastrar critério "Análise Documental" no edital | 2 | 5.5h | 1 | Must |
| US-02 | Configurar pesos de entrevista no edital | 3 | 8.2h | 4 | Should |
| US-03 | Cadastrar calendário de etapa por edital | 5 | 13.7h | 5 | Should |
| US-04 | Cadastrar calendário de etapa por curso/oferta | 5 | 13.7h | 5 | Could |
| US-05 | Configurar tipo de documento com pontuação | 2 | 5.5h | 1 | Must |
| US-06 | Candidato declara pontuação ao enviar documentos | 8 | 21.8h | 2 | Must |
| US-07 | Candidato altera documentos e pontuação dentro do prazo | 5 | 13.7h | 3 | Should |
| US-08 | Analista pontua documentos do candidato | 13 | 35.5h | 3 | Must |
| US-09 | Analista pontua entrevista do candidato | 3 | 8.2h | 4 | Should |
| US-10 | Analista desclassifica candidato | 2 | 5.5h | 4 | Must |
| US-11 | Lista de classificação com edição manual | 8 | 21.8h | 4 | Should |
| US-12 | Exportar classificação em CSV e HTML | 5 | 13.7h | 5 | Could |
| US-13 | Perfil "Analista de Documento" | 5 | 13.7h | 1 | Must |
| US-14 | Candidato interpõe recurso pelo portal | 5 | 13.7h | 5 | Could |
| US-15 | Analista julga recurso | 8 | 21.8h | 5 | Could |
| US-16 | Candidato visualiza status e pontuação no portal | 5 | 13.7h | 4 | Must |

**Total:** 84 Story Points | 229.3h

---

## Dependências Conhecidas

### Dependências Internas

| US Dependente | Depende de | Razão Técnica |
|---------------|------------|---------------|
| US-06 | US-01, US-05 | Precisa do critério AD e tipos de documento configurados |
| US-07 | US-06 | Precisa do fluxo de declaração de pontuação |
| US-08 | US-06, US-13 | Precisa dos documentos enviados e perfil analista |
| US-02 | US-01 | Precisa do critério AD configurado |
| US-09 | US-02, US-08 | Precisa dos pesos e da análise documental |
| US-10 | US-08 | Precisa da análise documental |
| US-11 | US-08, US-09 | Precisa das pontuações atribuídas |
| US-12 | US-11 | Precisa da lista de classificação |
| US-14 | US-03 | Precisa do calendário de recurso |
| US-15 | US-14, US-08 | Precisa do recurso e da análise original |
| US-16 | US-10, US-11 | Precisa do status de eliminação e classificação |

### Dependências Externas

**Nenhuma dependência externa identificada.**

---

## Restrições

- **Capacidade limitada:** 4h/dia por pessoa (projeto paralelo a outras atividades)
- **Feriados em novembro:** 2 dias úteis perdidos (02/11 e 20/11)
- **Sem data de término fixa:** Estimativa de dezembro/2026
- **Sem dependências externas:** Todos os componentes estão sob controle do time

---

## 1. Cronograma por Sprint

### Sprint 1 (30/09 - 13/10/2026) — Fase 1: Fundação

**Objetivo:** Configurar base do sistema (critérios, tipos de documento, perfil analista)

| US | Título | Responsável | Effort | Status |
|----|--------|-------------|--------|--------|
| US-01 | Cadastrar critério "Análise Documental" no edital | Dev 1 (Sênior) | 5.5h | Planejado |
| US-05 | Configurar tipo de documento com pontuação | Dev 2 (Sênior) | 5.5h | Planejado |
| US-13 | Perfil "Analista de Documento" | Dev 3 (Pleno) | 13.7h | Planejado |

**Capacidade utilizada:**
- Dev 1: 5.5h / 36.4h = 15%
- Dev 2: 5.5h / 36.4h = 15%
- Dev 3: 13.7h / 36.4h = 38%
- **Total:** 24.7h / 109.2h = 23%

**Observações:**
- Sprint leve para permitir ajustes de ambiente e onboarding
- US-01 e US-05 são CRUDs simples, podem ser feitos em paralelo
- US-13 é mais complexa (novo perfil + vinculação a oferta), alocada ao Dev 3

---

### Sprint 2 (14/10 - 27/10/2026) — Fase 2: Inscrição com Pontuação

**Objetivo:** Implementar fluxo de declaração de pontuação pelo candidato

| US | Título | Responsável | Effort | Status |
|----|--------|-------------|--------|--------|
| US-06 | Candidato declara pontuação ao enviar documentos | Dev 1 + Dev 2 | 21.8h | Planejado |

**Capacidade utilizada:**
- Dev 1: 10.9h / 36.4h = 30%
- Dev 2: 10.9h / 36.4h = 30%
- Dev 3: 0h / 36.4h = 0% (disponível para suporte)
- **Total:** 21.8h / 109.2h = 20%

**Observações:**
- US-06 é complexa (upload + validação de tetos + cálculo em tempo real)
- Alocada a 2 devs seniores para garantir qualidade
- Dev 3 fica disponível para suporte, testes ou ajustes de ambiente

---

### Sprint 3 (28/10 - 10/11/2026) — Fase 3: Análise Documental

**Objetivo:** Implementar tela de análise documental (coração do sistema)

| US | Título | Responsável | Effort | Status |
|----|--------|-------------|--------|--------|
| US-07 | Candidato altera documentos e pontuação dentro do prazo | Dev 3 (Pleno) | 13.7h | Planejado |
| US-08 | Analista pontua documentos do candidato | Dev 1 + Dev 2 | 35.5h | Planejado |

**Capacidade utilizada:**
- Dev 1: 17.8h / 36.4h = 49%
- Dev 2: 17.8h / 36.4h = 49%
- Dev 3: 13.7h / 36.4h = 38%
- **Total:** 49.2h / 109.2h = 45%

**Observações:**
- US-08 é a mais complexa do projeto (visualizador PDF + cálculo + auditoria)
- Requer 2 devs seniores trabalhando em paralelo
- US-07 é independente e pode ser feita pelo Dev 3

---

### Sprint 4 (11/11 - 24/11/2026) — Fase 4: Classificação e Portal

**Objetivo:** Implementar lista de classificação, desclassificação e visualização no portal

**Atenção:** Sprint impactada por feriado (20/11) — capacidade reduzida

| US | Título | Responsável | Effort | Status |
|----|--------|-------------|--------|--------|
| US-02 | Configurar pesos de entrevista no edital | Dev 3 (Pleno) | 8.2h | Planejado |
| US-10 | Analista desclassifica candidato | Dev 3 (Pleno) | 5.5h | Planejado |
| US-16 | Candidato visualiza status e pontuação no portal | Dev 1 (Sênior) | 13.7h | Planejado |
| US-11 | Lista de classificação com edição manual | Dev 2 (Sênior) | 21.8h | Planejado |

**Capacidade utilizada:**
- Dev 1: 13.7h / 29.1h = 47% (capacidade reduzida pelo feriado)
- Dev 2: 21.8h / 29.1h = 75% (capacidade reduzida pelo feriado)
- Dev 3: 13.7h / 29.1h = 47% (capacidade reduzida pelo feriado)
- **Total:** 49.2h / 87.3h = 56%

**Observações:**
- Feriado 20/11 reduz capacidade de 36.4h para 29.1h por pessoa
- US-11 é complexa (lista editável + auditoria), alocada ao Dev 2
- US-16 depende de US-10 e US-11, mas pode ser desenvolvida em paralelo
- US-09 (pontuação de entrevista) não foi alocada por dependência de US-08 e US-02

---

### Sprint 5 (25/11 - 08/12/2026) — Fase 5: Entrevista e Recurso

**Objetivo:** Implementar pontuação de entrevista e fluxo de recurso

**Atenção:** Sprint impactada por feriado (02/11 já passou, mas sprint começa em 25/11)

| US | Título | Responsável | Effort | Status |
|----|--------|-------------|--------|--------|
| US-09 | Analista pontua entrevista do candidato | Dev 3 (Pleno) | 8.2h | Planejado |
| US-03 | Cadastrar calendário de etapa por edital | Dev 1 (Sênior) | 13.7h | Planejado |
| US-04 | Cadastrar calendário de etapa por curso/oferta | Dev 2 (Sênior) | 13.7h | Planejado |
| US-14 | Candidato interpõe recurso pelo portal | Dev 3 (Pleno) | 13.7h | Planejado |

**Capacidade utilizada:**
- Dev 1: 13.7h / 36.4h = 38%
- Dev 2: 13.7h / 36.4h = 38%
- Dev 3: 21.9h / 36.4h = 60%
- **Total:** 49.3h / 109.2h = 45%

**Observações:**
- US-09 depende de US-02 e US-08 (já prontas)
- US-03 e US-04 são calendários independentes
- US-14 depende de US-03 (calendário de recurso)

---

### Sprint 6 (09/12 - 22/12/2026) — Fase 6: Julgamento e Exportação

**Objetivo:** Implementar julgamento de recurso e exportação de classificação

| US | Título | Responsável | Effort | Status |
|----|--------|-------------|--------|--------|
| US-15 | Analista julga recurso | Dev 1 (Sênior) | 21.8h | Planejado |
| US-12 | Exportar classificação em CSV e HTML | Dev 2 (Sênior) | 13.7h | Planejado |

**Capacidade utilizada:**
- Dev 1: 21.8h / 36.4h = 60%
- Dev 2: 13.7h / 36.4h = 38%
- Dev 3: 0h / 36.4h = 0% (disponível para suporte)
- **Total:** 35.5h / 109.2h = 33%

**Observações:**
- US-15 é complexa (múltiplas visualizações + decisão + recálculo)
- US-12 depende de US-11 (lista de classificação)
- Sprint leve para permitir ajustes finais e testes

---

## 2. Dependências Mapeadas

### Dependências Explícitas

| US Dependente | Depende de | Razão Técnica | Sprint de Desbloqueio |
|---------------|------------|---------------|------------------------|
| US-06 | US-01, US-05 | Precisa do critério AD e tipos de documento | Sprint 2 (após Sprint 1) |
| US-07 | US-06 | Precisa do fluxo de declaração de pontuação | Sprint 3 (após Sprint 2) |
| US-08 | US-06, US-13 | Precisa dos documentos enviados e perfil analista | Sprint 3 (após Sprint 1 e 2) |
| US-02 | US-01 | Precisa do critério AD configurado | Sprint 4 (após Sprint 1) |
| US-09 | US-02, US-08 | Precisa dos pesos e da análise documental | Sprint 5 (após Sprint 4) |
| US-10 | US-08 | Precisa da análise documental | Sprint 4 (após Sprint 3) |
| US-11 | US-08, US-09 | Precisa das pontuações atribuídas | Sprint 4 (após Sprint 3) |
| US-12 | US-11 | Precisa da lista de classificação | Sprint 6 (após Sprint 4) |
| US-14 | US-03 | Precisa do calendário de recurso | Sprint 5 (após Sprint 5) |
| US-15 | US-14, US-08 | Precisa do recurso e da análise original | Sprint 6 (após Sprint 5) |
| US-16 | US-10, US-11 | Precisa do status de eliminação e classificação | Sprint 4 (após Sprint 3 e 4) |

### Dependências Implícitas

| US Dependente | Depende de | Razão Técnica |
|---------------|------------|---------------|
| US-16 | US-03 | Precisa do calendário para respeitar datas de publicação |
| US-14 | US-04 | Pode precisar do calendário por oferta (alternativa) |

---

## 3. Caminho Crítico

O caminho crítico é a sequência de USs cujo atraso impacta diretamente a data final do projeto:

```
US-01 (Sprint 1) → US-06 (Sprint 2) → US-08 (Sprint 3) → US-11 (Sprint 4) → US-16 (Sprint 4)
```

**Duração do caminho crítico:** 4 sprints (8 semanas)

**USs no caminho crítico:**
- US-01: Cadastrar critério AD (5.5h)
- US-06: Candidato declara pontuação (21.8h)
- US-08: Analista pontua documentos (35.5h)
- US-11: Lista de classificação (21.8h)
- US-16: Candidato visualiza status (13.7h)

**Total:** 98.3h (43% do backlog total)

**Risco:** Qualquer atraso nessas USs impacta a data final do projeto.

---

## 4. Flags de Risco ⚠️

### ⚠️ US-08: Visualizador PDF Inline

**Descrição:** US-08 (35.5h) requer visualizador PDF inline no navegador. Viabilidade técnica não confirmada.

**Impacto:** Se a implementação do visualizador PDF atrasar, todo o caminho crítico é impactado (US-08 → US-11 → US-16).

**Mitigação:** Validar biblioteca/componente (pdf.js, react-pdf) antes do Sprint 3.

---

### ⚠️ US-13: Modelo de Permissões

**Descrição:** US-13 (13.7h) requer vinculação de analista a oferta específica. Modelo de permissões atual pode não suportar vinculação granular.

**Impacto:** Se o modelo não suportar, a implementação pode ser mais complexa que o estimado.

**Mitigação:** Validar modelo de permissões antes do Sprint 1.

---

### ⚠️ Capacidade Reduzida em Novembro

**Descrição:** Feriados em novembro (02/11 e 20/11) reduzem capacidade das Sprints 4 e 5.

**Impacto:** Sprint 4 tem capacidade reduzida de 109.2h para 87.3h (-20%).

**Mitigação:** Sprint 4 já está planejada com 56% de utilização, então há margem.

---

### ⚠️ US-06: Base ENEM Não Mapeada

**Descrição:** US-06 (21.8h) depende de base existente (ENEM) para pontuação declarada. Reaproveitamento não documentado.

**Impacto:** Se não for possível reaproveitar, o effort pode ser maior que o estimado.

**Mitigação:** Mapear base ENEM antes do Sprint 2.

---

## 5. Soluções de Contorno

### Blocker: Visualizador PDF (US-08)

**Solução de contorno:** Implementar upload de PDF com link para download, em vez de visualizador inline. Isso permite que o analista visualize o documento em outra aba ou aplicativo externo.

**Trade-off:** Perde conveniência, mas mantém o fluxo funcional.

**Quando usar:** Se a validação técnica do visualizador PDF não for concluída antes do Sprint 3.

---

### Blocker: Modelo de Permissões (US-13)

**Solução de contorno:** Implementar vinculação por unidade (ao invés de oferta), usando o modelo existente. Analista teria acesso a todas as ofertas da unidade.

**Trade-off:** Perde granularidade, mas mantém a separação de responsabilidades.

**Quando usar:** Se o modelo de permissões não suportar vinculação por oferta.

---

### Blocker: Base ENEM Não Mapeada (US-06)

**Solução de contorno:** Implementar fluxo de pontuação declarada do zero, sem reaproveitamento da base ENEM.

**Trade-off:** Aumenta o effort de US-06 de 21.8h para ~30h, mas mantém o fluxo funcional.

**Quando usar:** Se não for possível reaproveitar a base ENEM.

---

## 6. Resumo do Cronograma

| Sprint | Período | USs Alocadas | Story Points | Capacidade Utilizada |
|--------|---------|--------------|--------------|----------------------|
| Sprint 1 | 30/09 - 13/10 | US-01, US-05, US-13 | 10 SP | 23% |
| Sprint 2 | 14/10 - 27/10 | US-06 | 8 SP | 20% |
| Sprint 3 | 28/10 - 10/11 | US-07, US-08 | 18 SP | 45% |
| Sprint 4 | 11/11 - 24/11 | US-02, US-10, US-16, US-11 | 18 SP | 56% |
| Sprint 5 | 25/11 - 08/12 | US-09, US-03, US-04, US-14 | 18 SP | 45% |
| Sprint 6 | 09/12 - 22/12 | US-15, US-12 | 13 SP | 33% |
| **Total** | | **16 USs** | **84 SP** | **38% (média)** |

---

## 7. Ordem de Implementação Recomendada

1. **Sprint 1:** US-01 → US-05 → US-13 (fundação — sem dependências)
2. **Sprint 2:** US-06 (inscrição com pontuação — depende de US-01, US-05)
3. **Sprint 3:** US-07 → US-08 (alteração e análise — depende de US-06, US-13)
4. **Sprint 4:** US-02 → US-10 → US-11 → US-16 (classificação e portal — depende de US-08)
5. **Sprint 5:** US-09 → US-03 → US-04 → US-14 (entrevista e recurso — depende de US-02, US-08)
6. **Sprint 6:** US-15 → US-12 (julgamento e exportação — depende de US-14, US-11)

---

## 8. Análise What-If

### Cenário 1: Visualizador PDF atrasa 1 sprint

**Impacto:**
- US-08 atrasa para Sprint 4
- US-11, US-16, US-09, US-10 atrasam para Sprint 5
- US-15, US-12 atrasam para Sprint 7
- **Projeto estende para Janeiro/2027**

**Opções de resposta:**
1. **Implementar solução de contorno:** Upload com link para download (perde conveniência, mas mantém cronograma)
2. **Alocar 3 devs para US-08:** Reduz effort de 35.5h para ~25h, mas requer coordenação intensa

**Recomendação:** Opção 1 — solução de contorno mantém o cronograma e pode ser melhorada posteriormente.

---

### Cenário 2: Dev 1 ausente por 1 semana no Sprint 3

**Impacto:**
- US-08 perde 18h de capacidade (1 semana × 4h/dia × 5 dias = 20h, mas considerando 65% = 13h)
- US-08 não cabe no Sprint 3 com apenas Dev 2
- US-08 atrasa para Sprint 4

**Opções de resposta:**
1. **Reduzir escopo de US-08:** Implementar apenas pontuação básica, sem visualizador PDF
2. **Alocar Dev 3 para US-08:** Dev 3 assume parte de US-08, mas perde capacidade para US-07

**Recomendação:** Opção 2 — Dev 3 assume US-07 (13.7h) e parte de US-08 (10h), mantendo o cronograma.

---

## 9. Próximos Passos

1. **Validar viabilidade técnica do visualizador PDF** antes do Sprint 3
2. **Validar modelo de permissões** antes do Sprint 1
3. **Mapear base ENEM** antes do Sprint 2
4. **Confirmar feriados de novembro** (02/11 e 20/11)
5. **Ajustar cronograma** conforme validações técnicas

---

*Gerado pela skill scheduling-prompt em 29/09/2026*
*Baseado no template de Ahirton Lopes · PM AI Toolkit*
