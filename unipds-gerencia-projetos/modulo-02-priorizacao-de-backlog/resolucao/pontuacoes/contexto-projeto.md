# Contexto da Equipe — Projeto Análise Documental

**Última atualização:** 25/09/2026

---

## 1. Velocidade Histórica

- **Story points por sprint (2 semanas):** 120 pontos (60 pts/semana)
- **Capacidade em pessoa-mês:** ~8.0 pm por sprint (calculado com âncora CRUD=0.2pm/3pts)
- **Composição da equipe:** não informada
- **Buffer para atividades não-código:** não informado

---

## 2. Volume de Usuários/Transações

- **Editais processados por mês:** 10 editais
- **Candidatos por mês:** 2000 inscrições
- **Picos sazonais:** não informados

---

## 3. Histórico com Features Similares

| Feature | Esforço Real | Observações |
|---------|--------------|-------------|
| CRUD simples | 0.2 pm (4 dias) | Sem integrações externas |
| CRUD médio | 0.3-0.4 pm | Com validações e campos condicionais |
| CRUD complexo | 0.5-0.6 pm | Com cálculos e múltiplas validações |
| Tela processamento complexa | 0.8-1.2 pm | Com visualizador PDF e auditoria |

---

## 4. Prazos Externos e Regulatórios

| Prazo | Descrição | Impacto |
|-------|-----------|---------|
| Sem prazo | Sem deadline explícito por lei | TC moderado (4) |

---

## 5. Dependências Externas Conhecidas

- **Base existente (ENEM):** reaproveitamento não mapeado — adicionar buffer
- **Visualizador PDF inline:** validação técnica pendente
- **Modelo de permissões:** pode não suportar vinculação granular por oferta

---

## 6. Restrições Técnicas

- **Visualizador PDF inline:** biblioteca/componente precisa validação
- **Modelo de permissões:** vinculação por oferta vs. unidade precisa verificação
- **Base ENEM:** reaproveitamento não documentado

---

## 7. Escala de Complexidade Utilizada

| Categoria | Simples | Médio | Complexo |
|-----------|---------|-------|----------|
| CRUDs / Cadastros | 0.2 | 0.3-0.4 | 0.5-0.6 |
| Telas de Processamento | 0.2-0.3 | 0.4-0.5 | 0.8-1.2 |
| Entrada de Dados | 0.2 | 0.3-0.4 | 0.5-0.6 |
| Listas e Relatórios | 0.2 | 0.3-0.5 | 0.5-0.7 |
| Portal / Autoatendimento | 0.2 | 0.3-0.4 | 0.5-0.6 |

---

*Atualizado pela skill backlog-scorer-skill*
