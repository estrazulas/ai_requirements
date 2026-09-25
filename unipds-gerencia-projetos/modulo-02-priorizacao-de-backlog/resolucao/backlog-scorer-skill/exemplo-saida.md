# Exemplo de Saída — Estrutura de Resultados

Este arquivo mostra a estrutura de diretórios com os resultados gerados após a execução da skill de priorização de backlog.

---

## Estrutura de Diretórios

```
modulo-02-priorizacao-de-backlog/
└── resolucao/
    ├── backlog-scorer-skill/
    │   ├── backlog-scorer-skill.md          # Skill de priorização (RICE + WSJF)
    │   └── README.md                         # Guia de uso da skill
    │
    ├── analise-requisitos-analise-documental.md   # Documento de requisitos (input)
    │
    ├── sprint-0-resumo-consolidado.md       # Resumo consolidado de todas as sprints
    ├── sprint-1-2-must-have.md              # Sprints 1-2: User Stories classificadas como Must
    ├── sprint-3-4-should-have.md            # Sprints 3-4: User Stories classificadas como Should
    └── sprint-5-could-have.md               # Sprint 5: User Stories classificadas como Could
```

---

## Descrição dos Arquivos de Saída

### sprint-0-resumo-consolidado.md
Visão geral consolidada de todas as sprints, contendo:
- Ranking final das User Stories (RICE + WSJF)
- Distribuição por categoria MoSCoW
- Total de story points por sprint
- Flags e riscos identificados
- Recomendações de execução

### sprint-1-2-must-have.md
Contém as User Stories classificadas como **Must have**:
- USs essenciais para o MVP (sem elas o projeto falha)
- Prioridade máxima de implementação
- Story points e esforço estimado
- Dependências e critérios de aceite

### sprint-3-4-should-have.md
Contém as User Stories classificadas como **Should have**:
- USs importantes mas não críticas (existe workaround)
- Implementadas após as Must
- Story points e esforço estimado
- Dependências e critérios de aceite

### sprint-5-could-have.md
Contém as User Stories classificadas como **Could have**:
- USs desejáveis (podem ser adiadas ou feitas manualmente)
- Implementadas apenas se houver capacidade
- Story points e esforço estimado
- Dependências e critérios de aceite

---

## Fluxo de Geração

1. **Input:** Documento de requisitos (`analise-requisitos-analise-documental.md`)
2. **Skill:** Executa filtragem MoSCoW + cálculo RICE/WSJF
3. **Output:** Arquivos de sprint organizados por prioridade

---

## Como Usar

```bash
# 1. Execute a skill
Use a skill backlog-scorer-skill

# 2. Informe os dados solicitados (OKR, perfil, restrições, USs)

# 3. A skill vai:
#    - Classificar cada US pelo MoSCoW
#    - Calcular RICE/WSJF para Must + Should
#    - Gerar ranking combinado

# 4. Os resultados serão organizados nos arquivos de sprint
```

---

*Gerado automaticamente pela skill backlog-scorer-skill*
