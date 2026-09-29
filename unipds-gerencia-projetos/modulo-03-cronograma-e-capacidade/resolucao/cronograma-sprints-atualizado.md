# Cronograma de Sprints — Projeto Análise Documental (ATUALIZADO)

**Data de Criação:** 29/09/2026
**Data de Atualização:** 29/09/2026
**Data de Início:** 30/09/2026
**Término Estimado:** Dezembro/2026

---

## ⚠️ Mudança de Contexto

**Alteração:** Dev 3 (Pleno) vai pegar licença médica

**Impacto:**
- Capacidade do time reduzida de 3 para 2 pessoas
- Capacidade total cai de 78h para 52h/sprint (-33%)
- Necessário redistribuir backlog ou estender cronograma

---

## Contexto do Time (ATUALIZADO)

### Composição

| Papel | Senioridade | Foco Técnico | Horas/Sprint |
|-------|-------------|--------------|--------------|
| Dev 1 | Sênior | Full Stack (Backend + Frontend) | 26h |
| Dev 2 | Sênior | Full Stack (Backend + Frontend) | 26h |
| ~~Dev 3~~ | ~~Pleno~~ | ~~Backend + Frontend~~ | ~~26h~~ **EM LICENÇA** |

### Capacidade (ATUALIZADA)

- **Duração da Sprint:** 14 dias corridos = 2 semanas = **10 dias úteis**
- **Horas por dia:** 4h/pessoa
- **Capacidade nominal por sprint:** 10 dias úteis × 4h = **40h/pessoa/sprint**
- **Capacidade real (65%):** 40h × 0.65 = **26h/pessoa/sprint**
- **Capacidade total do time:** 2 pessoas × 26h = **52h/sprint** (era 78h)
- **Velocidade estimada:** 27 Story Points/sprint (era 40 SP)

### Período do Projeto

- **Início:** 30/09/2026
- **Término estimado:** Dezembro/2026
- **Duração total:** ~3 meses = **6 sprints**
- **Férias:** Nenhuma programada no curto prazo

---

## Feriados no Período

### Novembro 2026

| Data | Dia da Semana | Feriado | Sprint Afetada |
|------|---------------|---------|----------------|
| 02/11 | Segunda | Finados | Sprint 3 (28/10 - 10/11) |
| 20/11 | Sexta | Dia da Consciência Negra | Sprint 4 (11/11 - 24/11) |

**Total de feriados:** 2 dias úteis perdidos

### Ajuste de Capacidade por Sprint (ATUALIZADO)

| Sprint | Período | Dias Úteis | Feriados | Dias Efetivos | Capacidade (por pessoa) | Capacidade Total (time) |
|--------|---------|------------|----------|---------------|-------------------------|-------------------------|
| Sprint 1 | 30/09 - 13/10 | 10 | 0 | 10 | 26h | 52h |
| Sprint 2 | 14/10 - 27/10 | 10 | 0 | 10 | 26h | 52h |
| Sprint 3 | 28/10 - 10/11 | 10 | 1 (02/11) | 9 | 23.4h | 46.8h |
| Sprint 4 | 11/11 - 24/11 | 10 | 1 (20/11) | 9 | 23.4h | 46.8h |
| Sprint 5 | 25/11 - 08/12 | 10 | 0 | 10 | 26h | 52h |
| Sprint 6 | 09/12 - 22/12 | 10 | 0 | 10 | 26h | 52h |

**Capacidade total do projeto:** 303.6h (era 452.4h)

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
- **Time reduzido:** Apenas 2 devs seniores (Dev 3 em licença)
- **Feriados em novembro:** 2 dias úteis perdidos (02/11 e 20/11)
- **Sem data de término fixa:** Estimativa de dezembro/2026
- **Sem dependências externas:** Todos os componentes estão sob controle do time

---

## 1. Cronograma por Sprint (ATUALIZADO)

### Sprint 1 (30/09 - 13/10/2026) — Fase 1: Fundação

**Capacidade disponível:** 52h (10 dias úteis)

**Objetivo:** Configurar base do sistema (critérios, tipos de documento, perfil analista)

| US | Título | Responsável | Effort | Status |
|----|--------|-------------|--------|--------|
| US-01 | Cadastrar critério "Análise Documental" no edital | Dev 1 (Sênior) | 5.5h | Planejado |
| US-05 | Configurar tipo de documento com pontuação | Dev 2 (Sênior) | 5.5h | Planejado |

**Capacidade utilizada:**
- Dev 1: 5.5h / 26h = 21%
- Dev 2: 5.5h / 26h = 21%
- **Total:** 11h / 52h = **21%**

**Observações:**
- Sprint leve para permitir ajustes de ambiente e onboarding
- US-01 e US-05 são CRUDs simples, podem ser feitos em paralelo
- US-13 (Perfil Analista) foi movida para Sprint 2 devido à capacidade reduzida
- Margem de 41h para imprevistos ou ajustes

---

### Sprint 2 (14/10 - 27/10/2026) — Fase 2: Inscrição com Pontuação

**Capacidade disponível:** 52h (10 dias úteis)

**Objetivo:** Implementar perfil analista e fluxo de declaração de pontuação

| US | Título | Responsável | Effort | Status |
|----|--------|-------------|--------|--------|
| US-13 | Perfil "Analista de Documento" | Dev 1 (Sênior) | 13.7h | Planejado |
| US-06 | Candidato declara pontuação ao enviar documentos | Dev 2 (Sênior) | 21.8h | Planejado |

**Capacidade utilizada:**
- Dev 1: 13.7h / 26h = 53%
- Dev 2: 21.8h / 26h = 84%
- **Total:** 35.5h / 52h = **68%**

**Observações:**
- US-13 é mais complexa (novo perfil + vinculação a oferta), alocada ao Dev 1
- US-06 é complexa (upload + validação de tetos + cálculo em tempo real), alocada ao Dev 2
- Dev 2 está com 84% de utilização — monitorar sobrecarga
- Margem de 16.5h para imprevistos

---

### Sprint 3 (28/10 - 10/11/2026) — Fase 3: Análise Documental

**Capacidade disponível:** 46.8h (9 dias úteis — feriado 02/11)

**Objetivo:** Implementar tela de análise documental (coração do sistema)

| US | Título | Responsável | Effort | Status |
|----|--------|-------------|--------|--------|
| US-07 | Candidato altera documentos e pontuação dentro do prazo | Dev 1 (Sênior) | 13.7h | Planejado |
| US-08 | Analista pontua documentos do candidato | Dev 2 (Sênior) | 23.4h | Planejado |

**Capacidade utilizada:**
- Dev 1: 13.7h / 23.4h = 59%
- Dev 2: 23.4h / 23.4h = 100%
- **Total:** 37.1h / 46.8h = **79%**

**Observações:**
- US-08 é a mais complexa do projeto (visualizador PDF + cálculo + auditoria)
- US-08 foi reduzida de 35.5h para 23.4h — **ESCOPO REDUZIDO** (ver Soluções de Contorno)
- Dev 2 está com 100% de utilização — sprint crítica
- Margem de 9.7h para imprevistos (apenas para Dev 1)

---

### Sprint 4 (11/11 - 24/11/2026) — Fase 4: Classificação e Portal

**Capacidade disponível:** 46.8h (9 dias úteis — feriado 20/11)

**Objetivo:** Implementar lista de classificação, desclassificação e visualização no portal

| US | Título | Responsável | Effort | Status |
|----|--------|-------------|--------|--------|
| US-02 | Configurar pesos de entrevista no edital | Dev 1 (Sênior) | 8.2h | Planejado |
| US-10 | Analista desclassifica candidato | Dev 1 (Sênior) | 5.5h | Planejado |
| US-16 | Candidato visualiza status e pontuação no portal | Dev 2 (Sênior) | 13.7h | Planejado |
| US-11 | Lista de classificação com edição manual | Dev 2 (Sênior) | 21.8h | Planejado |

**Capacidade utilizada:**
- Dev 1: 13.7h / 23.4h = 59%
- Dev 2: 35.5h / 23.4h = 152% ⚠️ **SOBRECARGA**
- **Total:** 49.2h / 46.8h = **105%** ⚠️ **EXCEDE CAPACIDADE**

**Observações:**
- Sprint 4 excede a capacidade disponível em 2.4h
- US-11 (21.8h) é muito grande para um único dev
- **SOLUÇÃO:** Mover 5.5h de US-11 para Sprint 5 ou reduzir escopo

---

### Sprint 5 (25/11 - 08/12/2026) — Fase 5: Entrevista e Recurso

**Capacidade disponível:** 52h (10 dias úteis)

**Objetivo:** Completar US-11 e implementar pontuação de entrevista

| US | Título | Responsável | Effort | Status |
|----|--------|-------------|--------|--------|
| US-11 (continuação) | Lista de classificação com edição manual | Dev 2 (Sênior) | 5.5h | Planejado |
| US-09 | Analista pontua entrevista do candidato | Dev 1 (Sênior) | 8.2h | Planejado |
| US-03 | Cadastrar calendário de etapa por edital | Dev 1 (Sênior) | 13.7h | Planejado |
| US-04 | Cadastrar calendário de etapa por curso/oferta | Dev 2 (Sênior) | 13.7h | Planejado |

**Capacidade utilizada:**
- Dev 1: 21.9h / 26h = 84%
- Dev 2: 19.2h / 26h = 74%
- **Total:** 41.1h / 52h = **79%**

**Observações:**
- US-11 foi dividida: 16.3h no Sprint 4 + 5.5h no Sprint 5
- US-09 depende de US-02 e US-08 (já prontas)
- US-03 e US-04 são calendários independentes
- Margem de 10.9h para imprevistos

---

### Sprint 6 (09/12 - 22/12/2026) — Fase 6: Recurso e Exportação

**Capacidade disponível:** 52h (10 dias úteis)

**Objetivo:** Implementar fluxo de recurso e exportação de classificação

| US | Título | Responsável | Effort | Status |
|----|--------|-------------|--------|--------|
| US-14 | Candidato interpõe recurso pelo portal | Dev 1 (Sênior) | 13.7h | Planejado |
| US-15 | Analista julga recurso | Dev 2 (Sênior) | 21.8h | Planejado |
| US-12 | Exportar classificação em CSV e HTML | Dev 1 (Sênior) | 13.7h | Planejado |

**Capacidade utilizada:**
- Dev 1: 27.4h / 26h = 105% ⚠️ **SOBRECARGA**
- Dev 2: 21.8h / 26h = 84%
- **Total:** 49.2h / 52h = **95%**

**Observações:**
- Sprint 6 excede a capacidade do Dev 1 em 1.4h
- **SOLUÇÃO:** Mover US-12 para Sprint 7 ou reduzir escopo
- US-15 é complexa (múltiplas visualizações + decisão + recálculo)
- US-12 depende de US-11 (lista de classificação)

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
| US-11 | US-08, US-09 | Precisa das pontuações atribuídas | Sprint 4-5 (após Sprint 3) |
| US-12 | US-11 | Precisa da lista de classificação | Sprint 6 (após Sprint 5) |
| US-14 | US-03 | Precisa do calendário de recurso | Sprint 6 (após Sprint 5) |
| US-15 | US-14, US-08 | Precisa do recurso e da análise original | Sprint 6 (após Sprint 6) |
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
US-01 (Sprint 1) → US-06 (Sprint 2) → US-08 (Sprint 3) → US-11 (Sprint 4-5) → US-16 (Sprint 4)
```

**Duração do caminho crítico:** 4 sprints (8 semanas)

**USs no caminho crítico:**
- US-01: Cadastrar critério AD (5.5h)
- US-06: Candidato declara pontuação (21.8h)
- US-08: Analista pontua documentos (23.4h — escopo reduzido)
- US-11: Lista de classificação (21.8h — dividida em 2 sprints)
- US-16: Candidato visualiza status (13.7h)

**Total:** 86.2h (38% do backlog total)

**Risco:** Qualquer atraso nessas USs impacta a data final do projeto.

---

## 4. Flags de Risco ⚠️

### ⚠️ CRÍTICO: Capacidade Insuficiente nos Sprints 4 e 6

**Descrição:** Sprints 4 e 6 excedem a capacidade disponível (105% e 95% respectivamente).

**Impacto:** 
- Sprint 4: excesso de 2.4h
- Sprint 6: excesso de 1.4h
- Total: 3.8h de trabalho não alocado

**Mitigação:**
- Opção 1: Mover US-12 (13.7h) para Sprint 7 (estender projeto para Janeiro/2027)
- Opção 2: Reduzir escopo de US-11 e US-12
- Opção 3: Aumentar horas diárias temporariamente (4h → 5h/dia)

**Recomendação:** Opção 1 — estender para 7 sprints mantém qualidade e evita sobrecarga.

---

### ⚠️ US-08: Visualizador PDF Inline (Escopo Reduzido)

**Descrição:** US-08 foi reduzida de 35.5h para 23.4h devido à capacidade limitada.

**Impacto:** Visualizador PDF inline pode não ser implementado na primeira versão.

**Mitigação:** Implementar upload de PDF com link para download (solução de contorno).

**Quando usar:** Se a capacidade não permitir implementação completa.

---

### ⚠️ US-13: Modelo de Permissões

**Descrição:** US-13 (13.7h) requer vinculação de analista a oferta específica. Modelo de permissões atual pode não suportar vinculação granular.

**Impacto:** Se o modelo não suportar, a implementação pode ser mais complexa que o estimado.

**Mitigação:** Validar modelo de permissões antes do Sprint 2.

---

### ⚠️ Capacidade Reduzida em Novembro

**Descrição:** Feriados em novembro (02/11 e 20/11) reduzem capacidade das Sprints 3 e 4.

**Impacto:** Sprints 3 e 4 têm capacidade reduzida de 52h para 46.8h (-10%).

**Mitigação:** Sprints 3 e 4 já estão planejadas com 79% e 105% de utilização respectivamente.

---

### ⚠️ Dev 2 Sobrecarregado

**Descrição:** Dev 2 está alocado com 84-100% de utilização nos Sprints 2, 3 e 4.

**Impacto:** Qualquer imprevisto pode causar atraso em múltiplas USs.

**Mitigação:** Monitorar de perto; considerar redistribuir tarefas se houver imprevisto.

---

### ⚠️ US-06: Base ENEM Não Mapeada

**Descrição:** US-06 (21.8h) depende de base existente (ENEM) para pontuação declarada. Reaproveitamento não documentado.

**Impacto:** Se não for possível reaproveitar, o effort pode ser maior que o estimado.

**Mitigação:** Mapear base ENEM antes do Sprint 2.

---

## 5. Soluções de Contorno

### Blocker: Capacidade Insuficiente (Sprints 4 e 6)

**Solução de contorno:** Estender projeto para 7 sprints (terminar em Janeiro/2027).

**Trade-off:** Adia entrega em 2 semanas, mas evita sobrecarga do time.

**Quando usar:** Se não for possível aumentar horas diárias ou reduzir escopo.

---

### Blocker: Visualizador PDF (US-08)

**Solução de contorno:** Implementar upload de PDF com link para download, em vez de visualizador inline.

**Trade-off:** Perde conveniência, mas mantém o fluxo funcional.

**Quando usar:** Se a capacidade não permitir implementação completa.

---

### Blocker: Modelo de Permissões (US-13)

**Solução de contorno:** Implementar vinculação por unidade (ao invés de oferta), usando o modelo existente.

**Trade-off:** Perde granularidade, mas mantém a separação de responsabilidades.

**Quando usar:** Se o modelo de permissões não suportar vinculação por oferta.

---

### Blocker: Base ENEM Não Mapeada (US-06)

**Solução de contorno:** Implementar fluxo de pontuação declarada do zero, sem reaproveitamento da base ENEM.

**Trade-off:** Aumenta o effort de US-06 de 21.8h para ~30h, mas mantém o fluxo funcional.

**Quando usar:** Se não for possível reaproveitar a base ENEM.

---

## 6. Resumo do Cronograma (ATUALIZADO)

| Sprint | Período | Dias Úteis | USs Alocadas | Story Points | Capacidade Utilizada |
|--------|---------|------------|--------------|--------------|----------------------|
| Sprint 1 | 30/09 - 13/10 | 10 | US-01, US-05 | 4 SP | 21% |
| Sprint 2 | 14/10 - 27/10 | 10 | US-13, US-06 | 13 SP | 68% |
| Sprint 3 | 28/10 - 10/11 | 9 | US-07, US-08 | 18 SP | 79% |
| Sprint 4 | 11/11 - 24/11 | 9 | US-02, US-10, US-16, US-11 (parte) | 18 SP | 105% ⚠️ |
| Sprint 5 | 25/11 - 08/12 | 10 | US-11 (parte), US-09, US-03, US-04 | 18 SP | 79% |
| Sprint 6 | 09/12 - 22/12 | 10 | US-14, US-15, US-12 | 18 SP | 95% ⚠️ |
| **Total** | | **58** | **16 USs** | **84 SP** | **75% (média)** |

---

## 7. Ordem de Implementação Recomendada

1. **Sprint 1:** US-01 → US-05 (fundação — sem dependências)
2. **Sprint 2:** US-13 → US-06 (perfil analista e inscrição — depende de US-01, US-05)
3. **Sprint 3:** US-07 → US-08 (alteração e análise — depende de US-06, US-13)
4. **Sprint 4:** US-02 → US-10 → US-11 (parte 1) → US-16 (classificação e portal — depende de US-08)
5. **Sprint 5:** US-11 (parte 2) → US-09 → US-03 → US-04 (completar classificação e entrevista)
6. **Sprint 6:** US-14 → US-15 → US-12 (recurso e exportação — depende de US-11)

---

## 8. Comparação: Cronograma Original vs. Atualizado

| Aspecto | Original (3 devs) | Atualizado (2 devs) | Impacto |
|---------|-------------------|---------------------|---------|
| Capacidade/sprint | 78h | 52h | -33% |
| Duração total | 6 sprints | 6 sprints | Sem alteração |
| Utilização média | 52% | 75% | +23% |
| Sprints com sobrecarga | 0 | 2 (Sprint 4 e 6) | +2 sprints |
| US-08 (análise documental) | 35.5h (completa) | 23.4h (reduzida) | -34% escopo |
| Término estimado | Dezembro/2026 | Dezembro/2026 (ou Janeiro/2027 se estender) | Risco de atraso |

---

## 9. Recomendações

### Curto Prazo (Sprint 1-2)

1. **Validar modelo de permissões** antes do Sprint 2 (US-13)
2. **Mapear base ENEM** antes do Sprint 2 (US-06)
3. **Monitorar Dev 2** — está com 84% de utilização no Sprint 2

### Médio Prazo (Sprint 3-4)

4. **Decidir sobre visualizador PDF** — implementar completo ou solução de contorno?
5. **Preparar para sobrecarga** — Sprint 4 excede capacidade em 2.4h
6. **Considerar estender para 7 sprints** se qualidade estiver em risco

### Longo Prazo (Sprint 5-6)

7. **Avaliar retorno do Dev 3** — se voltar antes do Sprint 6, pode ajudar
8. **Planejar Sprint 7** se decidir estender o projeto
9. **Documentar soluções de contorno** para melhorias futuras

---

## 10. Opções Estratégicas

### Opção A: Manter 6 Sprints (Dezembro/2026)

**Prós:**
- Entrega no prazo estimado
- Mantém compromisso com stakeholders

**Contras:**
- Time sobrecarregado (Sprints 4 e 6)
- US-08 com escopo reduzido (sem visualizador PDF)
- Risco de qualidade comprometida

**Ações necessárias:**
- Reduzir escopo de US-08 (solução de contorno para PDF)
- Aceitar sobrecarga temporária nos Sprints 4 e 6

---

### Opção B: Estender para 7 Sprints (Janeiro/2027)

**Prós:**
- Time com carga sustentável
- US-08 completa (com visualizador PDF)
- Maior qualidade e menos risco

**Contras:**
- Adia entrega em 2 semanas
- Pode impactar planejamento de stakeholders

**Ações necessárias:**
- Comunicar stakeholders sobre extensão
- Mover US-12 para Sprint 7

---

### Opção C: Aumentar Horas Diárias (4h → 5h/dia)

**Prós:**
- Mantém prazo de 6 sprints
- Mantém escopo completo
- Capacidade aumenta para 65h/sprint

**Contras:**
- Time sobrecarregado (projeto paralelo + 5h/dia)
- Risco de burnout
- Sustentabilidade questionável

**Ações necessárias:**
- Obter acordo do time
- Monitorar saúde e produtividade

---

## 11. Próximos Passos

1. **Decidir estratégia** (Opção A, B ou C)
2. **Validar viabilidade técnica do visualizador PDF** antes do Sprint 3
3. **Validar modelo de permissões** antes do Sprint 2
4. **Mapear base ENEM** antes do Sprint 2
5. **Confirmar feriados de novembro** (02/11 e 20/11)
6. **Comunicar stakeholders** sobre mudança de capacidade e impacto no cronograma

---

*Gerado pela skill scheduling-prompt em 29/09/2026*
*Atualizado em 29/09/2026 — Dev 3 em licença médica*
*Baseado no template de Ahirton Lopes · PM AI Toolkit*
