# Guia de Simulação - Bot GitLab ↔ GLPI com NL Parser

Este guia mostra como testar todos os cenários do bot usando mocks e simulações.

## Pré-requisitos

### 1. Configurar ambiente virtual

```bash
cd modulo-09-automacao-de-ecossistema/resolucao

# Criar e ativar venv
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 2. Configurar chaves de API

Edite o arquivo `.env`:

```env
# Para GitLab/GLPI (sincronização MR ↔ ticket)
GITLAB_TOKEN=glpat-your-token-here
GLPI_USER_TOKEN=your-glpi-token-here
GLPI_APP_TOKEN=your-glpi-app-token-here
GITLAB_URL=https://git.ifsc.edu.br
GLPI_URL=https://glpi.ifsc.edu.br/apirest.php
GITLAB_PROJECT_ID=123

# Para NL Parser (linguagem natural)
AI_PROVIDER=openai
AI_MODEL=gpt-4o-mini
OPENAI_API_KEY=sk-your-openai-key-here
```

**Nota:** Para testar apenas o modo local (`--local`), não precisa de tokens de API.

---

## Cenário 1: Sincronização MR ↔ Ticket (Modo Local)

Este modo demonstra a sincronização bidirecional sem chamar APIs reais.

### Comando

```bash
python ecosystem-bot-gitlab-glpi.py --local
```

### Saída Esperada

```
============================================================
MODO LOCAL - DEMONSTRAÇÃO COM MOCKS
============================================================

CENÁRIO 1: MR criado → cria ticket no GLPI
------------------------------------------------------------
MR !42: Implementar validação de CPF em formulário de cadastro
Status: opened
Autor: João Silva

Ações que seriam executadas:
  1. Buscar MR no GitLab
  2. Verificar se já existe ticket vinculado
  3. Criar ticket no GLPI com título: [MR !42] Implementar validação de CPF...
  4. Adicionar comentário no MR com link do ticket

CENÁRIO 2: Status do ticket muda → notifica no MR
------------------------------------------------------------
Ticket #1234: [MR !42] Implementar validação de CPF em formulário de cadastro
Novo status: 2

Ações que seriam executadas:
  1. Buscar ticket no GLPI
  2. Extrair MR IID do título: !42
  3. Adicionar comentário no MR com atualização do ticket

============================================================
Para testar em produção, configure o .env e execute:
  python ecosystem-bot-gitlab-glpi.py
============================================================
```

### O que este modo testa

- ✅ Leitura dos arquivos de mock (`mr-mock.json`, `ticket-mock.json`)
- ✅ Lógica de extração de MR IID do título do ticket
- ✅ Fluxo de sincronização (sem APIs reais)

---

## Cenário 2: NL Parser via CLI (Linguagem Natural)

Este modo testa o parser de linguagem natural que converte mensagens em tickets estruturados.

### Teste 1: Bug simples

**Comando:**

```bash
python ecosystem-bot-gitlab-glpi.py --parse "Preciso investigar bug no login OAuth"
```

**Saída esperada (exemplo):**

```
============================================================
MODO PARSE NL - TESTE DE LINGUAGEM NATURAL
============================================================

Mensagem original: Preciso investigar bug no login OAuth

Processando com IA...

------------------------------------------------------------
JSON PARSEADO:
------------------------------------------------------------
{
  "type": "bug",
  "title": "Investigar bug no login OAuth",
  "priority": "2",
  "assignee": null,
  "dueDate": null,
  "category": "Desenvolvimento",
  "requestedBy": null,
  "reason": "Problema de autenticação afetando usuários",
  "description": "Investigar falha no fluxo de login OAuth. Verificar logs de autenticação, tokens expirados e integração com provedor OAuth.",
  "tags": ["bug", "oauth", "login", "autenticação"],
  "actionRequired": "Atribuir assignee antes de criar ticket",
  "confidence": "high",
  "rawMessage": "Preciso investigar bug no login OAuth"
}

------------------------------------------------------------
INTERPRETAÇÃO:
------------------------------------------------------------
Tipo: bug
Título: Investigar bug no login OAuth
Prioridade: 2
Assignee: N/A
Confiança: high

⚠️  Ação necessária: Atribuir assignee antes de criar ticket

✅ Pronto para criar ticket no GLPI

============================================================
```

### Teste 2: Feature com prazo e assignee implícito

**Comando:**

```bash
python ecosystem-bot-gitlab-glpi.py --parse "Carlos pediu para antecipar o módulo de relatórios para antes do fim do mês. Alguém pode pegar isso?"
```

**Saída esperada (exemplo):**

```json
{
  "type": "feature",
  "title": "Antecipar módulo de relatórios",
  "priority": "2",
  "assignee": "[A DEFINIR]",
  "dueDate": "[fim do mês corrente]",
  "requestedBy": "Carlos",
  "reason": "Antecipação solicitada por Carlos",
  "description": "Antecipar entrega do módulo de relatórios para antes do fim do mês conforme solicitado por Carlos.",
  "tags": ["feature", "relatórios", "antecipação"],
  "actionRequired": "Confirmar assignee antes de criar ticket",
  "confidence": "high"
}
```

### Teste 3: Pergunta (não cria ticket)

**Comando:**

```bash
python ecosystem-bot-gitlab-glpi.py --parse "Alguém já olhou o bug do GPS?"
```

**Saída esperada:**

```json
{
  "type": "question",
  "actionRequired": false,
  "suggestedAction": "Criar ticket de investigação? Aguardando confirmação.",
  "rawMessage": "Alguém já olhou o bug do GPS?"
}
```

**Interpretação:** O bot identifica que é uma pergunta e não cria ticket automaticamente.

### Teste 4: Mensagem insuficiente

**Comando:**

```bash
python ecosystem-bot-gitlab-glpi.py --parse "Problema no sistema"
```

**Saída esperada:**

```json
{
  "type": "unknown",
  "confidence": "low",
  "actionRequired": "Mensagem insuficiente para criar ticket. Solicitar detalhes ao autor.",
  "rawMessage": "Problema no sistema"
}
```

**Interpretação:** Confiança baixa, mensagem muito vaga.

### Teste 5: Decisão crítica

**Comando:**

```bash
python ecosystem-bot-gitlab-glpi.py --parse "Atenção time: o deploy de sexta está bloqueado porque o módulo de Score depende de hardware que não chegou. Precisamos decidir até amanhã se postergamos o deploy ou removemos o Score do escopo."
```

**Saída esperada:**

```json
{
  "type": "decision",
  "title": "Decidir escopo do deploy de sexta",
  "priority": "1",
  "assignee": null,
  "dueDate": "[amanhã]",
  "reason": "Deploy bloqueado por dependência de hardware",
  "description": "Decisão necessária: postergar deploy completo ou remover módulo Score do escopo da release.",
  "tags": ["deploy", "bloqueador", "decisão", "hardware"],
  "actionRequired": null,
  "confidence": "high"
}
```

---

## Cenário 3: Webhook Server (Produção)

Este modo inicia o servidor Flask para receber webhooks reais.

### Passo 1: Iniciar servidor

```bash
python ecosystem-bot-gitlab-glpi.py
```

**Saída esperada:**

```
============================================================
SERVIDOR WEBHOOK INICIADO
============================================================
Endpoints:
  POST /webhook/gitlab  - Recebe eventos de MR do GitLab
  POST /webhook/glpi    - Recebe atualizações de ticket do GLPI
  POST /webhook/chat    - Recebe mensagens em linguagem natural (NL Parser)
  GET  /health          - Health check

Configure os webhooks:
  GitLab: https://git.ifsc.edu.br/hooks
  GLPI: Setup > Notifications > Webhook

Exemplo de uso do NL Parser:
  curl -X POST http://localhost:5000/webhook/chat \
    -H "Content-Type: application/json" \
    -d '{"message": "Preciso investigar bug no login OAuth"}'
============================================================
```

### Passo 2: Testar health check (em outro terminal)

```bash
curl http://localhost:5000/health
```

**Resposta esperada:**

```json
{"status": "ok", "service": "ecosystem-bot"}
```

### Passo 3: Simular webhook do GitLab (MR criado)

```bash
curl -X POST http://localhost:5000/webhook/gitlab \
  -H "Content-Type: application/json" \
  -d '{
    "object_kind": "merge_request",
    "object_attributes": {
      "iid": 42,
      "title": "Teste de webhook",
      "state": "opened",
      "author": {"name": "João Silva"},
      "web_url": "https://git.ifsc.edu.br/projeto/-/merge_requests/42",
      "source_branch": "feature/teste",
      "target_branch": "main",
      "description": "Descrição do MR de teste"
    }
  }'
```

**Resposta esperada:**

```json
{
  "status": "ok",
  "ticket_id": 5678
}
```

**O que aconteceu:**
1. Bot recebeu webhook do GitLab
2. Buscou informações do MR !42
3. Criou ticket #5678 no GLPI
4. Adicionou comentário no MR com link do ticket

### Passo 4: Simular webhook do GLPI (ticket atualizado)

```bash
curl -X POST http://localhost:5000/webhook/glpi \
  -H "Content-Type: application/json" \
  -d '{
    "id": 1234,
    "status": 2,
    "comment": "Ticket em andamento"
  }'
```

**Resposta esperada:**

```json
{
  "status": "ok",
  "mr_iid": 42
}
```

**O que aconteceu:**
1. Bot recebeu webhook do GLPI
2. Buscou ticket #1234
3. Extraiu MR IID do título: !42
4. Adicionou comentário no MR com atualização do status

### Passo 5: Simular webhook de chat (NL Parser)

**Mensagem simples:**

```bash
curl -X POST http://localhost:5000/webhook/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Preciso investigar bug no login OAuth"}'
```

**Resposta esperada:**

```json
{
  "status": "ok",
  "ticket_id": 5679,
  "parsed": {
    "type": "bug",
    "title": "Investigar bug no login OAuth",
    "priority": "2",
    "assignee": null,
    "confidence": "high"
  },
  "message": "Ticket #5679 criado com sucesso"
}
```

**Mensagem complexa:**

```bash
curl -X POST http://localhost:5000/webhook/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Carlos pediu para antecipar o módulo de relatórios para antes do fim do mês. Alguém pode pegar isso?"}'
```

**Resposta esperada:**

```json
{
  "status": "ok",
  "ticket_id": 5680,
  "parsed": {
    "type": "feature",
    "title": "Antecipar módulo de relatórios",
    "priority": "2",
    "assignee": "[A DEFINIR]",
    "dueDate": "[fim do mês corrente]",
    "confidence": "high"
  },
  "message": "Ticket #5680 criado com sucesso"
}
```

**Pergunta (não cria ticket):**

```bash
curl -X POST http://localhost:5000/webhook/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Alguém já olhou o bug do GPS?"}'
```

**Resposta esperada:**

```json
{
  "status": "question",
  "parsed": {
    "type": "question",
    "actionRequired": false,
    "suggestedAction": "Criar ticket de investigação? Aguardando confirmação."
  },
  "message": "Esta é uma pergunta. Confirme se deseja criar ticket de investigação."
}
```

---

## Cenário 4: Testes com Mocks Personalizados

Você pode criar seus próprios mocks para testar cenários específicos.

### Criar mock de MR personalizado

**Arquivo: `mr-mock-personalizado.json`**

```json
{
  "iid": 99,
  "title": "Corrigir bug de autenticação OAuth",
  "state": "merged",
  "author": {
    "name": "Maria Santos",
    "username": "maria.santos"
  },
  "source_branch": "fix/oauth-bug",
  "target_branch": "main",
  "web_url": "https://git.ifsc.edu.br/projeto/exemplo/-/merge_requests/99",
  "description": "Corrige problema de timeout na autenticação OAuth com Google."
}
```

### Criar mock de ticket personalizado

**Arquivo: `ticket-mock-personalizado.json`**

```json
{
  "id": 5678,
  "name": "[MR !99] Corrigir bug de autenticação OAuth",
  "status": 6,
  "content": "Ticket resolvido - bug corrigido e testado.",
  "date_creation": "2026-03-20T14:15:00-03:00"
}
```

### Testar com mocks personalizados

```bash
# Substitui os mocks padrão
cp mr-mock-personalizado.json mr-mock.json
cp ticket-mock-personalizado.json ticket-mock.json

# Executa teste
python ecosystem-bot-gitlab-glpi.py --local
```

---

## Resumo dos Comandos

| Cenário | Comando | Requer API Key |
|---|---|---|
| **Modo local (mocks)** | `python ecosystem-bot-gitlab-glpi.py --local` | ❌ Não |
| **NL Parser (CLI)** | `python ecosystem-bot-gitlab-glpi.py --parse "mensagem"` | ✅ Sim |
| **Webhook server** | `python ecosystem-bot-gitlab-glpi.py` | ✅ Sim |
| **Health check** | `curl http://localhost:5000/health` | ❌ Não |
| **Simular GitLab** | `curl -X POST http://localhost:5000/webhook/gitlab ...` | ✅ Sim |
| **Simular GLPI** | `curl -X POST http://localhost:5000/webhook/glpi ...` | ✅ Sim |
| **Simular chat** | `curl -X POST http://localhost:5000/webhook/chat ...` | ✅ Sim |

---

## Solução de Problemas

### "OPENAI_API_KEY não configurada"

**Causa:** Chave de API não está no `.env` ou não foi carregada.

**Solução:**
```bash
# Verifica se o .env existe
ls -la .env

# Verifica se a chave está configurada
grep OPENAI_API_KEY .env

# Recarrega o ambiente
source venv/bin/activate
```

### "Flask não instalado"

**Causa:** Dependências não instaladas.

**Solução:**
```bash
pip install -r requirements.txt
```

### "Tokens de API não configurados"

**Causa:** Tokens do GitLab/GLPI não estão no `.env`.

**Solução:**
```bash
# Para testar apenas o modo local, use:
python ecosystem-bot-gitlab-glpi.py --local

# Para modo webhook, configure os tokens no .env
```

### "Parser não retornou JSON válido"

**Causa:** Modelo de IA retornou texto fora do JSON.

**Solução:** O código já extrai JSON automaticamente com regex. Se persistir, verifique se o modelo está respondendo corretamente.

---

## Próximos Passos

Depois de testar localmente:

1. **Configurar webhooks reais** no GitLab e GLPI
2. **Expor servidor localmente** com ngrok para testes
3. **Adicionar interface de chat** (Slack/Teams)
4. **Implementar query contextual** com LangChain

Consulte o `README.md` para detalhes.
