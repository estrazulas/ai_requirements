# Módulo 9 - Automação de Ecossistema: GitLab ↔ GLPI

> **Resolução adaptada para IFSC** - Bot de sincronização entre GitLab e GLPI

## Visão Geral

Este módulo implementa um bot de automação de ecossistema que sincroniza Merge Requests do GitLab com tickets do GLPI, similar ao exemplo do professor com Slack ↔ Jira.

### Fluxos Implementados

#### Fluxo 1: GitLab → GLPI (MR cria/atualiza ticket)

Quando um Merge Request é criado ou atualizado no GitLab:
1. Webhook do GitLab dispara evento para o bot
2. Bot busca informações do MR via API
3. Cria ticket no GLPI com título formatado: `[MR !42] Título do MR`
4. Adiciona comentário no MR com link do ticket GLPI

**Exemplo:**
```
MR !42 criado: "Implementar validação de CPF"
  ↓
Ticket #1234 criado no GLPI
  ↓
Comentário no MR: "🎫 Ticket GLPI criado: #1234"
```

#### Fluxo 2: GLPI → GitLab (ticket notifica no MR)

Quando o status de um ticket muda no GLPI:
1. Webhook do GLPI dispara evento para o bot
2. Bot busca informações do ticket
3. Extrai MR IID do título do ticket
4. Adiciona comentário no MR com atualização do status

**Exemplo:**
```
Ticket #1234 muda para "Em andamento"
  ↓
Bot identifica MR !42 no título
  ↓
Comentário no MR: "🎫 Ticket #1234 atualizado: Em andamento"
```

## Estrutura da Resolução

```
resolucao/
├── ecosystem-bot-gitlab-glpi.py    # Bot principal
├── mr-mock.json                     # Mock de MR para testes
├── ticket-mock.json                 # Mock de ticket para testes
├── .env.example                     # Template de configuração
├── .env                             # Configuração local (não commitar)
├── requirements.txt                 # Dependências Python
└── README.md                        # Este arquivo
```

## Como Usar

### 1. Configurar Ambiente

```bash
cd modulo-09-automacao-de-ecossistema/resolucao

# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 2. Configurar Tokens

Edite o arquivo `.env` com seus tokens:

```env
GITLAB_TOKEN=glpat-your-gitlab-token-here
GLPI_USER_TOKEN=your-glpi-user-token-here
GLPI_APP_TOKEN=your-glpi-app-token-here
GITLAB_URL=https://git.ifsc.edu.br
GLPI_URL=https://glpi.ifsc.edu.br/apirest.php
GITLAB_PROJECT_ID=123
```

**Onde obter os tokens:**

- **GitLab Token**: Settings → Access Tokens → Criar token com `api` scope
- **GLPI User Token**: Setup → General → API → Criar token de usuário
- **GLPI App Token**: Mesmo local, criar token de aplicação

### 3. Testar Localmente (Modo Mock)

```bash
python ecosystem-bot-gitlab-glpi.py --local
```

Este modo demonstra os fluxos sem chamar APIs reais, usando os arquivos de mock.

### 4. Executar em Produção (Modo Webhook)

```bash
python ecosystem-bot-gitlab-glpi.py
```

O bot inicia um servidor Flask na porta 5000 com os seguintes endpoints:

- `POST /webhook/gitlab` - Recebe eventos de MR do GitLab
- `POST /webhook/glpi` - Recebe atualizações de ticket do GLPI
- `GET /health` - Health check

### 5. Configurar Webhooks

#### GitLab Webhook

1. Vá em Settings → Webhooks do seu projeto GitLab
2. URL: `http://seu-servidor:5000/webhook/gitlab`
3. Trigger: `Merge request events`
4. Salve e teste

#### GLPI Webhook

1. Vá em Setup → Notifications → Webhooks
2. URL: `http://seu-servidor:5000/webhook/glpi`
3. Eventos: `Ticket update`
4. Salve e teste

## Limitações Atuais

### O que o bot faz:
- ✅ Sincronização bidirecional MR ↔ ticket
- ✅ Criação automática de tickets a partir de MRs
- ✅ Notificação de mudanças de status no MR
- ✅ Rastreamento via título formatado `[MR !42]`

### O que o bot NÃO faz:
- ❌ **Query contextual** - Não responde perguntas como "qual o status da US-123?"
- ❌ **Parsing de linguagem natural** - Não extrai informações de conversas
- ❌ **Interface de chat** - Não tem integração com Slack/Teams para perguntas
- ❌ **Inteligência contextual** - Não busca dados históricos ou relacionados

## Comparação com o Exemplo do Professor

| Característica | Professor (Slack ↔ Jira) | Nossa Resolução (GitLab ↔ GLPI) |
|---|---|---|
| **Ferramentas** | Slack + Jira | GitLab + GLPI |
| **Linguagem** | Node.js | Python |
| **NL Parsing** | ✅ Sim (Claude/Gemini) | ❌ Não |
| **Bidirecional** | ✅ Sim | ✅ Sim |
| **Query Contextual** | ❌ Não | ❌ Não |
| **Webhook Server** | ❌ Não (Make.com) | ✅ Sim (Flask) |

## Próximos Passos (Opcional)

Para adicionar **query contextual**, seria necessário:

1. **Interface de chat** (Slack, Teams, ou CLI)
2. **LLM com tools** (LangChain agents) que:
   - Interpreta pergunta em linguagem natural
   - Decide qual API chamar (GitLab ou GLPI)
   - Busca dados relevantes
   - Gera resposta contextual

**Exemplo de uso com query contextual:**
```
Usuário: "Quais MRs estão relacionados ao ticket #1234?"
Bot: "Encontrei 2 MRs vinculados ao ticket #1234:
      - MR !42: Implementar validação de CPF (aberto)
      - MR !38: Corrigir bug de login (merged)"
```

**Exemplo mais avançado:**
```
Usuário: "Qual o status da US-123 e quais tickets estão relacionados?"
Bot: "US-123 'Implementar autenticação' está em revisão (MR !45).
      Tickets relacionados:
      - #1230: Configurar OAuth (resolvido)
      - #1231: Implementar login (em andamento)
      - #1232: Testes de segurança (novo)"
```

## Recursos Adicionais

- [GitLab API Documentation](https://docs.gitlab.com/ee/api/)
- [GLPI API Documentation](https://github.com/glpi-project/glpi/blob/master/apirest.md)
- [Flask Documentation](https://flask.palletsprojects.com/)

---

**Adaptado do template do professor Ahirton Lopes para o contexto IFSC**
