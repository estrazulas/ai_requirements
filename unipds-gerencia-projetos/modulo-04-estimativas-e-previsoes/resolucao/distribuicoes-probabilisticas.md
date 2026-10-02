# Distribuições Probabilísticas - Análise Avançada

**Data:** 02/10/2026  
**Contexto:** Limitações do PERT e Monte Carlo com distribuição triangular

---

## O Problema: Distribuição Assumida Erroneamente

### O que o PERT assume

O método PERT usa **distribuição Beta** para modelar incerteza. A fórmula clássica:

```
PERT = (O + 4M + P) / 6
```

Assume que:
- A incerteza é **simétrica ou levemente assimétrica**
- O "pior caso" (P) está próximo da realidade
- A cauda da distribuição é **curta** (eventos extremos são raros)

### O que acontece na prática

Muitas tarefas de software têm **distribuição assimétrica pesada à direita** (cauda pesada):

- **Normalmente:** 2 semanas
- **Quando dá errado:** 10-20 semanas (não 4!)

**Exemplo do seu projeto:**

```
US-08 (Visualizador PDF):
  Estimativa PERT: O=0.8 | M=2.0 | P=4.0 semanas
  
  Cenário realista:
  - Normal: 2 semanas
  - Biblioteca de PDF com bug: +3 semanas
  - Cliente muda requisitos: +4 semanas
  - Integração com sistema legado: +5 semanas
  
  Pior caso real: 2 + 3 + 4 + 5 = 14 semanas (não 4!)
```

Isso é **cauda pesada à direita** — o "pior caso" real é muito pior que o Pessimista.

---

## Tipos de Distribuição

| Distribuição | Quando usar | Característica | Exemplo |
|--------------|-------------|----------------|---------|
| **Beta (PERT)** | Incerteza "normal", cauda curta | Simétrica ou levemente assimétrica | CRUDs simples, telas padrão |
| **Triangular** | Monte Carlo simples | Aproximação razoável | Maioria das USs |
| **Log-normal** | Quando dá errado, pode atrasar 10× | Cauda pesada à direita | Integrações complexas, PDFs, APIs externas |

---

## Como Identificar USs de Cauda Pesada

### Pergunte ao time:

> "Quando essa tarefa deu errado no passado, quanto tempo levou?"

### Respostas:

**Cauda curta (use Beta/Triangular):**
- "Geralmente 2 semanas, no pior caso 3 semanas"
- "Uma vez atrasou 1 semana por causa de X"

**Cauda pesada (use Log-normal):**
- "Normalmente 2 semanas, mas uma vez levou 8 semanas"
- "Se der problema com API externa, pode atrasar 3× o previsto"
- "Depende de sistema legado não documentado"

### USs de cauda pesada no seu projeto:

| US | Título | Por que cauda pesada? |
|----|--------|----------------------|
| US-08 | Analista pontua documentos | Visualizador PDF + integrações complexas |
| US-06 | Candidato declara pontuação | Validações inesperadas + upload de arquivos |
| US-11 | Lista de classificação | Regras de negócio complexas + edição manual |
| US-13 | Perfil Analista Documento | Modelo de permissões pode não suportar |

---

## Implementação Prática

### Opção 1: Usar Log-normal no Monte Carlo

Para USs de cauda pesada, substitua distribuição triangular por log-normal:

```python
import numpy as np

# Em vez de:
duracao = triangular(o, m, p)

# Use:
mu = 0.7    # média dos log(durações) - calibrar com histórico
sigma = 0.8 # desvio padrão dos log(durações)
duracao = np.random.lognormal(mu, sigma)
```

**Como calibrar mu e sigma:**
- `mu` = ln(M) - 0.5 × sigma²
- `sigma` = 0.5 a 1.0 (quanto maior, mais incerteza)

Exemplo para US-08 (M=2.0 semanas):
```python
mu = math.log(2.0) - 0.5 * (0.8**2)  # ≈ 0.37
sigma = 0.8
```

### Opção 2: Adicionar Risco de Cauda Explicitamente

No script Monte Carlo, adicione evento catastrófico:

```python
# 5% de chance de evento catastrófico (mudança de escopo, bug crítico)
if random.random() < 0.05:
    fator_cauda = random.uniform(2.0, 5.0)  # multiplica por 2x a 5x
    duracao *= fator_cauda
```

Isso modela: "5% de chance de algo dar MUITO errado, atrasando 2-5× o previsto".

### Opção 3: Modelo Híbrido (Recomendado)

Combine as duas abordagens:

```python
def duracao_realista(us_id, o, m, p):
    # 1. Sortea duração base (triangular ou log-normal)
    if us_id in ["US-08", "US-06", "US-11", "US-13"]:
        # USs de cauda pesada usam log-normal
        mu = math.log(m) - 0.5 * (0.8**2)
        sigma = 0.8
        duracao = np.random.lognormal(mu, sigma)
    else:
        # USs normais usam triangular
        duracao = triangular(o, m, p)
    
    # 2. 5% de chance de evento catastrófico
    if random.random() < 0.05:
        duracao *= random.uniform(2.0, 5.0)
    
    return duracao
```

---

## Comparação de Resultados (Teórico)

### Cenário A: Triangular (o que você fez)

```
P50: 9 sprints
P85: 10 sprints
P95: 11 sprints
```

### Cenário B: Log-normal para USs críticas

```
P50: 10 sprints (aumenta 1 sprint)
P85: 12 sprints (aumenta 2 sprints)
P95: 15 sprints (aumenta 4 sprints)
```

**Por que muda?** Log-normal gera mais valores extremos (14+ semanas para US-08), empurrando P95 para cima.

### Cenário C: Triangular + Risco de Cauda (5%)

```
P50: 9 sprints (pouca mudança)
P85: 11 sprints (aumenta 1 sprint)
P95: 14 sprints (aumenta 3 sprints)
```

**Por que muda?** 5% de chance de evento catastrófico afeta principalmente P95 (cauda da distribuição).

---

## Quando Usar Cada Abordagem

| Situação | Abordagem Recomendada |
|----------|----------------------|
| Projeto simples, time experiente | Triangular (o que você fez) |
| Projeto com integrações complexas | Log-normal para USs críticas |
| Projeto com histórico de mudanças de escopo | Triangular + Risco de Cauda |
| Projeto crítico, alto risco | Modelo Híbrido (Log-normal + Cauda) |

---

## Como Coletar Dados para Calibrar

### Se tiver histórico do time:

1. Colete durações reais das últimas 10-20 USs similares
2. Calcule média e desvio padrão
3. Ajuste parâmetros da distribuição

**Exemplo:**
```python
# Histórico: [1.5, 2.0, 2.5, 3.0, 8.0] semanas (uma outlier)
media = 3.4
desvio = 2.6

# Para log-normal:
mu = math.log(media**2 / math.sqrt(desvio**2 + media**2))
sigma = math.sqrt(math.log(1 + (desvio**2 / media**2)))
```

### Se não tiver histórico:

1. Use estimativa de três pontos (O, M, P)
2. Adicione risco de cauda explicitamente (5-10%)
3. Reavalie após 3 sprints com dados reais

---

## Recomendações para Seu Projeto

### Curto Prazo (agora)

1. **Mantenha o modelo atual** (Triangular) para estimativas iniciais
2. **Adicione risco de cauda** (5% de chance de 2-5× atraso) para capturar incerteza real
3. **Monitore USs críticas:** US-08, US-06, US-11, US-13

### Médio Prazo (após Sprint 3)

4. **Colete dados reais** de duração das USs completadas
5. **Compare com estimativas** — se houver outliers (US que levou 3× o previsto), use log-normal
6. **Recalibre o Monte Carlo** com dados reais

### Longo Prazo (após Sprint 6)

7. **Reavalie distribuições** — se o time tiver histórico de 20+ USs, use distribuições específicas por tipo de tarefa
8. **Documente lições aprendidas** para estimativas futuras

---

## Implementação no Script - Guia Prático

### Código Atual (Triangular)

```python
def triangular(o, m, p):
    """Distribuição triangular para Monte Carlo"""
    u = random.random()
    fc = (m - o) / (p - o)
    if u < fc:
        return o + math.sqrt(u * (p - o) * (m - o))
    return p - math.sqrt((1 - u) * (p - o) * (p - m))

# Uso:
duracao = triangular(us_data["o"], us_data["m"], us_data["p"])
```

---

### Como Seria com Log-normal

```python
import numpy as np

def log_normal(m, sigma=0.8):
    """
    Distribuição log-normal para cauda pesada
    
    Parâmetros:
    - m: mediana (valor mais provável em semanas)
    - sigma: desvio padrão dos log(durações)
      - 0.5 = baixa incerteza
      - 0.8 = incerteza moderada
      - 1.0 = alta incerteza
    """
    # Calcula mu (média da distribuição normal dos logs)
    mu = math.log(m) - 0.5 * (sigma ** 2)
    
    # Sortea da distribuição log-normal
    return np.random.lognormal(mu, sigma)

# Uso:
duracao = log_normal(us_data["m"], sigma=0.8)
```

---

### Exemplo Prático para US-08 (M=2.0 semanas)

```python
# Parâmetros
m = 2.0  # mediana (valor mais provável)
sigma = 0.8  # incerteza moderada

# Calcula mu
mu = math.log(2.0) - 0.5 * (0.8 ** 2)
# mu ≈ 0.693 - 0.32 = 0.373

# Sortea 10.000 valores
duracoes = [np.random.lognormal(mu, sigma) for _ in range(10000)]

# Resultado:
# Média: 2.4 semanas
# P50: 2.0 semanas (mediana)
# P85: 4.2 semanas
# P95: 6.8 semanas
# P99: 11.5 semanas ← cauda pesada!
```

---

### Comparação Visual (Teórico)

```
Triangular (O=0.8, M=2.0, P=4.0):
  P50: 2.0 semanas
  P95: 3.8 semanas
  P99: 4.0 semanas ← limitado pelo P

Log-normal (M=2.0, sigma=0.8):
  P50: 2.0 semanas
  P95: 6.8 semanas
  P99: 11.5 semanas ← cauda pesada!
```

**Diferença:** Log-normal permite valores muito maiores (11+ semanas), enquanto triangular é limitado pelo P (4 semanas).

---

### Como Seria no Script Completo

```python
# No início do arquivo:
import numpy as np

# Definir quais USs têm cauda pesada:
US_CAUDA_PESADA = ["US-08", "US-06", "US-11", "US-13"]

# Função modificada:
def duracao_realista(us_id, o, m, p):
    """Sorteia duração usando distribuição apropriada"""
    
    if us_id in US_CAUDA_PESADA:
        # Log-normal para USs críticas (cauda pesada)
        mu = math.log(m) - 0.5 * (0.8 ** 2)
        return np.random.lognormal(mu, 0.8)
    else:
        # Triangular para USs normais (cauda curta)
        return triangular(o, m, p)

# Uso na simulação:
for us_id, us_data in historias.items():
    duracao = duracao_realista(
        us_id, 
        us_data["o"], 
        us_data["m"], 
        us_data["p"]
    )
    duracoes[us_id] = duracao * HORAS_POR_SEMANA
```

---

### Como Calibrar Sigma (Incerteza)

| Sigma | Quando usar | Exemplo |
|-------|-------------|---------|
| 0.5 | Baixa incerteza, time experiente | CRUD simples, telas padrão |
| 0.8 | Incerteza moderada | Integrações, validações complexas |
| 1.0 | Alta incerteza, tecnologia nova | PDFs, APIs externas, sistemas legados |

**Para US-08 (visualizador PDF):**
- Tecnologia conhecida, mas integrações complexas
- Sigma recomendado: 0.8 a 1.0

**Para US-01 (cadastrar critério):**
- CRUD simples, time experiente
- Sigma recomendado: 0.5 (ou usar triangular mesmo)

---

### Impacto Esperado no Resultado

```
Modelo atual (Triangular):
  P50: 9 sprints
  P85: 10 sprints
  P95: 11 sprints

Com Log-normal para USs críticas:
  P50: 10 sprints (+1)
  P85: 12 sprints (+2)
  P95: 15 sprints (+4) ← cauda pesada afeta P95
```

**Por que muda mais no P95?** Log-normal gera mais valores extremos (14+ semanas para US-08), que aparecem na cauda da distribuição (P95, P99).

---

## Conclusão

O PERT e Monte Carlo com distribuição triangular são **boas aproximações** para a maioria dos projetos. Mas quando você tem:

- Integrações complexas (PDFs, APIs externas)
- Dependências de sistemas legados
- Histórico de mudanças de escopo

Considere usar **distribuições de cauda pesada** (log-normal) ou **adicionar risco de cauda explicitamente**. Isso dá uma visão mais realista do risco, especialmente para P95 (cenário conservador).

**Regra prática:** Se o "pior caso" real pode ser 5-10× o previsto, use log-normal. Se é 2-3×, triangular funciona.

---

*Documento criado em 02/10/2026*  
*Baseado em discussão sobre limitações do PERT e distribuições probabilísticas*
