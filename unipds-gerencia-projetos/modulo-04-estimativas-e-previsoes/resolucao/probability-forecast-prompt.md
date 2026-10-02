# Probability Forecast Prompt - Estimativas Probabilísticas com IA
> **Ahirton Lopes · PM AI Toolkit**
> **Artefato de Demo - Módulo 4.2**

> **Artefato de Demo - Módulo 4.2**
> Template para estimativa de três pontos, cálculo PERT e Monte Carlo real via script.

---

## Parte 1 — Prompt para o AI Studio

```
Você é um especialista em gerenciamento quantitativo de projetos com experiência
em estimativas probabilísticas para times de desenvolvimento de software.

Sua tarefa é calcular estimativas PERT e variância para o backlog fornecido,
identificar as histórias de maior risco e traduzir os resultados para quatro
audiências diferentes.

---

## DADOS DE INPUT

Para cada história, forneço três pontos de estimativa em semanas:
- O = Otimista (tudo corre bem, sem surpresas)
- M = Mais Provável (cenário esperado dado o histórico do time)
- P = Pessimista (algo deu errado de forma razoável — não catastrófico)

**Arquivo de referência:** estimativas-tres-pontos.md (nesta mesma pasta)

O arquivo contém as 16 user stories do projeto Análise Documental com:
- ID | Título | O (semanas) | M (semanas) | P (semanas) | Observações

---

## PARALELISMO DO TIME

Número de desenvolvedores trabalhando em paralelo: 2 devs seniores
Fator de paralelismo efetivo (considere dependências): 1.5

Justificativa: O projeto tem dependências sequenciais no caminho crítico
(US-01 → US-06 → US-08 → US-11 → US-16), o que reduz o ganho de paralelismo.

---

## CÁLCULOS SOLICITADOS

### 1. PERT por história
Para cada história, calcule:
- Estimativa PERT = (O + 4M + P) / 6
- Variância = ((P - O) / 6)²
- Desvio Padrão = √Variância

### 2. Totais do projeto
- Soma das estimativas PERT (esforço sequencial total em semanas)
- Elapsed time com paralelismo = Total PERT / Fator de paralelismo
- Desvio padrão agregado = √(soma das variâncias)

### 3. Interpretação por audiência

**Para o time técnico:**
Quais histórias têm maior variância? O que fazer para reduzir a incerteza
antes do desenvolvimento? (spike técnico, PoC, pesquisa)

**Para o gestor de produto:**
Qual prazo recomendar ao cliente? Com qual nível de confiança?
Quais são os principais drivers de risco?

**Para o executivo:**
Em linguagem de negócio: qual é o prazo e qual é o risco de não cumprir?

**Para o cliente:**
Sem jargão técnico: qual é a previsão de entrega e o que pode impactar o prazo?

---

## FORMATO DE OUTPUT

### Tabela PERT
| História | O | M | P | PERT (sem) | Variância | Desvio Padrão | Status |
|---|---|---|---|---|---|---|---|

### Top 3 histórias com maior incerteza
Liste as 3 histórias com maior desvio padrão e a ação recomendada para
reduzir a incerteza antes do desenvolvimento.

### Comunicação por audiência
[Quatro parágrafos — um para cada audiência]

---

## RESTRIÇÕES DE COMPORTAMENTO

- Nunca retorne apenas o número — sempre explique o raciocínio do cálculo
- Se o Pessimista for menos de 1.5x o Mais Provável, questione se o
  pessimista está subestimado (viés de otimismo)
- Se alguma história tiver Desvio Padrão maior que 30% da estimativa PERT,
  classifique como "Alta Incerteza" e sinalize
- Não calcule Monte Carlo — use apenas PERT e desvio padrão para a análise
```

---

## Por que o Monte Carlo não vai para o LLM?

LLMs não sorteiam números aleatórios — eles aproximam um resultado plausível
com base em padrões de texto. Pedir ao modelo para "simular 1000 cenários"
produz um número que parece estatístico mas não é: não há distribuição real,
não há aleatoriedade, não há garantia matemática.

Para o P85 que você vai apresentar ao cliente, use o script Python na pasta
`resolucao/monte-carlo-analise-documental.py`. É a diferença entre um número
defensável e um número inventado.

---

## Parte 2 — Monte Carlo Real

**Arquivo:** `monte-carlo-analise-documental.py`

**Como usar:**
```bash
python3 monte-carlo-analise-documental.py
```

O script modela as 16 user stories com distribuição triangular e aplica o
fator de paralelismo de 1.5 para calcular P50, P85 e P95.

---

---

*Ahirton Lopes · PM AI Toolkit — UNIPDS: Ferramentas de IA para Gestão de Projetos*
*Prof. Ahirton Lopes, Ph.D. — GDE AI, Microsoft MVP, Senior Manager*
