# Sistema de Auditoria do Bot

O bot implementa um sistema de auditoria completo para rastrear a criação de tickets e sincronizações MR ↔ ticket.

## O que é registrado

### 1. Criação de Ticket via NL Parser

Quando um ticket é criado a partir de uma mensagem em linguagem natural, o bot registra:

```json
{
  "timestamp": "2026-03-15T14:30:45.123456Z",
  "event": "ticket_created",
  "prompt_version": "1.0.0",
  "prompt_hash": "a1b2c3d4e5f6",
  "ai_provider": "openai",
  "ai_model": "gpt-4o-mini",
  "message_id": "msg_123456",
  "channel": "#geral",
  "user_id": "user_789",
  "original_message": "Preciso investigar bug no login OAuth",
  "parsed_output": {
    "type": "bug",
    "title": "Investigar bug no login OAuth",
    "priority": "2",
    "assignee": null,
    "description": "Investigar falha no fluxo de login OAuth...",
    "confidence": "high"
  },
  "ticket_id": 5678,
  "confidence": "high",
  "ticket_type": "bug",
  "priority": "2",
  "assignee": null
}
```

### 2. Sincronização MR ↔ Ticket

Quando um MR é sincronizado com um ticket (criação ou atualização), o bot registra:

```json
{
  "timestamp": "2026-03-15T14:35:12.654321Z",
  "event": "mr_sync",
  "action": "mr_to_ticket",
  "mr_iid": 42,
  "ticket_id": 5678
}
```

## Campos de Auditoria

| Campo | Descrição | Exemplo |
|-------|-----------|---------|
| `timestamp` | Data/hora UTC da criação | `2026-03-15T14:30:45.123456Z` |
| `event` | Tipo de evento | `ticket_created` ou `mr_sync` |
| `prompt_version` | Versão do NL_PARSER_PROMPT | `1.0.0` |
| `prompt_hash` | Hash MD5 do prompt (12 chars) | `a1b2c3d4e5f6` |
| `ai_provider` | Provedor de IA usado | `openai` ou `anthropic` |
| `ai_model` | Modelo específico | `gpt-4o-mini` |
| `message_id` | ID da mensagem original (se disponível) | `msg_123456` |
| `channel` | Canal de origem (Slack, Teams, etc) | `#geral` |
| `user_id` | ID do usuário que enviou a mensagem | `user_789` |
| `original_message` | Mensagem original em linguagem natural | `"Preciso investigar bug..."` |
| `parsed_output` | JSON completo retornado pela IA | `{...}` |
| `ticket_id` | ID do ticket criado no GLPI | `5678` |
| `confidence` | Nível de confiança do parser | `high`, `medium`, `low` |
| `ticket_type` | Tipo do ticket | `bug`, `task`, `feature`, etc |
| `priority` | Prioridade do ticket | `1` a `6` |
| `assignee` | Assignee definido | `null` ou nome |

## Como consultar logs

### 1. Via API (endpoint /audit)

**Listar últimos 10 logs:**

```bash
curl http://localhost:5000/audit?limit=10
```

**Resposta:**

```json
{
  "status": "ok",
  "count": 10,
  "logs": [
    {
      "timestamp": "2026-03-15T14:30:45.123456Z",
      "event": "ticket_created",
      "ticket_id": 5678,
      "original_message": "Preciso investigar bug no login OAuth",
      "parsed_output": {...},
      ...
    },
    ...
  ]
}
```

**Buscar log de um ticket específico:**

```bash
curl http://localhost:5000/audit?ticket_id=5678
```

**Resposta:**

```json
{
  "status": "ok",
  "found": true,
  "log": {
    "timestamp": "2026-03-15T14:30:45.123456Z",
    "event": "ticket_created",
    "ticket_id": 5678,
    "original_message": "Preciso investigar bug no login OAuth",
    "parsed_output": {...},
    "prompt_version": "1.0.0",
    "prompt_hash": "a1b2c3d4e5f6",
    ...
  }
}
```

**Filtrar por tipo de evento:**

```bash
# Apenas tickets criados
curl http://localhost:5000/audit?event_type=ticket_created

# Apenas sincronizações MR
curl http://localhost:5000/audit?event_type=mr_sync
```

### 2. Via arquivo de log

Os logs são armazenados em `audit_log.jsonl` (uma linha por evento):

```bash
# Ver últimos 5 logs
tail -n 5 audit_log.jsonl

# Buscar logs de um ticket específico
grep '"ticket_id": 5678' audit_log.jsonl

# Contar tickets criados por dia
grep '"event": "ticket_created"' audit_log.jsonl | \
  jq -r '.timestamp' | cut -d'T' -f1 | sort | uniq -c
```

## Exemplo de uso: "Como esse card foi criado?"

Se alguém perguntar "Como o ticket #5678 foi criado?", você pode consultar:

```bash
curl http://localhost:5000/audit?ticket_id=5678
```

O bot retorna:

```json
{
  "status": "ok",
  "found": true,
  "log": {
    "timestamp": "2026-03-15T14:30:45.123456Z",
    "event": "ticket_created",
    "prompt_version": "1.0.0",
    "prompt_hash": "a1b2c3d4e5f6",
    "ai_provider": "openai",
    "ai_model": "gpt-4o-mini",
    "channel": "#geral",
    "user_id": "joao.silva",
    "original_message": "Preciso investigar bug no login OAuth",
    "parsed_output": {
      "type": "bug",
      "title": "Investigar bug no login OAuth",
      "priority": "2",
      "assignee": null,
      "confidence": "high"
    },
    "ticket_id": 5678,
    "confidence": "high",
    "ticket_type": "bug"
  }
}
```

**Interpretação:**

- **Quando:** 15/03/2026 às 14:30:45 UTC
- **Quem:** joao.silva no canal #geral
- **Como:** Mensagem "Preciso investigar bug no login OAuth"
- **Parser:** OpenAI GPT-4o-mini com prompt v1.0.0
- **Confiança:** high
- **Resultado:** Ticket #5678 criado como bug, prioridade 2

## Versionamento do Prompt

O sistema registra a versão e o hash do prompt usado:

- `prompt_version`: Versão semântica (ex: `1.0.0`)
- `prompt_hash`: Hash MD5 dos primeiros 12 caracteres do prompt

Isso permite rastrear se mudanças no prompt afetaram a qualidade dos tickets criados.

**Exemplo:** Se você atualizar o `NL_PARSER_PROMPT`, mude também o `PROMPT_VERSION`:

```python
PROMPT_VERSION = "1.1.0"  # Nova versão após mudança no prompt
```

Os logs mostrarão qual versão do prompt foi usada para criar cada ticket.

## Armazenamento

- **Formato:** JSONL (JSON Lines) - uma linha por evento
- **Arquivo:** `audit_log.jsonl` (configurável via `AUDIT_LOG_FILE`)
- **Rotação:** Não implementada (recomendado usar logrotate em produção)
- **Git:** Arquivo ignorado no `.gitignore` (não commitar logs)

## Resposta do /webhook/chat com auditoria

Quando um ticket é criado via `/webhook/chat`, a resposta inclui metadados de auditoria:

```json
{
  "status": "ok",
  "ticket_id": 5678,
  "parsed": {...},
  "audit": {
    "log_id": "2026-03-15T14:30:45.123456Z",
    "prompt_version": "1.0.0",
    "prompt_hash": "a1b2c3d4e5f6"
  },
  "message": "Ticket #5678 criado com sucesso"
}
```

Isso permite que o cliente saiba imediatamente qual log de auditoria foi gerado.

## Comparação com o Bot do Professor

O bot do professor **não tem sistema de auditoria**. Nosso bot adiciona:

| Recurso | Professor | Nosso Bot |
|---------|-----------|-----------|
| **Logs de criação** | ❌ Não | ✅ Sim |
| **Timestamp** | ❌ Não | ✅ Sim |
| **Canal de origem** | ❌ Não | ✅ Sim |
| **ID da mensagem** | ❌ Não | ✅ Sim |
| **Versão do prompt** | ❌ Não | ✅ Sim |
| **Hash do prompt** | ❌ Não | ✅ Sim |
| **Output raw da IA** | ❌ Não | ✅ Sim |
| **Endpoint de consulta** | ❌ Não | ✅ Sim (`/audit`) |

Isso é essencial para:
- **Rastreabilidade:** saber quem criou o ticket e quando
- **Debug:** entender por que um ticket foi criado de determinada forma
- **Auditoria:** compliance e governança
- **Melhoria contínua:** analisar qualidade do parser ao longo do tempo
