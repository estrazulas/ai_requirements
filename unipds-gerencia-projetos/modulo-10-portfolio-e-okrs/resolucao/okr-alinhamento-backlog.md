# OKR Aligner - Alinhamento Estratégico de Backlog com OKRs
> **Projeto:** Sistema de Processos Seletivos Acadêmicos com Análise Documental
> **Data:** 2026-10-11
> **Módulo 10 - UNIPDS: Ferramentas de IA para Gestão de Projetos**

---

## Parte A: OKRs Validados

### Contexto

- **Empresa:** Instituição de ensino com processos seletivos acadêmicos
- **Stakeholder:** Setor Solicitante / Gestão Acadêmica
- **Ciclo:** Q1 2027 (janeiro a março de 2027)
- **Problema atual:** Análise documental feita manualmente fora do sistema; candidatos ligam/enviam emails para saber status
- **Baselines conhecidas:**
  - Tempo médio de análise: 30 dias
  - Chamados sobre status: 50/mês (ligações/emails)
  - Tempo para candidato ver resultado: 30 dias (publicação manual no site)
  - % editais processados digitalmente: 0% (todos manuais)

---

### Objetivo 1: Migrar análise documental do processo manual para o sistema

**Descrição:** Eliminar o processo manual de avaliação de documentos, migrando para fluxo 100% digital dentro do sistema.

| KR | Métrica | Baseline | Alvo | Status |
|---|---|---|---|---|
| KR 1.1 | % editais processados pelo sistema | 0% | 80% | A definir |
| KR 1.2 | Tempo médio de análise por candidato | 30 dias | 7 dias | A definir |

**Critérios de validação:**
- ✅ Mensurável (percentual e dias)
- ✅ Baseline declarada (0% e 30 dias)
- ✅ Prazo definido (março 2027)
- ✅ Responsável implícito (Setor Solicitante / TI)
- ✅ Independente de output (mede resultado de processo, não entrega de software)
- ✅ Verificável por terceiro (dados do sistema)

---

### Objetivo 2: Dar transparência ao candidato sobre avaliação e resultados

**Descrição:** Permitir que o candidato acompanhe em tempo real o status da análise, pontuação e resultados pelo portal, eliminando a necessidade de contato manual.

| KR | Métrica | Baseline | Alvo | Status |
|---|---|---|---|---|
| KR 2.1 | % candidatos que consultam o portal | 0% | 60% | A definir |
| KR 2.2 | Chamados (ligações/emails) sobre status | 50/mês | 0 | A definir |
| KR 2.3 | Tempo para candidato ver resultado após publicação | 30 dias | 1 dia | A definir |

**Critérios de validação:**
- ✅ Mensurável (percentual, contagem e dias)
- ✅ Baseline declarada (0%, 50/mês, 30 dias)
- ✅ Prazo definido (março 2027)
- ✅ Responsável implícito (TI / Setor Solicitante)
- ✅ Independente de output (mede comportamento do candidato e eficiência, não entrega)
- ✅ Verificável por terceiro (logs do portal, tickets de suporte)

---

## Parte B: Alinhamento Backlog × OKRs

### Input: Backlog de 16 User Stories

Fonte: `modulo-02-priorizacao-de-backlog/resolucao/analise-requisitos-analise-documental.md`

| ID | User Story | Épico |
|---|---|---|
| US-01 | Cadastrar critério AD no edital | E1 |
| US-02 | Configurar pesos de entrevista | E1 |
| US-03 | Cadastrar calendário por edital | E2 |
| US-04 | Cadastrar calendário por curso/oferta | E2 |
| US-05 | Configurar tipo de documento com pontuação | E3 |
| US-06 | Candidato declara pontuação | E3 |
| US-07 | Candidato altera documentos dentro do prazo | E3 |
| US-08 | Analista pontua documentos | E4 |
| US-09 | Analista pontua entrevista | E4 |
| US-10 | Analista desclassifica candidato | E4 |
| US-11 | Lista de classificação editável | E4 |
| US-12 | Exportar classificação CSV/HTML | E4 |
| US-13 | Perfil Analista de Documento | E6 |
| US-14 | Candidato interpõe recurso pelo portal | E5 |
| US-15 | Analista julga recurso | E5 |
| US-16 | Candidato visualiza status e pontuação | E5 |

---

### Tabela de Alinhamento

| Item | Status | Alinhamento | OKR Relacionado | Justificativa |
|---|---|---|---|---|
| US-01 Cadastrar critério AD no edital | ativo | **Alinhado Diretamente** | OKR 1 / KR 1.1 | Habilita o fluxo digital — sem isso, edital não usa o sistema |
| US-02 Configurar pesos de entrevista | ativo | **Alinhado Diretamente** | OKR 1 / KR 1.1 | Parte essencial do cálculo digital de pontuação |
| US-03 Calendário por edital | ativo | **Alinhado Indiretamente** | OKR 1 | Controla prazos mas não move KR diretamente — infra de processo |
| US-04 Calendário por curso/oferta | ativo | **Alinhado Indiretamente** | OKR 1 | Mesmo caso — viabiliza US-03 em contexto multi-oferta |
| US-05 Configurar tipo de documento com pontuação | ativo | **Alinhado Diretamente** | OKR 1 / KR 1.1 | Permite pontuação digital — sem isso, candidato não declara pontos |
| US-06 Candidato declara pontuação | ativo | **Alinhado Diretamente** | OKR 1 / KR 1.1 | Coração do fluxo digital — entrada de dados do candidato |
| US-07 Candidato altera documentos dentro do prazo | ativo | **Alinhado Indiretamente** | OKR 1 | Melhoria de UX mas não é essencial para KR 1.1 |
| US-08 Analista pontua documentos | ativo | **Alinhado Diretamente** | OKR 1 / KR 1.1 + KR 1.2 | Coração da análise digital + redução de tempo de 30→7 dias |
| US-09 Analista pontua entrevista | ativo | **Alinhado Diretamente** | OKR 1 / KR 1.1 | Completa o fluxo digital de pontuação |
| US-10 Analista desclassifica candidato | ativo | **Alinhado Indiretamente** | OKR 1 | Funcionalidade de eliminação mas não move KR diretamente |
| US-11 Lista de classificação editável | ativo | **Alinhado Indiretamente** | OKR 1 | Viabiliza classificação final mas não é essencial para KR 1.1 |
| US-12 Exportar classificação CSV/HTML | ativo | **Não Alinhado** | — | Automação de publicação externa — não move nenhum KR (publicação continua no site) |
| US-13 Perfil Analista de Documento | ativo | **Alinhado Indiretamente** | OKR 1 | Viabiliza US-08 (segurança/permissão) mas não move KR por si só |
| US-14 Candidato interpõe recurso pelo portal | ativo | **Alinhado Diretamente** | OKR 2 / KR 2.1 + KR 2.2 | Portal do candidato + redução de chamados (50→0) |
| US-15 Analista julga recurso | ativo | **Alinhado Indiretamente** | OKR 2 | Viabiliza US-14 mas não move KR diretamente |
| US-16 Candidato visualiza status e pontuação | ativo | **Alinhado Diretamente** | OKR 2 / KR 2.1 + KR 2.2 + KR 2.3 | Portal + transparência + redução de chamados + tempo 30→1 dia |

---

### Resumo de Distribuição

| Categoria | Quantidade | Percentual |
|---|---|---|
| Alinhados Diretamente | 8 | 50% |
| Alinhados Indiretamente | 6 | 37,5% |
| Não Alinhados | 1 | 6,25% |
| Épicos Futuros sem OKR | 0 | 0% |

**Capacidade estimada em itens Não Alinhados:** ~5 SP (US-12) de um total de ~85 SP — **6% da capacidade**

---

### Recomendações

#### 1. Itens Candidatos à Postergação

**US-12 (Exportar CSV/HTML)**
- **Status:** Não Alinhado
- **Argumento:** Não move nenhum KR do ciclo Q1 2027. Publicação externa no site institucional continua funcionando manualmente.
- **Recomendação:** Mover para Q2 2027 quando os OKRs de automação de publicação forem definidos.
- **Economia:** ~5 SP de capacidade liberada para itens alinhados.

#### 2. Alertas de Dependência

**Dependência crítica: US-13 → US-08**
- US-13 (perfil analista) é pré-requisito de segurança para US-08 (analista pontua documentos)
- **Ação:** Priorizar US-13 no início do ciclo para não bloquear US-08.

**Dependência de dados: US-14/US-16 → US-08/US-11**
- Portal do candidato (US-14, US-16) depende de dados gerados pela análise (US-08) e classificação (US-11)
- **Ação:** Garantir que US-08 e US-11 entrem em produção antes ou junto com US-14/US-16.

#### 3. Itens Críticos para KR 1.2 (Reduzir Tempo de 30→7 Dias)

**US-08 (Analista pontua documentos)**
- Maior impacto na redução de tempo — automatiza cálculo manual e elimina retrabalho
- **Prioridade:** Alta

**US-06 (Candidato declara pontuação)**
- Elimina retrabalho de digitação pelo analista — candidato já entra com dados estruturados
- **Prioridade:** Alta

#### 4. Itens Críticos para KR 2.2 (Reduzir Chamados de 50→0)

**US-16 (Candidato visualiza status e pontuação)**
- Maior impacto — portal com status em tempo real elimina necessidade de contato manual
- **Prioridade:** Alta

**US-14 (Candidato interpõe recurso pelo portal)**
- Complementa US-16 — candidato resolve tudo pelo portal sem precisar ligar
- **Prioridade:** Alta

---

### Mapa de Prioridades por Épico

| Épico | Descrição | Alinhamento | Prioridade |
|---|---|---|---|
| E1 | Configuração de Edital com AD | Direto (KR 1.1) | Alta |
| E3 | Inscrição com Pontuação Declarada | Direto (KR 1.1) | Alta |
| E4 | Análise e Classificação Documental | Direto (KR 1.1 + KR 1.2) | Alta |
| E5 | Recurso da Análise Documental | Direto (KR 2.1 + KR 2.2 + KR 2.3) | Alta |
| E6 | Perfil Analista de Documento | Indireto (viabiliza E4) | Média |
| E2 | Gestão de Calendários de Etapas | Indireto (infra de processo) | Média |

**Observação:** US-12 (E4) é o único item Não Alinhado — considerar postergar para Q2 2027.

---

### Próximos Passos

1. **Validar OKRs com stakeholder** — confirmar baselines e alvos
2. **Definir ordem de sprints** — priorizar épicos E1, E3, E4, E5 (alinhamento direto)
3. **Planejar dependências** — US-13 antes de US-08; US-08/US-11 antes de US-14/US-16
4. **Decidir sobre US-12** — postergar para Q2 2027 ou manter no ciclo?
5. **Definir métricas de acompanhamento** — como medir progresso dos KRs mensalmente?

---

*Documento gerado em 2026-10-11 como parte do Módulo 10 - Portfolio e OKRs*
*Prof. Ahirton Lopes, Ph.D. — UNIPDS: Ferramentas de IA para Gestão de Projetos*
