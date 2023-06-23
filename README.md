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
exportados de uma planilha para um tsv, que será manipulado levando em
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

A seguir temos os dados coletados. Respectivamente, tempo de preparo de cada um
dos sabores anotados no dia da coleta de dados, e os pedidos.

- [pedidos](data/pedidos.json)
- [sabores](data/sabores.json)

## Cenário

O que vai interessar é o tempo de preparo total de cada pedido, priorizando que
todos os items de um pedido sejam entregues da forma mais simultânea possível.
