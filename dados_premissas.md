# Dados utilizados e premissas

**Citizen Assist AI - Módulo de Energia e Sustentabilidade**

O programa utiliza informações do usuário e valores de simulação para estimar o consumo do chuveiro. Os resultados não são medições reais.

## 1. Dados informados pelo usuário

- **Pessoas na residência:** número inteiro maior que zero.
- **Duração média do banho:** minutos inteiros, maiores que zero.
- **Tarifa de energia:** valor em R$/kWh, preferencialmente consultado na conta de luz. Ao pressionar Enter sem preencher, o programa usa R$ 1,00/kWh.

## 2. Valores utilizados

| Dado | Valor | Origem e justificativa |
|---|---|---|
| Potência do chuveiro | 5.500 W = 5,5 kW | Potência escolhida para a simulação, existente em uma versão da Bella Ducha 4T Ultra [1]. |
| Período | 30 dias | Mês padronizado para comparar as alternativas. |
| Tarifa padrão | R$ 1,00/kWh | Hipótese para executar o programa sem informar uma tarifa real. |
| Fator de emissão | 0,06 kg de CO₂/kWh | Hipótese didática; sem mês ou ano oficial associado. |
| Redução do banho | Até 3 minutos | Regra da alternativa A, mantendo o mínimo de 1 minuto. |
| Fração solar | 70% | Hipótese de substituição de parte da eletricidade por aquecimento solar de água. |
| Investimento solar | R$ 4.000,00 | Hipótese para equipamento e instalação, sem orçamento de fornecedor. |
| Limite de retorno | 72 meses | Critério interno do programa para recomendar a alternativa solar. |

## 3. Premissas e limitações

- Considera-se **um banho por pessoa por dia**, com duração média igual para todos, potência constante e tarifa fixa durante 30 dias.
- O custo calculado corresponde somente à eletricidade do chuveiro.
- A alternativa A tem investimento zero. Se o banho já dura 1 minuto, ela não gera economia adicional.
- A alternativa B utiliza energia solar térmica, mantendo 30% de apoio elétrico. Os 70% não representam eficiência do coletor.
- As alternativas são comparadas separadamente. Suas economias não devem ser somadas diretamente.
- O retorno é simples: investimento dividido pela economia mensal, sem juros ou manutenção.
- O CO₂ representa emissões indiretas estimadas da eletricidade, sem avaliação de ciclo de vida.
- Não há dimensionamento solar. Clima, instalação, equipamento e tarifa real podem alterar os resultados.

## 4. Fórmulas básicas

```text
Consumo (kWh/mês) = 5,5 × pessoas × (minutos / 60) × 30
Custo (R$/mês) = consumo × tarifa
CO₂ (kg/mês) = consumo × 0,06
```

**Exemplo:** 4 pessoas, banhos de 10 minutos e tarifa de R$ 1,00/kWh resultam em 110 kWh/mês, R$ 110,00/mês e 6,6 kg de CO₂/mês.

## 5. Referências

Consultadas em 17/11/2026. As fontes contextualizam os cálculos; os valores identificados como hipóteses não foram comprovados por elas.

1. [Lorenzetti - Bella Ducha 4T Ultra](https://www.lorenzetti.com.br/produto/bella-ducha-4t): referência para a potência de 5.500 W.
2. [ANEEL - Ranking das Tarifas](https://www.gov.br/aneel/pt-br/assuntos/tarifas/ranking-das-tarifas): consulta de tarifas e componentes da conta.
3. [MCTI - Fatores de emissão de CO₂](https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/noticias/2024/02/fator-de-emissao-de-co2-na-geracao-de-energia-eletrica-no-brasil-em-2023-e-o-menor-em-12-anos): referência conceitual sobre emissões da eletricidade.
4. [Inmetro - Aquecimento solar de água](https://www.gov.br/inmetro/pt-br/assuntos/regulamentacao/avaliacao-da-conformidade/programa-brasileiro-de-etiquetagem/tabelas-de-eficiencia-energetica/equipamentos-de-aquecimento-solar-de-agua): consulta de equipamentos e desempenho.
