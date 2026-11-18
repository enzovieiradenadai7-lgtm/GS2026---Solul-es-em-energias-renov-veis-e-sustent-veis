# Cálculos e comparação das alternativas

**Citizen Assist AI - Módulo de Energia e Sustentabilidade**

## 1. Cenário de referência

Consideram-se **4 pessoas**, um banho diário por pessoa, **10 minutos por banho** e **30 dias**. O chuveiro tem potência constante de **5.500 W (5,5 kW)**, a tarifa é **R$ 1,00/kWh** e o fator de emissão adotado é **0,06 kg de CO₂/kWh**.

Os cálculos reproduzem o código `Codigos Desenvolvidos.py`. A origem dos parâmetros e as hipóteses estão documentadas em `dados_premissas.md`.

## 2. Situação atual

Usa-se a relação: energia (kWh) = potência (kW) × tempo (h).

```text
Consumo = 5,5 × 4 × (10 / 60) × 30 = 110 kWh/mês
Custo = 110 × 1,00 = R$ 110,00/mês
CO₂ estimado = 110 × 0,06 = 6,60 kg/mês
```

## 3. Alternativa A: banho mais curto

Reduzir até 3 minutos por banho, mantendo o mínimo de 1 minuto. Neste cenário, o banho passa de 10 para **7 minutos**, sem investimento inicial.

```text
Novo consumo = 5,5 × 4 × (7 / 60) × 30 = 77 kWh/mês
Energia economizada = 110 - 77 = 33 kWh/mês
Economia financeira = 33 × 1,00 = R$ 33,00/mês
CO₂ evitado estimado = 33 × 0,06 = 1,98 kg/mês
```

A redução do consumo é de **30%**. Pressupõe-se que o usuário consiga atender à necessidade de higiene com um banho mais curto.

## 4. Alternativa B: aquecimento solar de água

Considera-se, como hipótese, que o aquecimento solar térmico substitua **70% da eletricidade** usada no chuveiro. O banho permanece com 10 minutos e os outros 30% dependem de apoio elétrico. O investimento estimado é de **R$ 4.000,00**, incluindo equipamento e instalação no cenário simulado.

```text
Energia elétrica economizada = 110 × 0,70 = 77 kWh/mês
Consumo elétrico restante = 110 - 77 = 33 kWh/mês
Economia financeira = 77 × 1,00 = R$ 77,00/mês
CO₂ evitado estimado = 77 × 0,06 = 4,62 kg/mês
Retorno simples = 4.000 / 77 ≈ 51,95 meses
Retorno em anos = 51,95 / 12 ≈ 4,33 anos
```

## 5. Comparação no mesmo período de 30 dias

| Indicador | Situação atual | A: banho mais curto | B: aquecimento solar |
|---|---|---|---|
| Tempo de cada banho | 10 min | 7 min | 10 min |
| Consumo elétrico | 110 kWh | 77 kWh | 33 kWh |
| Custo da eletricidade | R$ 110,00 | R$ 77,00 | R$ 33,00 |
| Economia financeira | Referência | R$ 33,00 | R$ 77,00 |
| Redução do consumo elétrico | Referência | 30% | 70% |
| CO₂ indireto estimado | 6,60 kg | 4,62 kg | 1,98 kg |
| CO₂ evitado estimado | Referência | 1,98 kg | 4,62 kg |
| Investimento adicional | Não considerado | R$ 0,00 | R$ 4.000,00 |
| Retorno simples | Não se aplica | Sem investimento inicial | Aproximadamente 4,3 anos |

## 6. Interpretação e limitações

- **A:** permite economizar sem comprar equipamento, dependendo da mudança de hábito.
- **B:** apresenta maior economia neste cenário. Seu retorno estimado é inferior ao limite de 72 meses adotado no código, mas a instalação depende de espaço adequado, condições solares, dimensionamento e orçamento real.
- As alternativas são comparadas separadamente com a situação atual. **As economias não devem ser somadas diretamente.**
- Os custos representam somente a eletricidade do chuveiro. O retorno simples desconsidera juros e manutenção; as emissões estimadas não incluem fabricação ou instalação dos equipamentos.
- Os resultados dependem das hipóteses adotadas e não são garantidos. No terminal, o CO₂ evitado aparece arredondado para **2,0 kg** em A e **4,6 kg** em B, e o retorno para **4,3 anos**.
