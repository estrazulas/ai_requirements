# Entendendo os Checklists de Compliance

Os **checklists de compliance** são diferentes das verificações automatizadas do script de governança. Enquanto o `danger-gitlab-ifsc.py` verifica regras fixas (título, aprovadores, tamanho), os checklists são gerados por IA com análise contextual de cada MR.

## Diferença entre os dois

| Verificação Automatizada | Checklist de Compliance |
|---|---|
| Script `danger-gitlab-ifsc.py` | Script `compliance-checker.py` |
| Regras fixas (título, aprovadores, tamanho) | Gerado por IA com contexto do MR |
| Passa/falha baseado em condições | Lista de itens a verificar manualmente |
| Bloqueia o merge | Orienta a revisão |

## O que são os checklists

São listas estruturadas em 3 categorias, geradas pela IA para cada MR:

### 1. **BLOQUEADORES** (máx. 5 itens)

Itens que impedem o merge se não estiverem OK.

Exemplo:
- **[Legal]** Base legal LGPD validada — aditivo contratual anexado
- **[Segurança]** Scan de vulnerabilidades passou no CI
- **[Aprovação]** Time de segurança aprovou alteração em `src/auth/`

### 2. **VERIFICAÇÕES OPERACIONAIS** (máx. 5 itens)

Itens que devem ser verificados mas não bloqueiam.

Exemplo:
- **[Operacional]** MR com 600 linhas — considere dividir
- **[Técnico]** Cobertura caiu 8 pontos — adicione testes
- **[Documentação]** Atualizar changelog

### 3. **INFORMATIVOS** (máx. 4 itens)

Registros obrigatórios para auditoria.

Exemplo:
- **[Rastreabilidade]** Hash do commit: `abc123`
- **[Documentação]** MR relacionado: #42

## Como funciona na prática

O arquivo `compliance-checklist-prompt.md` (do professor) é um **template de prompt** que você alimenta em uma IA (junto com o contexto do MR), e ela devolve um checklist personalizado.

O script `compliance-checker.py` automatiza isso:
1. Lê o contexto do MR
2. Monta o prompt com o template
3. Chama a IA (OpenAI/Anthropic)
4. Posta o checklist como comentário no MR

## Exemplo de uso

```bash
# Gera checklist para um MR específico
python compliance-checker.py --local --mock mr-mock-sucesso.json
```

A IA analisa o MR e gera algo como:

```markdown
### BLOQUEADORES
1. **[Técnico]** Arquivo crítico `migrations/001_add_users.sql` modificado — requer aprovação do DBA.
2. **[Legal]** MR menciona "dados de usuários" — verificar conformidade LGPD.

### VERIFICAÇÕES OPERACIONAIS
1. **[Performance]** Query adicionada sem índice — verificar impacto em tabelas grandes.
2. **[Testes]** Cobertura caiu 12 pontos — adicionar testes para migration.

### INFORMATIVOS
1. **[Rastreabilidade]** Migration executada em produção: sim/não
2. **[Documentação]** Atualizar diagrama de banco de dados
```

## Por que usar checklists?

As verificações automatizadas são ótimas para regras fixas, mas não conseguem capturar nuances contextuais. Os checklists complementam com:

- **Análise de risco contextual** — a IA entende o que o MR está fazendo
- **Considerações de compliance** — LGPD, segurança, performance
- **Recomendações específicas** — não apenas "passou/falhou"
- **Documentação automática** — gera registro para auditoria

## Quando usar cada um

| Situação | Ferramenta |
|---|---|
| Validar formato do título (tem #issue?) | `danger-gitlab-ifsc.py` |
| Verificar número de aprovadores | `danger-gitlab-ifsc.py` |
| Checar tamanho do MR | `danger-gitlab-ifsc.py` |
| Analisar impacto de mudanças em dados sensíveis | `compliance-checker.py` |
| Gerar recomendações contextuais | `compliance-checker.py` |
| Criar documentação de auditoria | `compliance-checker.py` |

## Integração no CI/CD

Ambos os scripts podem rodar juntos no pipeline:

```yaml
stages:
  - test
  - compliance

# 1. Governança automatizada (regras fixas)
governance-check:
  stage: test
  script:
    - python danger-gitlab-ifsc.py
  rules:
    - if: $CI_MERGE_REQUEST_IID

# 2. Checklist de compliance (análise contextual)
compliance-review:
  stage: compliance
  script:
    - python compliance-checker.py
  rules:
    - if: $CI_MERGE_REQUEST_IID
  allow_failure: true  # não bloqueia, apenas orienta
```

O primeiro script **bloqueia** o merge se as regras não forem seguidas. O segundo **orienta** a revisão com checklists contextuais.
