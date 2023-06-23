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
{
  numero: 1,
  tempo_chegada_cliente: 4,
  items: [
    {
      sabor: 'queijo',
      minutos_preparo: 3
    },
    {
      sabor: 'manteiga',
      minutos_preparo: 2
    },
  ],
  minutos_preparo: 5
}
```

### Os dados

A seguir temos os dados coletados. Respectivamente, tempo de preparo de cada um
dos sabores anotados no dia da coleta de dados, e os pedidos.

```tsv
sabor	minutos_preparo
Queijo	3
Manteiga	2
Ovo	3
Carne	5
Molhada	3
Frango	5
```

```tsv
tempo_chegada	numero_pedido	items
1	1	Queijo, Manteiga
2	2	Ovo, Queijo, Molhada
3	3	Carne, Queijo, Manteiga
10	4	Frango, Queijo, Manteiga, Ovo
15	5	Queijo
17	6	Manteiga, Ovo, Molhada
18	7	Ovo, Queijo
18	8	Carne, Frango, Manteiga, Ovo, Queijo
20	9	Ovo, Manteiga, Molhada
21	10	Carne, Queijo
25	11	Frango, Queijo, Manteiga, Ovo
35	12	Queijo, Manteiga, Molhada
36	13	Ovo, Frango
37	14	Carne, Queijo, Ovo, Manteiga
40	15	Manteiga, Molhada
42	16	Queijo, Ovo, Manteiga
43	17	Carne, Frango, Ovo, Queijo
44	18	Manteiga, Ovo
44	19	Frango, Queijo, Manteiga
45	20	Queijo, Manteiga, Molhada
60	21	Ovo, Carne, Queijo, Manteiga(2
62	22	Frango, Manteiga, Ovo, Queijo
63	23	Carne, Manteiga
64	24	Ovo, Molhada, Frango, Queijo, Manteiga
67	25	Queijo, Ovo, Manteiga, Molhada
69	26	Carne, Frango
70	27	Queijo, Manteiga, Ovo
72	28	Ovo, Carne, Manteiga, Frango, Molhada
75	29	Queijo, Ovo, Manteiga, Carne
80	30	Frango, Manteiga, Ovo
86	31	Queijo, Manteiga, Ovo, Molhada
90	32	Carne, Frango, Ovo, Queijo, Manteiga
91	33	Queijo, Ovo
92	34	Manteiga, Molhada, Frango
93	35	Carne, Queijo, Ovo, Manteiga
99	36	Ovo, Queijo, Manteiga, Molhada, Carne
105	37	Frango, Queijo
106	38	Manteiga, Ovo, Carne
107	39	Queijo, Manteiga, Ovo
110	40	Molhada, Queijo, Manteiga
111	41	Carne, Queijo, Ovo, Manteiga
111	42	Frango, Manteiga, Ovo, Molhada
112	43	Queijo, Manteiga, Frango, Ovo, Carne
115	44	Manteiga, Queijo, Ovo
117	45	Carne, Manteiga, Molhada
118	46	Queijo, Ovo, Manteiga, Carne
120	47	Frango, Manteiga, Queijo, Molhada, Ovo
121	48	Manteiga, Queijo, Carne
122	49	Ovo, Queijo, Manteiga, Frango, Molhada
125	50	Carne, Queijo, Manteiga, Ovo
126	51	Ovo, Queijo
127	52	Frango, Manteiga, Molhada
27	53	Carne, Queijo, Manteiga, Ovo
129	54	Queijo, Manteiga, Frango, Molhada, Ovo
132	55	Ovo, Queijo
133	55	Ovo, Queijo
135	57	Frango, Queijo, Ovo
136	58	Queijo, Manteiga, Molhada, Carne
138	59	Ovo, Manteiga, Queijo
140	60	Frango, Manteiga, Ovo, Molhada
145	61	Queijo, Ovo, Manteiga, Carne, Frango
149	62	Manteiga, Queijo, Ovo
155	63	Carne, Manteiga, Molhada
160	64	Queijo, Ovo, Manteiga, Frango, Molhada
168	65	Carne, Queijo, Ovo, Manteiga
172	66	Ovo, Queijo
180	67	Frango, Manteiga, Ovo
210	68	Queijo, Manteiga, Carne, Ovo
215	69	Ovo, Queijo, Manteiga
230	70	Frango, Manteiga
242	71	Queijo, Ovo, Molhada
255	72	Carne, Frango, Manteiga
261	73	Ovo, Queijo, Manteiga
262	74	Queijo, Molhada, Ovo
262	75	Carne, Manteiga, Queijo, Frango, Ovo
275	76	Queijo, Manteiga, Carne, Molhada
278	77	Ovo, Queijo, Manteiga
300	78	Frango, Ovo, Manteiga
305	79	Queijo, Carne, Ovo, Molhada, Manteiga
306	80	Ovo, Queijo, Manteiga, Frango
308	81	Carne, Queijo, Ovo, Manteiga
310	82	Queijo, Manteiga, Frango, Molhada, Ovo
315	83	Ovo, Queijo, Manteiga
318	84	Carne, Manteiga, Frango
322	85	Queijo, Ovo, Manteiga, Molhada, Carne
335	86	Frango, Queijo, Ovo, Manteiga
341	87	Manteiga, Queijo, Ovo, Molhada
347	88	Carne, Queijo, Manteiga
348	89	Ovo, Queijo
362	90	Frango, Manteiga, Ovo, Carne, Molhada
370	91	Queijo, Manteiga, Ovo
```

## Cenário

O que vai interessar é o tempo de preparo total de cada pedido, priorizando que
todos os items de um pedido sejam entregues da forma mais simultânea possível.
