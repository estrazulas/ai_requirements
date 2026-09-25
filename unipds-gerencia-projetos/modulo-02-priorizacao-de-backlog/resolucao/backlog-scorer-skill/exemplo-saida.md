# Exemplo de Saída — Estrutura de Resultados

Este arquivo mostra a estrutura de diretórios com os resultados gerados após a execução da skill de priorização de backlog.

---

## Estrutura de Diretórios Gerados

A skill gera os seguintes arquivos no diretório `pontuacoes/` na raiz do projeto:

```
[NOME DO PROJETO]/
├── pontuacoes/
│   ├── contexto-projeto.md              # Contexto da equipe (persistido)
│   ├── sprint-0-resumo-consolidado.md   # Resumo consolidado de todas as sprints
│   ├── sprint-1-2-must-have.md          # User Stories classificadas como Must
│   ├── sprint-3-4-should-have.md        # User Stories classificadas como Should
│   └── sprint-5-could-have.md           # User Stories classificadas como Could
└── [outros arquivos do projeto]
```

**Exemplo real (projeto unipds-gerencia-projetos):**

```
unipds-gerencia-projetos/
├── modulo-01-planejamento-e-escopo/
├── modulo-02-priorizacao-de-backlog/
│   └── resolucao/
│       ├── backlog-scorer-skill/
│       │   ├── backlog-scorer-skill.md
│       │   ├── README.md
│       │   ├── exemplo-contexto-projeto.md
│       │   └── exemplo-saida.md
│       └── analise-requisitos-analise-documental.md
└── pontuacoes/                          # ← Gerado pela skill
    ├── contexto-projeto.md
    ├── sprint-0-resumo-consolidado.md
    ├── sprint-1-2-must-have.md
    ├── sprint-3-4-should-have.md
    └── sprint-5-could-have.md
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

1. **Input:** Documento de requisitos (ex: `analise-requisitos-analise-documental.md`)
2. **Skill:** Executa filtragem MoSCoW + cálculo RICE/WSJF
3. **Output:** Arquivos gerados no diretório `pontuacoes/` na raiz do projeto

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

# 4. Os resultados serão organizados no diretório pontuacoes/
```

---

*Gerado automaticamente pela skill backlog-scorer-skill*
