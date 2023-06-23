```
                          UIVERSIDADE FEDERAL DO PARÁ
                    Instituto de Ciências Exatas e Naturais
                            Faculdade de Computação

                         EN05225 - SIMULAÇÃO DISCRETA
                                   Prova II


      Alunos:
        1. Jose Carlos Noronha Ferreira - 201804940020
        2. Marcos Eduardo Nascimento Lima - 201804940007
```

# Prova 2 - Simulação discreta

Simulação de um problema discreto do mundo real.

## O problema

Fila de preparo de cozinha de uma lanchonete.

Dado a limitação de trabalho simultâneo, quantos pedidos podem ser preparados
ao mesmo tempo, na cozinha de uma lanchonete da região, resolvemos simular o
modelo de trabalho atual em busca de melhorias. E caso não fossem encontrados
pontos de melhoria, um cenário futuro de atendimento seria modelado, indicar
qual seria o momento ideal para, por exemplo aumentar a equipe.

## Base de dados

A tomada de dados ocorreu no sábado 17/06/2023, um dos dias e horários mais
intensos, segundo os colaboradores do local.

Nesse intervalo, foram coletados 91 pedidos de clientes distintos, com uma
média de 3 items por pedido.

Cada tipo de item do pedido pode ter um tempo diferente para preparo. Por
exemplo, a tapioca simples, com manteiga, demora cerca de 2 minutos para ser
preparada. Já a tapioca com queijo leva 1 minuto a mais (3 minutos).

Os tempos foram foram baseados a partir da chegada do primeiro cliente, dado a
característica da tomada de dados ser linear, durante o período estabelecido,
entre as 6:30 e 12:30, não achamos que seria necessário tomar nota do horário
preciso. Utilizando assim um cronometro, marcando os minutos a partir da
chegada do primeiro cliente.

### Schemas

Para representar os dados coletados e facilitar a manipulação, eles foram
exportados de uma planilha para o formato json, que será manipulado levando em
consideração o seguinte schema.

```python
Pedido(
  tempo_chegada='1',
  numero_pedido='1',
  items=[
    Sabor(nome='queijo', minutos_preparo='3'),
    Sabor(nome='manteiga', minutos_preparo='2')
  ]
)
```

### Os dados

A seguir os links para os arquivos com os dados coletados.

- [pedidos](data/pedidos.json)
- [sabores](data/sabores.json)

## Cenário

**As observações se concentraram na observação do tempo de preparo**. Levando
em consideração que no dia das anotações apenas uma pessoa estava preparando os
pedidos, e sua capacidade de preparo simultâneo é de 3 items, as seguintes
observações foram feitas sobre os dados.

- qual a quantidade média de items por pedido?
- qual o tempo médio de preparo dos pedidos?
- faria sentido parar de priorizar o preparo por pedido e utilizar o preparo
  por tipo de item. Priorizar o items que demoram mais?

Durante a coleta inicial de informações, resolvemos perguntar aos colaboradores
e proprietários do estabelecimento qual eram as principais preocupações
relacionados ao preparo dos pedidos, as principais foram:

- qualidade do preparo
- tempo de preparo
- todos os items do pedido chegarem ao mesmo tempo

Uma melhoria futura que pode ser aplicada ao modelo é o incremento de outras
variáveis que possam impactar na experiência de atendimento do cliente, tal
como o tempo que um atendente demora para anotar os pedidos, ou no caso em
questão, o tempo que o cliente ficaria na fila, para pagar no caixa.
