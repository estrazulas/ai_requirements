# Resolução - Módulo 4: Estimativas Probabilísticas

Este documento explica como criamos as estimativas de três pontos e rodamos o Monte Carlo para o projeto Análise Documental.

---

## Contexto: O que já tínhamos do Módulo 3

Do módulo 3 (`modulo-03-cronograma-e-capacidade/resolucao/cronograma-sprints-atualizado.md`), tínhamos:

- **16 user stories** com effort em horas (ex: US-01 = 5.5h, US-08 = 23.4h)
- **Time:** 2 devs seniores
- **Capacidade:** 52h/sprint (2 devs × 26h, considerando 65% de eficiência)
- **Dependências:** Grafo completo de dependências entre USs
- **Caminho crítico:** US-01 → US-06 → US-08 → US-11 → US-16
- **Feriados:** Sprint 3 e 4 com -10% de capacidade

**Problema:** O cronograma do módulo 3 usa estimativas determinísticas (um único valor por US). Para análise probabilística, precisamos de três pontos (O, M, P).

---

## Passo 1: Conversão de horas para semanas

**Fórmula:** `horas ÷ 40h/semana = semanas`

Exemplo:
- US-08: 23.4h ÷ 40 = 0.585 semanas ≈ 0.6 semanas (arredondado)

**Por que 40h/semana?** É a capacidade teórica (2 devs × 4h/dia × 5 dias), não a capacidade real por sprint (52h/sprint = 26h/pessoa).

---

## Passo 2: Definição de três pontos (O, M, P)

Para cada US, definimos:
- **O (Otimista):** Tudo corre bem, sem surpresas
- **M (Mais Provável):** Cenário esperado dado o histórico do time
- **P (Pessimista):** Algo deu errado de forma razoável (não catastrófico)

**Critério usado:** P ≈ 2× M (para capturar incerteza real)

Exemplo prático:
```
US-08 (Analista pontua documentos):
  - Effort original: 23.4h ≈ 0.6 semanas
  - O = 0.8 semanas (se visualizador PDF for simples)
  - M = 2.0 semanas (cenário esperado)
  - P = 4.0 semanas (se PDF tiver problemas de performance)
```

**Observação importante:** As primeiras estimativas que fizemos tinham P muito próximo de M (ex: US-11 com P=0.6 e M=0.55). Isso gerou variância artificialmente baixa no Monte Carlo. Ajustamos depois para ter P ≈ 2× M.

---

## Passo 3: Criação do arquivo de estimativas

Arquivo: `estimativas-tres-pontos.md`

Contém:
- Tabela com todas as 16 USs e seus três pontos
- Paralelismo do time: 2 devs, fator efetivo 1.5
- Observações sobre cada US

---

## Passo 4: Adaptação do prompt para nosso cenário

Arquivo: `probability-forecast-prompt.md`

Mudanças em relação ao template original:
- Referencia `estimativas-tres-pontos.md` ao invés de ter dados inline
- Define paralelismo: 2 devs, fator 1.5
- Mantém a estrutura de cálculo PERT e interpretação por audiência

---

## Passo 5: Criação do script Monte Carlo

Arquivo: `monte-carlo-analise-documental.py`

**O que o script faz:**
1. Sorteia duração de cada US usando distribuição triangular
2. Aplica riscos específicos:
   - 10% de chance de doença/licença por sprint (reduz capacidade pela metade)
   - 20% de chance de spike técnico na US-08 (+0.5 semanas)
   - 15% de chance de complexidade na US-11 (+0.3 semanas)
3. Aloca USs em sprints respeitando:
   - Dependências (US só começa quando deps terminam)
   - Capacidade limitada (52h/sprint)
   - Feriados (Sprint 3 e 4 com -10%)
4. Roda 10.000 simulações
5. Calcula P50, P85, P95

**Como rodar:**
```bash
python3 monte-carlo-analise-documental.py
```

---

## Passo 6: Interpretação dos resultados

**Resultado final:**
- P50: 9 sprints (18 semanas) - cenário provável
- P85: 10 sprints (20 semanas) - compromisso recomendado
- P95: 11 sprints (22 semanas) - conservador

**Distribuição:**
- 8 sprints: 21% das simulações
- 9 sprints: 44% (mais provável)
- 10 sprints: 26%
- 11 sprints: 7%

**Margem de risco:** 2 sprints de diferença entre P50 e P95

**Comparação com cronograma módulo 3:**
- Cronograma: 6 sprints (com sobrecarga) ou 7 sprints (realista)
- Monte Carlo: 9-11 sprints (mais conservador, considera riscos)

---

## Entendendo os Percentis (P50, P85, P95)

### O que são percentis?

Imagine que você rodou o projeto 10.000 vezes no Monte Carlo. Cada simulação deu um resultado diferente (7, 8, 9, 10, 11 sprints...). Os percentis mostram a distribuição desses resultados.

### Definição simples

**P50 (Percentil 50):**
- 50% das simulações terminaram em **9 sprints ou menos**
- 50% das simulações demoraram **mais de 9 sprints**
- É a **mediana** — o cenário "meio a meio"
- **Interpretação:** "Se tudo correr razoavelmente bem, termino em 9 sprints"

**P85 (Percentil 85):**
- 85% das simulações terminaram em **10 sprints ou menos**
- Apenas 15% das simulações demoraram **mais de 10 sprints**
- **Interpretação:** "Tenho 85% de chance de cumprir o prazo se prometer 10 sprints"
- **Uso:** Compromisso com cliente (alto nível de confiança)

**P95 (Percentil 95):**
- 95% das simulações terminaram em **11 sprints ou menos**
- Apenas 5% das simulações demoraram **mais de 11 sprints**
- **Interpretação:** "Tenho 95% de chance de cumprir o prazo se prometer 11 sprints"
- **Uso:** Cenário conservador (margem de segurança máxima)

### Analogia prática

```
Você vai viajar de carro para outra cidade (200km).

P50 = 2h30min
  → "Normalmente chego em 2h30, mas pode variar"

P85 = 3h00min  
  → "Se sair às 8h, tenho 85% de chance de chegar antes das 11h"

P95 = 3h30min
  → "Se tiver imprevisto (trânsito, chuva), posso levar 3h30"
```

### Aplicado ao nosso projeto

```
P50 = 9 sprints (18 semanas)
  → "Cenário provável: se tudo correr razoavelmente bem"

P85 = 10 sprints (20 semanas)
  → "Compromisso seguro: 85% de chance de cumprir"

P95 = 11 sprints (22 semanas)
  → "Conservador: margem para imprevistos graves"
```

### Qual percentil usar?

| Percentil | Confiança | Quando usar |
|-----------|-----------|-------------|
| P50 | 50% | Planejamento interno (cara ou coroa) |
| P85 | 85% | **Compromisso com cliente** (recomendado) |
| P95 | 95% | Contratos com multa por atraso |

### Recomendação para este projeto

- **Prometa ao cliente:** 10 sprints (P85)
- **Planeje internamente:** 9 sprints (P50)
- **Tenha contingência:** 11 sprints (P95)

---

## Por que o Monte Carlo é mais conservador que o cronograma?

1. **Incerteza real:** O cronograma assume effort fixo, o Monte Carlo considera variação
2. **Riscos modelados:** Doença, spike técnico, complexidade inesperada
3. **Dependências rígidas:** Se uma US do caminho crítico atrasa, todo o projeto atrasa
4. **Capacidade limitada:** Nem sempre conseguimos alocar 100% da capacidade em trabalho produtivo

---

## Lições aprendidas

1. **Estimativas apertadas subestimam risco:** Quando O, M, P são próximos, o Monte Carlo não captura variabilidade real
2. **P deve ser 2× M ou mais:** Isso reflete melhor a incerteza de projetos de software
3. **Riscos importam:** Modelar doença, spike técnico e complexidade inesperada muda o resultado de 8 para 9-11 sprints
4. **Monte Carlo > cronograma determinístico:** Para compromissos com cliente, use P85/P95, não o cenário "mais provável"

---

## Arquivos gerados

- `estimativas-tres-pontos.md` - Tabela com 16 USs e três pontos
- `probability-forecast-prompt.md` - Prompt adaptado para o AI Studio
- `monte-carlo-analise-documental.py` - Script Python com simulação probabilística
- `README.md` - Este documento

---

*Gerado em 02/10/2026*
*Baseado no cronograma do módulo 3 e template do professor Ahirton Lopes*
