# Resultado Monte Carlo - Projeto Análise Documental

**Data:** 02/10/2026  
**Simulações:** 10.000  
**Modelo:** Com riscos (doença, spike técnico, complexidade)

---

## Configuração

- **Capacidade:** 52h/sprint (2 devs × 26h)
- **Eficiência:** 65% (4h/dia produtivas)
- **Feriados:** Sprint 3 e 4 (-10% capacidade cada)
- **Dependências:** 16 USs com grafo de dependências

---

## Riscos Modelados

| Risco | Probabilidade | Impacto |
|-------|---------------|---------|
| Doença/licença | 10% por sprint | 1 dev indisponível por 1 sprint |
| Spike técnico US-08 | 20% | +0.5 semanas |
| Complexidade US-11 | 15% | +0.3 semanas |

---

## Resultados

### Percentis

| Percentil | Sprints | Semanas | Interpretação |
|-----------|---------|---------|---------------|
| **P50** | 9 | 18 | Cenário provável |
| **P85** | 10 | 20 | **Compromisso recomendado com cliente** |
| **P95** | 11 | 22 | Conservador |
| Média | 9.2 | 18.4 | - |

### Distribuição de Sprints

| Sprints | Simulações | Percentual |
|---------|------------|------------|
| 7 | 139 | 1.4% |
| 8 | 2.096 | 21.0% |
| **9** | **4.317** | **43.2%** ← Mais provável |
| 10 | 2.658 | 26.6% |
| 11 | 682 | 6.8% |
| 12 | 100 | 1.0% |
| 13 | 8 | 0.1% |

---

## Interpretação

### Para o Time Técnico

- **Cenário mais provável (P50):** 9 sprints (18 semanas)
- **Margem de risco:** 2 sprints entre P50 e P95
- **Principal driver de risco:** US-08 (visualizador PDF) com spike técnico em 20% das simulações

### Para o Gestor de Produto

- **Prazo recomendado:** 10 sprints (20 semanas) com 85% de confiança
- **Risco de não cumprir:** 15% se comprometer com 10 sprints
- **Principal risco:** Doença/licença de um dev (10% por sprint)

### Para o Executivo

- **Prazo:** 20 semanas (5 meses)
- **Risco:** 15% de chance de atrasar além de 20 semanas
- **Buffer de contingência:** 2 semanas (entre cenário provável e conservador)

### Para o Cliente

- **Previsão de entrega:** 20 semanas (5 meses)
- **O que pode impactar:** Problemas técnicos no visualizador de PDF, indisponibilidade do time, complexidade inesperada na lista de classificação

---

## Comparação com Cronograma Módulo 3

| Aspecto | Cronograma M3 | Monte Carlo M4 |
|---------|---------------|----------------|
| Duração | 6-7 sprints | 9-11 sprints |
| Abordagem | Determinística | Probabilística |
| Considera riscos | Não | Sim |
| Considera incerteza | Não | Sim |
| Recomendado para | Planejamento interno | Compromisso com cliente |

**Por que Monte Carlo é mais conservador?**
1. Captura incerteza real das estimativas (O, M, P)
2. Modela riscos (doença, spike técnico, complexidade)
3. Considera dependências rígidas no caminho crítico
4. Mostra variabilidade, não apenas cenário "ideal"

---

## Recomendações

### Curto Prazo (Sprint 1-3)

1. **Validar viabilidade técnica do visualizador PDF** (US-08) antes do Sprint 3
   - Se houver spike técnico, o projeto pode atrasar 0.5 semanas
   - Mitigação: PoC ou pesquisa antecipada

2. **Monitorar saúde do time**
   - 10% de chance de doença por sprint
   - Mitigação: Ter documentação atualizada para outro dev assumir

### Médio Prazo (Sprint 4-6)

3. **Comprometer-se com 10 sprints (P85)**
   - 85% de chance de cumprir
   - Buffer de 1 sprint além do cenário provável

4. **Preparar plano de contingência**
   - Se US-11 (lista de classificação) for mais complexa, pode atrasar 0.3 semanas
   - Mitigação: Simplificar edição manual se necessário

### Longo Prazo (Sprint 7-10)

5. **Reavaliar a cada 3 sprints**
   - Rodar Monte Carlo novamente com dados reais de velocidade do time
   - Ajustar estimativas conforme aprendizado

---

## Como Reproduzir

```bash
cd modulo-04-estimativas-e-previsoes/resolucao
python3 monte-carlo-analise-documental.py
```

**Arquivos de entrada:**
- `estimativas-tres-pontos.md` - Três pontos das 16 USs
- `monte-carlo-analise-documental.py` - Script de simulação

---

## Lições Aprendidas

1. **Estimativas apertadas subestimam risco:** Quando O, M, P são próximos, o Monte Carlo não captura variabilidade real
2. **P deve ser 2× M ou mais:** Reflete melhor a incerteza de projetos de software
3. **Riscos importam:** Modelar doença, spike técnico e complexidade muda o resultado de 8 para 9-11 sprints
4. **Monte Carlo > cronograma determinístico:** Para compromissos com cliente, use P85/P95, não o cenário "mais provável"

---

*Gerado em 02/10/2026*  
*Baseado no template do Prof. Ahirton Lopes - PM AI Toolkit*
