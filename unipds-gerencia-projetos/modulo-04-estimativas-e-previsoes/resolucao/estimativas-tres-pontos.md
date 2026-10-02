# Estimativas de Três Pontos - Projeto Análise Documental

**Data:** 02/10/2026  
**Baseado em:** Cronograma Módulo 3 (cronograma-sprints-atualizado.md)

---

## Tabela de Estimativas

| ID | Título | O (sem) | M (sem) | P (sem) | Observações |
|----|--------|---------|---------|---------|-------------|
| US-01 | Cadastrar critério "Análise Documental" no edital | 0.1 | 0.14 | 0.3 | CRUD simples de configuração |
| US-02 | Configurar pesos de entrevista no edital | 0.15 | 0.3 | 0.6 | Depende de US-01 |
| US-03 | Cadastrar calendário de etapa por edital | 0.25 | 0.4 | 0.8 | Calendário com regras de datas |
| US-04 | Cadastrar calendário de etapa por curso/oferta | 0.25 | 0.4 | 0.8 | Similar à US-03, mas por oferta |
| US-05 | Configurar tipo de documento com pontuação | 0.1 | 0.15 | 0.35 | CRUD simples |
| US-06 | Candidato declara pontuação ao enviar documentos | 0.4 | 0.6 | 1.5 | Upload + validação + cálculo em tempo real |
| US-07 | Candidato altera documentos e pontuação dentro do prazo | 0.25 | 0.5 | 1.2 | Depende de US-06 |
| US-08 | Analista pontua documentos do candidato | 0.8 | 2.0 | 4.0 | Visualizador PDF + cálculo + auditoria |
| US-09 | Analista pontua entrevista do candidato | 0.15 | 0.21 | 0.5 | Depende de US-02 e US-08 |
| US-10 | Analista desclassifica candidato | 0.08 | 0.14 | 0.3 | Ação simples |
| US-11 | Lista de classificação com edição manual | 0.4 | 0.55 | 1.2 | Ordenação + edição + recálculo |
| US-12 | Exportar classificação em CSV e HTML | 0.2 | 0.34 | 0.7 | Depende de US-11 |
| US-13 | Perfil "Analista de Documento" | 0.2 | 0.34 | 0.7 | Novo perfil + vinculação a oferta |
| US-14 | Candidato interpõe recurso pelo portal | 0.2 | 0.34 | 0.7 | Formulário + upload de anexos |
| US-15 | Analista julga recurso | 0.3 | 0.55 | 1.0 | Múltiplas visualizações + decisão |
| US-16 | Candidato visualiza status e pontuação no portal | 0.2 | 0.34 | 0.7 | Depende de US-10 e US-11 |

---

## Paralelismo do Time

- **Número de desenvolvedores:** 2 devs seniores
- **Fator de paralelismo efetivo:** 1.5 (dependências sequenciais no caminho crítico)

---

## Observações

- Estimativas baseadas no effort em horas do cronograma do Módulo 3
- Conversão: horas ÷ 40h/semana = semanas
- US-08 tem maior variância devido à complexidade do visualizador PDF
- USs dependentes do caminho crítico (US-06, US-08, US-11) têm maior incerteza

---

*Gerado em 02/10/2026*
