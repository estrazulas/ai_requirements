# Meeting Digest Skill

Skill interativa para gerar atas estruturadas a partir de transcrições de reunião.

---

## Quando Usar

### Reuniões de Projeto

- **Sprint Review** — revisar entregas da sprint, coletar feedback de stakeholders, ajustar backlog
- **Sprint Planning** — decidir quais itens entram na sprint, alinhar capacidade e dependências
- **Sprint Retrospective** — refletir sobre o que funcionou, o que melhorar, ações de melhoria
- **Backlog Refinement/Grooming** — detalhar user stories, esclarecer critérios de aceite, estimar esforço
- **Discovery de Requisitos** — levantar necessidades com stakeholders, definir escopo de features
- **Reunião de Riscos** — identificar e avaliar riscos, definir planos de contingência
- **Kickoff de Projeto** — alinhar escopo, cronograma, papéis e expectativas com o time e cliente
- **Reunião com Cliente/Stakeholder** — apresentar progresso, negociar prioridades, coletar decisões

### Contextos Específicos

- **Mudança de Escopo** — quando surgem novos pedidos durante o projeto (ex: feature que havia sido cortada precisa voltar)
- **Dependências Externas** — quando há bloqueios por fornecedores, hardware, APIs de terceiros
- **Decisões Técnicas** — quando o time decide abordagens de implementação que afetam o projeto
- **Alinhamento Cross-Team** — quando múltiplos times precisam coordenar entregas

---

## O Que a Skill Gera

### 1. Resumo Executivo
4-6 bullets com decisões, alinhamentos e blockers — legível por qualquer stakeholder.

### 2. Tabela de Ações
| ID | Ação | Responsável | Prazo | Prioridade | Observação |

### 3. Decisões Registradas
Decisões explícitas e implícitas com contexto e impacto.

### 4. Perguntas em Aberto
Itens não resolvidos, quem deve responder, se são blockers.

### 5. JSON para Jira
Cards prontos para importação com title, assignee, priority, dueDate, description.

---

## Como a Skill Funciona

1. **Pergunta** se você tem arquivo ou texto da transcrição
2. **Coleta** contexto: tipo de reunião, data, duração, participantes, projeto
3. **Explora** repositório/backlog se você indicar um projeto (para enriquecer contexto técnico)
4. **Processa** a transcrição seguindo regras rigorosas (nunca inventa responsável, sinaliza erros, marca decisões implícitas)
5. **Gera** arquivo `ata-[tipo]-[data].md` com a ata completa

---

## Exemplos de Uso

### Exemplo 1: Sprint Review
```
Contexto: Reunião de revisão da Sprint 2 do projeto RouteWise
Transcrição: 20 min, 3 participantes (Tech Lead, Diretor, RH)
Output: 5 ações, 4 decisões (incluindo 1 implícita), 1 pergunta em aberto, 4 cards Jira
```

### Exemplo 2: Discovery de Requisitos
```
Contexto: Levantamento de requisitos para nova feature de dashboard
Transcrição: 35 min, 3 participantes (Consultor, Diretor de Operações, TI/Infra)
Output: decisões de escopo, ações de investigação técnica, dependências identificadas
```

### Exemplo 3: Reunião de Riscos
```
Contexto: Avaliação de riscos do projeto Análise Documental
Transcrição: 45 min, 4 participantes (PM, Tech Lead, QA, Stakeholder)
Output: riscos priorizados, planos de mitigação, responsáveis por acompanhamento
```

---

## Diferenciais da Skill

- **Interativa** — não precisa ter tudo pronto, a skill pergunta o que falta
- **Enriquecimento com contexto** — se você indicar um projeto/repositorio, a skill explora o código para entender termos técnicos
- **Regras rigorosas** — nunca inventa responsável, sinaliza decisões implícitas, trata ações de acompanhamento separadamente
- **Output acionável** — gera JSON pronto para Jira, não apenas texto

---

## Limitações

- A qualidade do output depende da qualidade da transcrição
- Transcrições automáticas (Whisper, Otter, etc.) podem ter erros — a skill sinaliza mas não corrige
- Decisões não verbais (linguagem corporal, tom) não são capturadas
- A skill não substitui revisão humana — sempre revise antes de distribuir

---

*Skill criada em 02/10/2026*
*Baseada no Meeting Digest Prompt do Prof. Ahirton Lopes — Módulo 6.2*
