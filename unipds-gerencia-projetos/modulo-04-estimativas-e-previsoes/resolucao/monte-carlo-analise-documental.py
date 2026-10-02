#!/usr/bin/env python3
"""
Monte Carlo - Projeto Análise Documental (Modelo com Riscos)
Simulação probabilística com capacidade, dependências, feriados e riscos

Como usar:
    python3 monte-carlo-analise-documental.py

Riscos modelados:
  1. Doença/licença: 10% de chance por sprint de um dev ficar 1 semana indisponível
  2. Spike técnico US-08: 20% de chance de visualizador PDF exigir spike (+0.5 semanas)
  3. Complexidade US-11: 15% de chance de edição manual ser mais complexa (+0.3 semanas)
"""

import random
import math

# Estimativas de três pontos (O, M, P) em SEMANAS
# Ajustadas com maior variância para capturar incerteza real
historias = {
    "US-01": {"nome": "Cadastrar critério AD", "o": 0.1, "m": 0.14, "p": 0.3, "deps": []},
    "US-02": {"nome": "Configurar pesos entrevista", "o": 0.15, "m": 0.3, "p": 0.6, "deps": ["US-01"]},
    "US-03": {"nome": "Calendário etapa por edital", "o": 0.25, "m": 0.4, "p": 0.8, "deps": []},
    "US-04": {"nome": "Calendário etapa por oferta", "o": 0.25, "m": 0.4, "p": 0.8, "deps": []},
    "US-05": {"nome": "Configurar tipo documento", "o": 0.1, "m": 0.15, "p": 0.35, "deps": []},
    "US-06": {"nome": "Candidato declara pontuação", "o": 0.4, "m": 0.6, "p": 1.5, "deps": ["US-01", "US-05"]},
    "US-07": {"nome": "Candidato altera documentos", "o": 0.25, "m": 0.5, "p": 1.2, "deps": ["US-06"]},
    "US-08": {"nome": "Analista pontua documentos", "o": 0.8, "m": 2.0, "p": 4.0, "deps": ["US-06", "US-13"]},
    "US-09": {"nome": "Analista pontua entrevista", "o": 0.15, "m": 0.21, "p": 0.5, "deps": ["US-02", "US-08"]},
    "US-10": {"nome": "Analista desclassifica", "o": 0.08, "m": 0.14, "p": 0.3, "deps": ["US-08"]},
    "US-11": {"nome": "Lista classificação", "o": 0.4, "m": 0.55, "p": 1.2, "deps": ["US-08", "US-09"]},
    "US-12": {"nome": "Exportar classificação", "o": 0.2, "m": 0.34, "p": 0.7, "deps": ["US-11"]},
    "US-13": {"nome": "Perfil Analista Documento", "o": 0.2, "m": 0.34, "p": 0.7, "deps": []},
    "US-14": {"nome": "Candidato interpõe recurso", "o": 0.2, "m": 0.34, "p": 0.7, "deps": ["US-03"]},
    "US-15": {"nome": "Analista julga recurso", "o": 0.3, "m": 0.55, "p": 1.0, "deps": ["US-14", "US-08"]},
    "US-16": {"nome": "Candidato visualiza status", "o": 0.2, "m": 0.34, "p": 0.7, "deps": ["US-10", "US-11"]},
}

# Capacidade do time
CAPACIDADE_POR_SPRINT = 52  # horas/sprint (2 devs × 26h)
HORAS_POR_SEMANA = 40

# Feriados
FERIADOS = {
    3: 0.10,  # Sprint 3: 02/11
    4: 0.10,  # Sprint 4: 20/11
}

# Riscos
RISCO_DOENCA_POR_SPRINT = 0.10  # 10% de chance de um dev ficar 1 semana indisponível
RISCO_SPIKE_US08 = 0.20  # 20% de chance de US-08 precisar de spike técnico
RISCO_COMPLEXIDADE_US11 = 0.15  # 15% de chance de US-11 ser mais complexa
ADICAO_SPIKE_US08 = 0.5  # semanas adicionais se spike ocorrer
ADICAO_COMPLEXIDADE_US11 = 0.3  # semanas adicionais se complexidade ocorrer

N = 10_000

def triangular(o, m, p):
    """Distribuição triangular para Monte Carlo"""
    u = random.random()
    fc = (m - o) / (p - o)
    if u < fc:
        return o + math.sqrt(u * (p - o) * (m - o))
    return p - math.sqrt((1 - u) * (p - o) * (p - m))

def capacidade_sprint(num_sprint):
    """Retorna capacidade do sprint considerando feriados"""
    cap = CAPACIDADE_POR_SPRINT
    if num_sprint in FERIADOS:
        cap *= (1 - FERIADOS[num_sprint])
    return cap

def simular_projeto():
    """Simula uma execução do projeto com riscos"""
    
    # Sorteia duração base de cada US
    duracoes = {}
    for us_id, us_data in historias.items():
        duracao_semanas = triangular(us_data["o"], us_data["m"], us_data["p"])
        duracao_horas = duracao_semanas * HORAS_POR_SEMANA
        duracoes[us_id] = duracao_horas
    
    # Aplica riscos específicos
    # Risco 1: Spike técnico na US-08
    if random.random() < RISCO_SPIKE_US08:
        duracoes["US-08"] += ADICAO_SPIKE_US08 * HORAS_POR_SEMANA
    
    # Risco 2: Complexidade na US-11
    if random.random() < RISCO_COMPLEXIDADE_US11:
        duracoes["US-11"] += ADICAO_COMPLEXIDADE_US11 * HORAS_POR_SEMANA
    
    # Estado da simulação
    horas_restantes = duracoes.copy()
    uss_completadas = set()
    sprint_atual = 1
    dev_disponivel = 2  # começa com 2 devs
    
    while len(uss_completadas) < len(historias):
        # Risco 3: Doença/licença (verifica no início de cada sprint)
        if sprint_atual > 1 and random.random() < RISCO_DOENCA_POR_SPRINT:
            dev_disponivel = 1  # um dev fica indisponível por 1 sprint
        else:
            dev_disponivel = 2  # volta ao normal
        
        # Calcula capacidade considerando devs disponíveis
        cap_base = capacidade_sprint(sprint_atual)
        cap_disponivel = cap_base * (dev_disponivel / 2)  # reduz se 1 dev indisponível
        
        cap_usada = 0
        
        # Lista de USs prontas para iniciar
        uss_prontas = [
            us_id for us_id in historias.keys()
            if us_id not in uss_completadas and
               horas_restantes[us_id] > 0 and
               all(dep in uss_completadas for dep in historias[us_id]["deps"])
        ]
        
        # Aloca USs prontas
        for us_id in uss_prontas:
            if cap_usada >= cap_disponivel:
                break
            
            horas_disponiveis = cap_disponivel - cap_usada
            horas_trabalhadas = min(horas_restantes[us_id], horas_disponiveis)
            
            horas_restantes[us_id] -= horas_trabalhadas
            cap_usada += horas_trabalhadas
            
            if horas_restantes[us_id] <= 0:
                uss_completadas.add(us_id)
        
        sprint_atual += 1
        
        if sprint_atual > 50:
            break
    
    return sprint_atual - 1

# Executa simulações
totais = []
eventos_risco = {"doenca": 0, "spike_us08": 0, "complexidade_us11": 0}

for _ in range(N):
    # Rastreia ocorrência de riscos
    if random.random() < RISCO_DOENCA_POR_SPRINT:
        eventos_risco["doenca"] += 1
    if random.random() < RISCO_SPIKE_US08:
        eventos_risco["spike_us08"] += 1
    if random.random() < RISCO_COMPLEXIDADE_US11:
        eventos_risco["complexidade_us11"] += 1
    
    sprints = simular_projeto()
    totais.append(sprints)

# Calcula estatísticas
totais.sort()
percentil = lambda pct: totais[int(pct * N / 100)]
media = sum(totais) / N

# Output
print("=" * 70)
print("Monte Carlo - Projeto Análise Documental (Com Riscos)")
print(f"{N:,} simulações com capacidade, dependências, feriados e riscos")
print("=" * 70)
print()
print("Configuração:")
print(f"  - Capacidade: {CAPACIDADE_POR_SPRINT}h/sprint (2 devs × 26h)")
print(f"  - Feriados: Sprint 3 e 4 (-10% capacidade)")
print()
print("Riscos modelados:")
print(f"  - Doença/licença: {RISCO_DOENCA_POR_SPRINT*100:.0f}% chance/sprint de 1 dev indisponível")
print(f"  - Spike técnico US-08: {RISCO_SPIKE_US08*100:.0f}% chance (+{ADICAO_SPIKE_US08} semanas)")
print(f"  - Complexidade US-11: {RISCO_COMPLEXIDADE_US11*100:.0f}% chance (+{ADICAO_COMPLEXIDADE_US11} semanas)")
print()
print(f"P50 (cenário provável):        {percentil(50)} sprints ({percentil(50)*2} semanas)")
print(f"P85 (compromisso com cliente): {percentil(85)} sprints ({percentil(85)*2} semanas)")
print(f"P95 (conservador):             {percentil(95)} sprints ({percentil(95)*2} semanas)")
print(f"Média:                         {media:.1f} sprints ({media*2:.1f} semanas)")
print()
print("Distribuição de sprints:")
for sprints in sorted(set(totais))[:12]:
    count = totais.count(sprints)
    pct = count / N * 100
    print(f"  {sprints:2d} sprints: {count:5,} simulações ({pct:5.1f}%)")
print()
print("Interpretação:")
print(f"  - 50% de chance de terminar em até {percentil(50)} sprints")
print(f"  - 85% de chance de terminar em até {percentil(85)} sprints (recomendado)")
print(f"  - 95% de chance de terminar em até {percentil(95)} sprints (conservador)")
print()
print("Análise de risco:")
print(f"  - O P50 é {percentil(50)} sprints e o P95 é {percentil(95)} sprints")
print(f"  - Diferença P95-P50: {percentil(95) - percentil(50)} sprints de margem de risco")
