# Questionamentos ao solicitante — Análise Documental
**Data:** 14/07/2026

**Autor:** Daniel Severo Estrazulas

**Para:** setor solicitante ([SETOR SOLICITANTE] / Ingresso)

## O que entendemos
Cursos de qualificação profissional, especialização e mestrado usam análise documental como etapa classificatória. Hoje o sistema de ingresso não suporta esse tipo de seleção — a classificação precisa ser feita fora e importada por planilha.

Vocês pediram quatro coisas:

1. No cadastro do edital, incluir "Análise Documental" como critério de seleção.
2. Na inscrição, o candidato envia os documentos e informa uma pontuação para cada um.
3. Depois da inscrição, o coordenador de curso confere os documentos, atribui pontuação final e pode desclassificar candidatos. Se houver entrevista, a nota da entrevista entra no cálculo.
4. Após o resultado, o candidato pode recorrer pelo portal, e o coordenador defere ou indefere.

## O que entendemos:
Conversamos sobre 21 pontos ao longo do refinamento. Abaixo, o resumo das decisões por tema.

### Edital
- "Análise Documental" entra como item novo no combobox de critério de seleção. Convive com "Importação da classificação" (que já existe e permanece). Cada edital escolhe um dos dois.
- O cadastro do edital ganha checkboxes ativados conforme a necessidade:
  - "Terá entrevista?" — exige informar os pesos (ex.: 60% documental, 40% entrevista).
  - "Terá convocação para nivelamento?" — habilita essa etapa.
  - "Permitirá recursos?" — abre a possibilidade de recurso ao candidato.
- Novo campo "Pontuação máxima total" — teto geral da soma de pontos que o candidato pode declarar.

#### Como fica na tela — cadastro do edital (protótipo sugestivo)

```plaintext
┌──────────────────────────────────────────────────────────────┐
│ CADASTRO DE EDITAL                                           │
│                                                              │
│ Critério de seleção:  [ Análise Documental          ▼ ]     │
│                                                              │
│ Pontuação máxima total: [ 100 ]                              │
│                                                              │
│ ☑ Terá entrevista?                                           │
│   ├─ Peso da análise documental:  [ 60 ] %                   │
│   ├─ Peso da entrevista:          [ 40 ] %                   │
│   └─ Calendário da entrevista:    [ Entrev. Edital 01  ▼ ]   │
│                                                              │
│ ☑ Terá análise documental?                                   │
│   └─ Calendário da análise:       [ Análise 2026-2     ▼ ]   │
│                                                              │
│ ☐ Terá convocação para nivelamento?                          │
│                                                              │
│ ☑ Permitirá recursos da análise documental?                  │
│   └─ Calendário de recurso:       [ Recurso 2026-2    ▼ ]    │
│                                                              │
│ [Salvar edital]                                              │
└──────────────────────────────────────────────────────────────┘

```
Quando um checkbox é desmarcado, os campos vinculados desaparecem.

### Calendários
- Cada etapa (análise, entrevista, nivelamento, recurso) terá um calendário próprio cadastrado separadamente. Um calendário tem: data de início, data de fim e data de publicação do resultado.
- No edital, ao marcar um checkbox, você escolhe qual calendário se aplica àquela etapa.
- Um calendário pode ser do tipo "por edital" (um único calendário vale para todas as ofertas do edital) ou "por curso" (cada oferta/curso pode ter datas diferentes). Isso é definido no cadastro do calendário.
- O mesmo calendário pode ser reutilizado em vários editais.

#### Como fica na tela — CRUD de calendários (protótipo sugestivo)

```plaintext
┌─────────────────────────────────────────────────────────┐
│ CADASTRO DE CALENDÁRIO DE ETAPA                         │
│                                                         │
│ Nome:          [ Análise Documental 2026-2        ]     │
│ Tipo de etapa: [ Análise Documental           ▼ ]       │
│                                                         │
│ Escopo:        ● Por edital                             │
│                ○ Por curso/oferta                        │
│                                                         │
│ ── Quando "Por edital" ──────────────────────────────   │
│ Edital vinculado:    [ Edital 01/2026             ▼ ]   │
│                                                         │
│ Data de início:      [ 01/08/2026 ]                     │
│ Data de fim:         [ 30/08/2026 ]                     │
│ Data de publicação:  [ 05/09/2026 ]                     │
│                                                         │
│ [Salvar]  [Cancelar]                                    │
└─────────────────────────────────────────────────────────┘

```
Quando o escopo for "Por curso/oferta", o campo "Edital vinculado" é substituído por "Oferta vinculada":

```plaintext
┌─────────────────────────────────────────────────────────┐
│ CADASTRO DE CALENDÁRIO DE ETAPA                         │
│                                                         │
│ Nome:          [ Análise Doc. [CURSO EXEMPLO] ]     │
│ Tipo de etapa: [ Análise Documental           ▼ ]       │
│                                                         │
│ Escopo:        ○ Por edital                             │
│                ● Por curso/oferta                        │
│                                                         │
│ ── Quando "Por curso/oferta" ────────────────────────   │
│ Oferta vinculada:    [ [CURSO EXEMPLO] - [CIDADE A] ▼ ] │
│                                                         │
│ Data de início:      [ 01/08/2026 ]                     │
│ Data de fim:         [ 15/08/2026 ]                     │
│ Data de publicação:  [ 20/08/2026 ]                     │
│                                                         │
│ [Salvar]  [Cancelar]                                    │
└─────────────────────────────────────────────────────────┘

```
Cada oferta pode ter seu próprio calendário com datas distintas. Um edital com 3 cursos pode ter 3 calendários "por curso" para a mesma etapa.

### Inscrição do candidato
- No cadastro de Tipos de Documento (a tela que já existe em [GESTÃO LOCAL] → Processo → Tipos de Documentos), acrescentamos a opção "Requer pontuação?". Só os documentos marcados terão campo de pontuação ao lado do upload.
- O teto de pontuação por documento vem de um parâmetro geral do sistema. Se um tipo de documento precisar de teto diferente (ex.: "Curso de extensão" com máximo de 20 pontos), basta sobrescrever no cadastro desse tipo.
- O candidato vê a soma acumulada enquanto preenche. Se a soma passar do teto do edital, o sistema bloqueia o envio.
- Enquanto o prazo de inscrição estiver aberto, o candidato altera pontuação e documento. Depois, trava.

#### Como fica na tela — formulário de inscrição do candidato (protótipo sugestivo)

```plaintext
┌─────────────────────────────────────────────────────────────┐
│ DOCUMENTOS PARA ANÁLISE DOCUMENTAL                          │
│                                                             │
│ Pontuação máxima total do edital: 100 pontos                │
│ Soma atual: 55 de 100                                       │
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░ 55%                    │
│                                                             │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ Artigo em periódico (máx. 30 pts por documento)         │ │
│ │ Arquivo: [ artigo_qualis_a1.pdf      ] [Alterar]        │ │
│ │ Pontuação declarada: [ 30 ]                             │ │
│ └─────────────────────────────────────────────────────────┘ │
│                                                             │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ Curso de extensão (máx. 20 pts por documento)           │ │
│ │ Arquivo: [ certificado_extensao.pdf  ] [Alterar]        │ │
│ │ Pontuação declarada: [ 15 ]                             │ │
│ └─────────────────────────────────────────────────────────┘ │
│                                                             │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ Diploma de especialização (máx. 50 pts por documento)   │ │
│ │ Arquivo: [ _________________ ] [Selecionar PDF]         │ │
│ │ Pontuação declarada: [ __ ]                             │ │
│ └─────────────────────────────────────────────────────────┘ │
│                                                             │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ RG (documento obrigatório, sem pontuação)               │ │
│ │ Arquivo: [ rg_frente_verso.pdf       ] [Alterar]        │ │
│ └─────────────────────────────────────────────────────────┘ │
│                                                             │
│ [Confirmar inscrição]                                       │
└─────────────────────────────────────────────────────────────┘

```
O documento "RG" não tem campo de pontuação porque não está marcado com "Requer pontuação?" no cadastro de tipos.

### Análise e classificação
- Novo perfil: "Analista de Documento". Diferente de "[GESTÃO LOCAL] de [UNIDADE]" (que já existe). O analista vê apenas os candidatos do curso/oferta ao qual foi vinculado e só acessa as telas de pontuação. Sem acesso administrativo.
- Na tela de análise (que já está especificada), o analista preenche:
  - Pontuação documental (número) + justificativa obrigatória.
  - Se o edital tem entrevista: pontuação da entrevista + justificativa.
- Para desclassificar, o analista preenche o motivo em texto livre (mesmo padrão já definido).
- A pontuação final é calculada automaticamente pelos pesos do edital.
- Antes da classificação, existe uma lista onde é possível corrigir manualmente a pontuação de qualquer candidato (com registro de quem fez a alteração e quando).
- A classificação não é automática. Existem botões manuais para processar cada lista.

#### Como fica na tela — análise do candidato pelo analista (protótipo sugestivo)

```plaintext
┌──────────────────────────────────────────────────────────────────────┐
│ ANÁLISE DO CANDIDATO — João da Silva (inscr. 202601001)              │
│ Curso: [CURSO EXEMPLO] │ [UNIDADE]: [CIDADE A]                │
├──────────────────────────────┬───────────────────────────────────────┤
│ PAINEL ESQUERDO              │ PAINEL DIREITO                        │
│                              │                                       │
│ Status: Inscrição Homologada │ Documentos enviados:                  │
│                              │  [Artigo periódico] [Curso extensão]  │
│ ─── Pontuação ─────────────  │  [Diploma espec.]                     │
│                              │                                       │
│ Pont. documental: [ 75 ]     │ ┌──────────────────────────────────┐  │
│ Justificativa:               │ │ Visualizador do documento        │  │
│ [ Candidato apresentou 3     │ │        (PDF inline)              │  │
│   artigos válidos e 1 curso  │ │                                  │  │
│   com carga horária mínima ] │ └──────────────────────────────────┘  │
│                              │                                       │
│ Pont. entrevista: [ 85 ]     │ Pontuação declarada pelo candidato:   │
│ Justificativa:               │ 30 pts (artigo) + 15 pts (extensão)   │
│ [ Demonstrou domínio do      │ = 45 pontos                           │
│   tema e boa articulação ]   │                                       │
│                              │                                       │
│ ─── Pontuação Final ───────  │                                       │
│ Cálculo: 75×60% + 85×40%    │                                       │
│ = 79,00                      │                                       │
│                              │                                       │
│ ─── Desclassificação ─────  │                                       │
│ Motivo: [ ________________ ] │                                       │
│ [ELIMINAR CANDIDATO]         │                                       │
│                              │                                       │
│ [Salvar análise]             │                                       │
└──────────────────────────────┴───────────────────────────────────────┘

```

#### Como fica na tela — lista com pontuação final editável (protótipo sugestivo)

```plaintext
┌───────────────────────────────────────────────────────────────────────────┐
│ CANDIDATOS COM PONTUAÇÃO FINAL — Edital 01/2026 — [CURSO EXEMPLO]  │
│                                                                           │
│ Oferta: [ [CURSO EXEMPLO] ▼ ]   [Filtrar]                          │
│                                                                           │
│ ┌────┬──────────────────┬────────┬───────┬───────┬───────┬──────────────┐ │
│ │ #  │ Nome             │ Inscr. │ Doc.  │ Entr. │ Final │ Ação         │ │
│ ├────┼──────────────────┼────────┼───────┼───────┼───────┼──────────────┤ │
│ │ 1  │ João da Silva    │ 001    │ 75,00 │ 85,00 │ 79,00 │ [Editar]     │ │
│ │ 2  │ Maria Souza      │ 005    │ 80,00 │ 70,00 │ 76,00 │ [Editar]     │ │
│ │ 3  │ Carlos Alberto   │ 008    │ 60,00 │ 90,00 │ 72,00 │ [Editar]     │ │
│ │ -- │ Ana Beatriz      │ 012    │ --    │ --    │ ELIM. │ Ver motivo   │ │
│ └────┴──────────────────┴────────┴───────┴───────┴───────┴──────────────┘ │
│                                                                           │
│ [Classificar Análise Documental]  [Exportar CSV]  [Exportar HTML]         │
└───────────────────────────────────────────────────────────────────────────┘

```
Ao clicar "Editar", abre campo inline para corrigir a pontuação final com justificativa obrigatória (registra quem alterou e quando).

### Portal do candidato
- O sistema não publica as listas no portal. Elas são extraídas (CSV/HTML) e publicadas no site institucional pela [SETOR SOLICITANTE], como já é feito.
- No portal, o candidato vê:
  - Antes da data de publicação do calendário da análise: "Aguardando análise documental".
  - Depois da data de publicação: pontuação final + status (Classificado, Eliminado com motivo, etc.).
- Mesmo padrão para o recurso: "Recurso em análise" até a data de publicação; depois, "Deferido" ou "Indeferido" com nova pontuação.

### Recurso
- O candidato abre o recurso pelo portal: preenche uma justificativa em texto e anexa um PDF de manifestação.
- O analista abre tudo numa tela só: documentos originais, pontuação anterior, texto do pedido, PDF anexado. Na mesma tela, lança nova pontuação e justificativa da revisão. Uma ação só.
- Ao deferir, a pontuação é corrigida e o candidato passa a ver o novo status no portal (respeitando a data de publicação do calendário de recurso).

#### Como fica na tela — candidato cadastra recurso (protótipo sugestivo)

```plaintext
┌─────────────────────────────────────────────────────────┐
│ RECURSO DA ANÁLISE DOCUMENTAL                           │
│ Edital 01/2026 — [CURSO EXEMPLO]                 │
│                                                         │
│ Sua pontuação final: 79,00                              │
│ Status atual: Classificado em 3º lugar                  │
│                                                         │
│ Justificativa do recurso:                               │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ Solicito revisão da pontuação documental. O artigo  │ │
│ │ publicado na revista X atende ao critério de...     │ │
│ │                                                     │ │
│ └─────────────────────────────────────────────────────┘ │
│                                                         │
│ PDF de manifestação:                                    │
│ [ recurso_manifestacao.pdf ] [Selecionar arquivo]       │
│                                                         │
│ [Enviar recurso]                                        │
└─────────────────────────────────────────────────────────┘

```

#### Como fica na tela — analista julga o recurso (protótipo sugestivo)

```plaintext
┌────────────────────────────────────────────────────────────────────────┐
│ JULGAMENTO DE RECURSO — João da Silva (inscr. 202601001)               │
├────────────────────────────────┬───────────────────────────────────────┤
│ DADOS DO RECURSO               │ DOCUMENTOS ORIGINAIS                  │
│                                │                                       │
│ Data do pedido: 10/09/2026     │ [Artigo periódico] [Curso extensão]   │
│                                │ [Diploma espec.]                      │
│ Justificativa do candidato:    │                                       │
│ "Solicito revisão da           │ ┌─────────────────────────────────┐   │
│  pontuação documental..."      │ │ Visualizador PDF                │   │
│                                │ │ (documento ou manifestação)     │   │
│ [Ver PDF de manifestação]      │ └─────────────────────────────────┘   │
│                                │                                       │
│ ─── Pontuação anterior ─────  │                                       │
│ Documental: 75,00              │                                       │
│ Entrevista: 85,00              │                                       │
│ Final anterior: 79,00          │                                       │
│                                │                                       │
│ ─── Decisão ─────────────────  │                                       │
│ Resultado: ● Deferido          │                                       │
│            ○ Indeferido        │                                       │
│                                │                                       │
│ Nova pont. documental: [ 85 ]  │                                       │
│ Nova pont. final: 85×60%+85×40%│                                       │
│ = 85,00                        │                                       │
│                                │                                       │
│ Justificativa da revisão:      │                                       │
│ [ Artigo na revista X foi      │                                       │
│   reavaliado como Qualis A1  ] │                                       │
│                                │                                       │
│ [Salvar julgamento]            │                                       │
└────────────────────────────────┴───────────────────────────────────────┘

```

## O que precisa de decisão de vocês
Seis pontos ficaram pendentes. Sem essas respostas não conseguimos fechar o desenho:

1. Critérios para gerar listas intermediárias. Quantos candidatos são convocados para entrevista? Como fica a reserva de vagas por cota nessa convocação? Existe lista de espera? Esses critérios mudam por edital ou são fixos?
2. Nivelamento O que é? Como e quando aparece no sistema?. Além de gerar a lista de convocados (que já está garantido), o candidato precisa confirmar aceite? Tem alocação em turmas? Controle de presença? Aprovação com impacto na matrícula?
3. Critério de desempate. Quando dois candidatos empatam na pontuação final, quem fica na frente? Nossa sugestão: Mas o setor pode ter outra regra (ex.: quem foi melhor na entrevista, quem tem mais titulação). Idade?
4. Precisamos das convocações publicadas desse edital como referência para modelar os relatórios.
5. Quem cadastra o perfil "Analista de Documento"? Só o Administrador/[SETOR SOLICITANTE], ou a [GESTÃO LOCAL] de [UNIDADE] também pode atribuir dentro do [UNIDADE] dela?
6. Notificação por e-mail. A funcionalidade de avisar o candidato por e-mail quando um resultado sai fica separada desta demanda. Confirmam?
7. Pode ter recurso de recurso?
8. O que acontece no deferimento e indeferimento?
9. Como são feitas as notificações para recursos e ver respostas das avaliações (email em que formato?
10. Pode ter mais de um avaliador ?
11. Convocações onde definir horarios e instruções? No edital? Sistema de notificações acionado manualmente, site do [INSTITUIÇÃO]?
12. Quem vai cadastrar os avaliadores?
13. Como tratar ausências nas convocações?

## Nossas sugestões
Entregar primeiro o essencial: critério novo, calendários, pontuação por documento, perfil do analista, análise com pontuação, classificação simples e recurso. Nivelamento e listas intermediárias mais complexas entram na sequência, depois que as 6 pendências acima forem resolvidas.

O modelo de pontuação declarada pelo candidato + correção pelo analista com registro de autoria já existe no sistema (é o mesmo usado para nota do ENEM). Vamos reaproveitar essa base.

O perfil do analista vai ser enxuto de propósito: ele vê só os candidatos do curso dele e os botões de análise/recurso. Nada além disso.

## O que muda na prática
Para o candidato: ao se inscrever num edital de Análise Documental, digita uma pontuação para cada documento que envia. Depois acompanha o resultado pelo portal (pontuação final + status), respeitando as datas de publicação. Se discordar, entra com recurso ali mesmo.

Para o coordenador de curso (analista): ganha acesso a uma tela onde vê os candidatos do curso dele, lança pontuação com justificativa, e julga eventuais recursos.

Para a [SETOR SOLICITANTE]: cadastra o edital com o critério "Análise Documental", configura calendários e pesos, atribui os analistas às ofertas, acompanha o processo e aciona os botões de classificação. Publica as listas no site institucional como já faz.

## Próximos passos
1. Ler este documento e alinhar dentro do setor.
2. Agendar reunião para resolver as 6 pendências.
3. Após alinhamento, criamos as tarefas de desenvolvimento.