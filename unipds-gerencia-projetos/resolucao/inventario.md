# Inventário de Artefatos — UNIPDS: Ferramentas de IA para Gestão de Projetos
> **Estudante:** Estrazulas
> **Período:** 2026
> **Prof. Ahirton Lopes, Ph.D.**

---

## Módulo 1: Planejamento e Escopo

**Análise Documental de Requisitos**
Utilizei o Requirements Copilot para extrair requisitos de um documento de processo seletivo acadêmico com análise documental. O output foi uma análise completa com 16 user stories organizadas em 6 épicos, incluindo critérios de aceite em Gherkin, flags de risco (especificação inventada, dependência não mapeada, gold plating), e perguntas em aberto para validação com stakeholder. O arquivo CSV de import para Jira foi gerado automaticamente a partir da análise.

---

## Módulo 2: Priorização de Backlog

**Backlog Scorer com RICE e WSJF**
Criei uma skill personalizada (backlog-scorer-skill) que aplica dois frameworks de priorização: RICE Score (Reach, Impact, Confidence, Effort) e WSJF (Weighted Shortest Job First). O output consolidou 16 user stories com pontuações, ranking combinado, e justificativas para cada decisão. As user stories foram classificadas em sprints (0-5) segundo prioridade MoSCoW (Must Have, Should Have, Could Have), com contexto de projeto consolidado incluindo OKRs e restrições conhecidas.

---

## Módulo 3: Cronograma e Capacidade

**Cronograma de Sprints com Alocação de Capacidade**
Construí um cronograma detalhado de sprints considerando capacidade do time (6 devs, 35 SP/sprint), dependências entre user stories, e restrições de hardware (lead time de 60 dias para sensores IoT). O cronograma foi atualizado para refletir ajustes de capacidade e priorização, com visão de entrega por sprint e marcos do projeto.

> **Pendente:** Aplicar o Scheduling Prompt com os dados do meu projeto de processos seletivos acadêmicos (16 user stories, 6 épicos, dependências entre US-01→US-06→US-08, validador PDF pendente). O output esperado é um cronograma próprio com alocação de capacidade por sprint, identificação de caminho crítico, e ajustes baseados em restrições de dependência e capacidade.

---

## Módulo 4: Estimativas e Previsões

**Estimativas Probabilísticas com Monte Carlo**
Apliquei técnica de estimativa de três pontos (otimista, mais provável, pessimista) para cada user story, gerando distribuições probabilísticas. Executei simulação de Monte Carlo para prever datas de entrega com níveis de confiança (50%, 80%, 95%). O output incluiu análise de risco de cronograma e recomendações de buffer baseadas em dados probabilísticos, não em estimativas determinísticas.

---

## Módulo 5: Riscos e AIOps

**Registro de Riscos com Mitigação Automatizada**
Construí um registro de riscos do projeto com classificação (probabilidade × impacto), planos de mitigação, e donos para cada risco. Integrei conceitos de AIOps para monitoramento proativo de riscos em produção, incluindo alertas automatizados e respostas programadas a cenários de risco materializados.

> **Pendente:** Aplicar o Risk Monitor Prompt com os dados do meu projeto de processos seletivos acadêmicos. O output esperado é um registro de riscos estruturado com: (1) tabela de riscos classificados por probabilidade × impacto, (2) planos de mitigação com donos, (3) gatilhos de alerta para riscos materializados, (4) integração com AIOps para monitoramento contínuo. Riscos específicos do meu projeto: visualizador PDF (viabilidade técnica), modelo de permissões (vinculação granular), base ENEM (reaproveitamento não documentado), formato de relatórios (pendente de referência).

---

## Módulo 6: Reuniões Turbinadas

**Meeting Digest Skill para Síntese de Reuniões**
Criei uma skill (meeting-digest-skill) que transforma transcrições de reuniões em digests estruturados com decisões tomadas, ações definidas (com dono e prazo), riscos identificados, e perguntas em aberto. O output é formatado para consumo assíncrono, eliminando necessidade de atas manuais e garantindo que todas as ações tenham rastreabilidade.

> **Pendente:** Aplicar o Meeting Digest Prompt em uma transcrição real de reunião do meu projeto de processos seletivos acadêmicos. O output esperado é um digest estruturado com: (1) decisões tomadas, (2) ações definidas com dono e prazo, (3) riscos identificados, (4) perguntas em aberto para stakeholder, (5) resumo executivo para comunicação assíncrona. Pode usar a transcrição da sprint review do RouteWise como exemplo ou criar uma transcrição fictícia de reunião de refinamento do meu projeto.

---

## Módulo 7: Status Reports

**Status Reports Automatizados**
Gerei status reports estruturados com métricas de velocity, lead time, progresso de sprint, e saúde do projeto. Os reports incluem visualização de blockers, dependências críticas, e recomendações de ação para próxima sprint. O formato é otimizado para comunicação executiva (1 página) e detalhamento técnico (appendix com métricas).

> **Pendente:** Aplicar o Status Report Prompt com os dados do meu projeto de processos seletivos acadêmicos. O output esperado é um status report estruturado com: (1) resumo executivo (1 página) com saúde do projeto, (2) métricas de velocity e lead time, (3) progresso de sprint atual, (4) blockers e dependências críticas, (5) recomendações de ação para próxima sprint, (6) appendix técnico com métricas detalhadas. Pode usar o jira-estado-board do RouteWise como exemplo ou criar um snapshot fictício do board do meu projeto.

---

## Módulo 8: Governança e Compliance

**Checklists de Compliance e Simulação de Auditoria**
Desenvolvi checklists de compliance (LGPD, segurança, acessibilidade) aplicáveis ao projeto. Executei uma simulação de auditoria onde o modelo atuou como auditor externo, identificando gaps de compliance, riscos regulatórios, e recomendações de mitigação. O output incluiu explicação detalhada de cada item do checklist e como aplicar no contexto específico do projeto.

---

## Módulo 9: Automação de Ecossistema

**Fluxo de Automação com Múltiplos Agentes**
Construí um fluxo de automação que orquestra múltiplos agentes de IA (Hugging Face, modelos locais) para executar tarefas sequenciais: transcrição de áudio, extração de requisitos, priorização de backlog, e geração de artifacts. O fluxo inclui auditoria de cada etapa, logs de execução, e guia de simulação para teste end-to-end. A arquitetura é extensível para integração com novas ferramentas e APIs.

---

## Módulo 10: Portfolio e OKRs

**OKR Aligner: Alinhamento Estratégico de Backlog com OKRs**
Apliquei o framework OKR Aligner em 3 partes: (A) validei OKRs do projeto com baselines, métricas e prazos mensuráveis; (B) classifiquei 16 user stories segundo alinhamento com OKRs (8 Diretamente Alinhadas, 6 Indiretamente, 1 Não Alinhada, 0 Épicos Futuros); (C) documentei scorecard de portfólio multi-projeto com rúbrica de semáforo (🟢🟡🔴). O output incluiu recomendações de postergação (US-12), alertas de dependência crítica (US-13 → US-08), e identificação de itens de alta alavancagem (US-08 e US-16 movem múltiplos KRs). A curadoria destacou convergência de frameworks (OKR Aligner + WSJF) como argumento defensável para decisões de priorização.

---

## Skills Personalizadas Criadas

**Requirements Copilot (Módulo 1)**
Skill para extração estruturada de requisitos a partir de documentos, gerando user stories com critérios de aceite em Gherkin, flags de risco, e perguntas para stakeholder.

**Backlog Scorer (Módulo 2)**
Skill para priorização de backlog usando RICE Score e WSJF, com output consolidado incluindo ranking, justificativas, e classificação por sprint.

**Meeting Digest (Módulo 6)**
Skill para síntese de reuniões, transformando transcrições em digests estruturados com decisões, ações, riscos e perguntas em aberto.

---

## Artefatos Transversais

**Contexto de Projeto Consolidado**
Documento mestre com contexto do projeto (empresa, stakeholder, OKRs, restrições, time), usado como input para todos os módulos. Garante consistência de dados entre diferentes artifacts e simulações.

**Jira State Board**
Snapshot do estado do board no Jira em diferentes momentos do projeto, usado para rastrear evolução de user stories e validar que artifacts gerados estão alinhados com execução real.

---

*Inventário gerado em 2026-10-11*
*Total de módulos: 10 | Skills criadas: 3 | Artefatos principais: 15+*
