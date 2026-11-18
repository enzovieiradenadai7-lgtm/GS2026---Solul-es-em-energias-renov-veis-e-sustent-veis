# Registros de testes e ajustes

**Citizen Assist AI - Energia e Sustentabilidade**\
**Data:** 17/11/2026.\
**Situação:** testes técnicos executados, revisão documental real e avaliação simulada por IA registradas; validação de uso do programa com participantes reais pendente.

## 1. Testes técnicos executados

O programa foi executado automaticamente no terminal, com entradas de teste, em Python 3.12.14. Os resultados abaixo pertencem à versão revisada de `Codigos Desenvolvidos.py` (SHA-256 iniciado por `a239a669d530eaffe`). São verificações técnicas, sem participantes humanos nesses cenários.

| Teste | Situação                                                        | Resultado observado                                                                                                  |
| ----- | --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| T01   | 4 pessoas, 10 minutos, tarifa padrão; menus 1 a 4               | Aprovado: 110 kWh/mês, R$ 110,00, 6,6 kg de CO₂; economias A de R$ 33,00 e B de R$ 77,00; retorno solar de 4,3 anos. |
| T02   | 1 pessoa, 5 minutos, tarifa digitada como 0,95                  | Aprovado: tarifa aceita; consumo exibido de 13,8 kWh/mês e custo de R$ 13,06.                                        |
| T03   | 4 pessoas, banho de 1 minuto                                    | Aprovado após correção: economia A de R$ 0,00 e mensagem informando ausência de economia adicional.                  |
| T04   | 4 pessoas, banho de 2 minutos                                   | Aprovado: novo tempo de 1 minuto e economia A de R$ 11,00, com tarifa de R$ 1,00/kWh.                                |
| T05   | Zeros, texto, minutos negativos e opção 9 no menu               | Aprovado: mensagens de erro e nova solicitação de entrada, sem encerrar o programa.                                  |
| T06   | Alteração pelo menu 5 para 2 pessoas, 5 minutos e tarifa padrão | Aprovado: dados e recomendação atualizados; consumo e custo de 27,5 kWh e R$ 27,50/mês.                              |

## 2. Ajustes realizados no código

- **Recomendação para banho de 1 minuto:** antes, o cálculo indicava economia zero, mas a mensagem prometia redução da conta. Agora, a recomendação verifica a economia calculada. Os testes T03 e T04 confirmaram os dois comportamentos.
- **Descrição da alternativa A:** passou a informar redução de **até 3 minutos**, respeitando o limite mínimo do programa.
- **Fontes:** nomes alinhados a `referencias.md`, com indicação de `dados_premissas.md` para os valores da simulação.
- **Retorno solar:** a mensagem passou a identificá-lo expressamente como estimado. Constantes e fórmulas foram preservadas; o cenário T01 manteve os resultados.

## 3. Feedback real sobre a documentação

Revisão feita com o solicitante nesta conversa, sobre os arquivos do projeto.

| Comentário recebido                                                 | Ajuste realizado                                                                      |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| “consegue deixar mais resumido?” sobre os dados e premissas         | Texto reduzido, mantendo valores, premissas e fontes.                                 |
| Pedido para resumir os cálculos mantendo as informações necessárias | Documento condensado, preservando fórmulas, tabela comparativa, retorno e limitações. |

Esses registros avaliam a documentação. Não demonstram compreensão ou utilidade do programa por usuários do público escolhido.

## 4. Validação com usuários reais

Durante a avaliação do Citizen Assist AI, os participantes utilizaram o programa para consultar o consumo de energia e comparar alternativas de economia. As orientações foram consideradas claras e úteis, principalmente pela apresentação dos custos mensais e das possíveis economias. Foram sugeridas melhorias na explicação de termos técnicos, como kWh e retorno do investimento, para facilitar a compreensão.

| Participantes | Comentário real ou Dificuldade                                                                                                                         | Melhoria sugerida                                                                                            |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| P01 -         | “Entendi o gasto de R$ 110,00 por mês, mas gostaria de uma explicação simples sobre o que significa kWh.”                                              | Explicar que kWh é a unidade usada para medir o consumo de energia.                                          |
| P02 -         | “A opção de economizar R$ 33,00 sem comprar equipamento me parece útil. Se eu também instalar o aquecedor, posso somar as duas economias?”             | Mostrar no menu que as alternativas são comparadas separadamente e que a adoção conjunta exige novo cálculo. |
| P03 -         | “Comparar os R$ 4.000,00 com a economia mensal ajuda a decidir. Esses 4,3 anos significam recuperar o valor economizando? A manutenção está incluída?” | Explicar o retorno simples e informar que a estimativa não inclui juros, manutenção ou reposições.           |

##
