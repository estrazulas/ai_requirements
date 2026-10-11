# Fluxo do Bot: Do Prompt à Execução

Este documento explica como o bot implementado se relaciona com o prompt de parsing de linguagem natural.

## 1. O Prompt Original do Professor

O arquivo `nl-to-workflow-prompt.md` (do professor) é um **System Prompt** que ensina a IA a extrair informações estruturadas de mensagens em linguagem natural.

**Exemplo de entrada:**
```
"Preciso investigar por que os alertas de velocidade não estão chegando 
para os motoristas na região de Uberlândia."
```

**Saída esperada (JSON):**
```json
{
  "type": "bug",
  "title": "Falha no recebimento de alertas de velocidade em Uberlândia",
  "priority": "High",
  "component": "Alertas de Velocidade",
  "assignee": null,
  "description": "Investigar rastreadores Teltonika FMB920 e pacotes MQTT...",
  "confidence": "high"
}
```

## 2. Como Adaptei para o Nosso Contexto

No nosso bot (`ecosystem-bot-gitlab-glpi.py`), criei o `NL_PARSER_PROMPT` baseado no prompt do professor, mas adaptado para GLPI:

**Diferenças principais:**

| Aspecto | Professor (Jira) | Nosso Bot (GLPI) |
|---------|------------------|------------------|
| **Prioridades** | `Highest`, `High`, `Medium`, `Low` | `1` a `6` (numérico) |
| **Contexto** | RouteWise (frota, veículos) | Genérico (adaptável) |
| **Modelo** | Claude (claude-sonnet-4-6) | OpenAI ou Anthropic |
| **Integração** | Jira API | GLPI API |

## 3. Fluxo Completo no Código

```
┌─────────────────────────────────────────────────────────────┐
│ 1. ENTRADA (mensagem natural)                                │
│    "Preciso investigar bug no login OAuth"                   │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 2. MONTAGEM DO PROMPT                                        │
│    NL_PARSER_PROMPT.replace("{message}", mensagem)           │
│                                                              │
│    O prompt inclui:                                          │
│    - Instruções de como extrair informações                  │
│    - Definição dos campos (type, title, priority, etc)      │
│    - Regras de classificação (bug/task/feature/question)    │
│    - Casos especiais (perguntas, mensagens vagas)           │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 3. CHAMADA À IA                                              │
│    parse_natural_language(message)                           │
│    - Se AI_PROVIDER == "openai": usa OpenAI API             │
│    - Se AI_PROVIDER == "anthropic": usa Anthropic API       │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 4. SAÍDA (JSON estruturado)                                  │
│    {                                                         │
│      "type": "bug",                                          │
│      "title": "Investigar bug no login OAuth",              │
│      "priority": "2",                                        │
│      "assignee": null,                                       │
│      "description": "Investigar falha no fluxo...",         │
│      "confidence": "high"                                    │
│    }                                                         │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 5. EXECUÇÃO                                                  │
│    - Se confidence == "high" ou "medium": cria ticket GLPI  │
│    - Se type == "question": não cria, apenas sugere         │
│    - Se confidence == "low": pede revisão humana            │
└─────────────────────────────────────────────────────────────┘
```

## 4. Exemplo Prático

**Comando:**
```bash
python ecosystem-bot-gitlab-glpi.py --parse "Carlos pediu para antecipar o módulo de relatórios para antes do fim do mês. Alguém pode pegar isso?"
```

**O que acontece internamente:**

### Passo 1: Monta o prompt

```python
prompt = NL_PARSER_PROMPT.replace("{message}", "Carlos pediu para antecipar...")
```

O prompt é uma string com placeholders que são preenchidos com a mensagem do usuário.

### Passo 2: Envia para a IA

```python
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)
```

A IA recebe o prompt completo e retorna um JSON estruturado.

### Passo 3: Extrai JSON da resposta

```python
json_match = re.search(r'\{[\s\S]*\}', text)
parsed = json.loads(json_match.group(0))
```

O código extrai o JSON da resposta (a IA pode adicionar texto explicativo ao redor do JSON).

### Passo 4: Resultado

```json
{
  "type": "feature",
  "title": "Antecipar módulo de relatórios",
  "priority": "2",
  "assignee": "[A DEFINIR]",
  "dueDate": "[fim do mês corrente]",
  "requestedBy": "Carlos",
  "actionRequired": "Confirmar assignee antes de criar ticket",
  "confidence": "high"
}
```

## 5. Por que o Prompt é Importante?

O prompt é o **cérebro** do parser. Ele define:

- **O que extrair:** type, title, priority, assignee, dueDate, etc
- **Como classificar:** bug vs task vs feature vs question
- **Como inferir:** datas relativas ("fim do mês"), prioridades implícitas
- **Casos especiais:** perguntas, mensagens vagas, múltiplas ações

Sem o prompt, a IA não saberia como estruturar a resposta. O prompt transforma uma mensagem livre em dados estruturados prontos para criar tickets.

## 6. Comparação com o Bot do Professor

| Componente | Professor | Nosso Bot |
|------------|-----------|-----------|
| **Prompt** | `nl-to-workflow-prompt.md` | `NL_PARSER_PROMPT` (adaptado) |
| **Parser** | `parseNaturalLanguage()` | `parse_natural_language()` |
| **Executor** | `createJiraCard()` | `glpi.create_ticket()` |
| **Listener** | Slack (`app.message()`) | Flask (`/webhook/chat`) |
| **Confirmação** | Sim (no Slack) | Não (automático) |

A lógica é a mesma, mudam apenas as ferramentas (Jira → GLPI, Slack → HTTP webhook).

## 7. Estrutura do Código

### Arquivos principais

```
resolucao/
├── ecosystem-bot-gitlab-glpi.py    # Bot principal
│   ├── NL_PARSER_PROMPT            # Prompt de parsing (adaptado do professor)
│   ├── parse_natural_language()    # Função que chama a IA
│   ├── EcosystemBot                # Classe principal do bot
│   │   ├── handle_mr_event()       # Fluxo 1: MR → ticket
│   │   └── handle_ticket_event()   # Fluxo 2: ticket → MR
│   └── run_webhook_server()        # Servidor Flask com endpoints
├── nl-to-workflow-prompt.md        # Prompt original do professor (referência)
└── README.md                        # Documentação completa
```

### Funções principais

```python
# Parser de linguagem natural
def parse_natural_language(message: str) -> dict:
    """
    Converte mensagem em linguagem natural em JSON estruturado.
    Usa o prompt NL_PARSER_PROMPT para guiar a IA.
    """
    prompt = NL_PARSER_PROMPT.replace("{message}", message)
    # ... chama OpenAI ou Anthropic ...
    return json.loads(response)

# Executor (cria ticket no GLPI)
def create_ticket(self, title, description, category_id=None, status=1):
    """
    Cria ticket no GLPI usando a API REST.
    """
    # ... chama GLPI API ...
    return response.json()

# Listener (webhook)
@app.route("/webhook/chat", methods=["POST"])
def chat_webhook():
    """
    Recebe mensagens em linguagem natural e cria tickets.
    """
    message = request.json.get("message")
    parsed = parse_natural_language(message)
    ticket = bot.glpi.create_ticket(...)
    return jsonify({"status": "ok", "ticket_id": ticket["id"]})
```

## 8. Resumo

O bot implementado segue a mesma arquitetura do bot do professor:

1. **Listener** recebe mensagem (webhook ou CLI)
2. **Parser** usa IA para extrair informações estruturadas
3. **Executor** cria ticket no GLPI
4. **Notificação** retorna resultado ao usuário

A principal diferença é que adaptamos para o contexto IFSC:
- GitLab em vez de GitHub
- GLPI em vez de Jira
- Prompt adaptado para prioridade numérica (1-6)
- Servidor Flask em vez de Slack Bot

O prompt é a peça central: sem ele, a IA não saberia como estruturar a resposta. O prompt transforma linguagem natural em dados estruturados prontos para automação.
