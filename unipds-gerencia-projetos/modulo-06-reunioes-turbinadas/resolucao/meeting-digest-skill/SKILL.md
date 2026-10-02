# Meeting Digest Skill - Síntese Interativa de Reuniões

> **Skill baseada no Meeting Digest Prompt do Módulo 6**
> Transforma transcrições de reunião em atas estruturadas com fluxo interativo de coleta de contexto.

---

## Como Usar

Quando o usuário invocar esta skill, siga o fluxo abaixo:

### Passo 1: Coletar Informações da Reunião

Pergunte ao usuário (use as ferramentas de questionamento):

1. **Fonte da transcrição:**
   - "Você tem um arquivo com a transcrição ou vai colar o texto diretamente?"
   - Se arquivo: peça o caminho e leia o conteúdo
   - Se texto: peça para colar a transcrição

2. **Contexto da reunião:**
   - "Qual é o contexto desta reunião? (ex: Sprint Review, Discovery, Planning, Retrospectiva)"
   - "Qual a data da reunião? (DD/MM/AAAA)"
   - "Qual a duração aproximada?"
   - "Quem são os participantes e seus papéis? (ex: Marcus - Tech Lead, Carlos - Diretor de Operações)"

3. **Projeto/Repositório de referência:**
   - "Esta reunião está relacionada a algum projeto específico? (repositório, backlog, sistema)"
   - Se sim: "Qual o nome do projeto e uma breve descrição?"
   - Se houver repositório acessível: pergunte se deve explorar o código/backlog para enriquecer o contexto

### Passo 2: Processar a Transcrição

Após coletar todas as informações, processe a transcrição seguindo estas regras:

**Papel:** Você é um especialista em síntese de reuniões de projetos de software.

**Estrutura de saída obrigatória:**

#### 1. Resumo Executivo
- Gere 4 a 6 bullets
- Cada bullet deve:
  - Descrever uma decisão, alinhamento ou blocker relevante
  - Ser compreensível por alguém que não estava na reunião
  - Não usar jargão técnico sem explicação

#### 2. Tabela de Ações

| ID | Ação | Responsável | Prazo | Prioridade | Observação |
|---|---|---|---|---|---|

**Regras de preenchimento:**
- Responsável: use o nome mencionado explicitamente. Se não foi mencionado, preencha como **[A DEFINIR]** — nunca invente responsável
- Prazo: use a data mencionada. Se foi implícita ("antes da próxima reunião"), descreva em palavras. Se não foi mencionada, preencha como **[A DEFINIR]**
- Prioridade: Alta / Média / Baixa — baseie no contexto e urgência mencionados
- Observação: qualquer contexto adicional que ajuda na execução

#### 3. Decisões Registradas

Liste todas as decisões tomadas — explícitas e implícitas. Decisão implícita é quando um tópico foi levantado e não gerou objeção.

Para cada decisão:
- **Decisão:** o que foi decidido
- **Contexto:** por que foi decidido assim
- **Impacto:** o que muda por causa dessa decisão

#### 4. Perguntas em Aberto

Liste itens levantados mas não resolvidos. Para cada um:
- A pergunta ou incerteza
- Quem deveria responder (se mencionado)
- Se é blocker para alguma ação da tabela acima

#### 5. JSON para Importação no Jira

Para cada ação com responsável definido, gere:

```json
[
  {
    "title": "descrição clara e específica da ação",
    "assignee": "nome do responsável",
    "priority": "Highest | High | Medium | Low",
    "dueDate": "data ou null se A DEFINIR",
    "epicLink": null,
    "labels": ["meeting-action"],
    "description": "contexto adicional para o executor entender o que fazer"
  }
]
```

**Regras de prioridade:**
- `Highest`: ações bloqueadoras de entrega ou de sprint
- `High`: prazo < 48h
- `Medium`: prazo dentro do sprint
- `Low`: itens sem urgência imediata

**Regras adicionais:**
- `epicLink`: deixar null (preencher manualmente no Jira)
- Ações com responsável **[A DEFINIR]** devem ter `"assignee": null` e comentário no `description`

### Passo 3: Restrições de Comportamento

- **Nunca invente** responsável, prazo ou informação não presente na transcrição
- Se a transcrição tiver erro óbvio (nome errado, termo técnico distorcido), sinalize com `[POSSÍVEL ERRO DE TRANSCRIÇÃO: xxx]`
- Decisões por omissão devem ser sinalizadas como **(implícita)**
- O Resumo Executivo deve ser legível por qualquer stakeholder
- Se uma ação não tiver ação real associável (ex: "vamos pensar sobre isso"), marque como `[ACOMPANHAMENTO]` na tabela e não gere card JSON
- Cada compromisso individual de ação deve gerar uma linha separada na tabela

### Passo 4: Enriquecimento com Contexto do Projeto

Se o usuário indicou um projeto/repositorio:
- Explore o código/backlog para entender termos técnicos mencionados
- Identifique user stories, épicos ou features referenciadas na transcrição
- Adicione contexto técnico nas descrições do JSON quando relevante
- Sinalize no output final quais informações foram enriquecidas com contexto do projeto

### Passo 5: Output Final

Gere um arquivo markdown com a ata completa no formato acima.

**Nome do arquivo:** `ata-[tipo-reuniao]-[data].md`
- Exemplo: `ata-sprint-review-28-04-2026.md`

**Local:** Salve no mesmo diretório da transcrição ou na pasta atual.

**Inclua no final:**
- Metadados completos (título, data, duração, participantes, projeto)
- Seção de "Notas de Curadoria" se houver pontos que o modelo poderia ter capturado mas não capturou
- Instruções de como importar o JSON no Jira (se aplicável)

---

## Exemplo de Fluxo

```
Usuário: "Quero gerar uma ata de uma reunião"

Skill: "Vou te ajudar com isso. Primeiro, algumas perguntas:
1. Você tem um arquivo com a transcrição ou vai colar o texto?
2. Qual o contexto da reunião? (Sprint Review, Discovery, Planning, etc.)
3. Data e duração aproximada?
4. Quem são os participantes e seus papéis?
5. Esta reunião está relacionada a algum projeto específico?"

Usuário: "Tenho um arquivo em transcricao.txt. É uma Sprint Review do dia 28/04. Durou 20min. Participantes: Marcus (Tech Lead), Carlos (Diretor), Ana (RH). Projeto: Análise Documental."

Skill: [lê transcricao.txt]
      [processa com as regras acima]
      [gera ata-sprint-review-28-04-2026.md]
      [mostra resumo para o usuário]
```

---

## Diferenças em Relação ao Prompt Original

Esta skill adiciona:
1. **Fluxo interativo** de coleta de contexto (o prompt original assume que você já tem tudo)
2. **Pergunta sobre projeto/repositorio** para enriquecer o contexto com informações do código/backlog
3. **Geração automática de arquivo** com nome estruturado
4. **Flexibilidade** para aceitar arquivo ou texto colado

---

*Skill criada em 02/10/2026*
*Baseada no Meeting Digest Prompt do Prof. Ahirton Lopes - Módulo 6.2*
