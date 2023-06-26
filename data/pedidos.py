import json
from dataclasses import dataclass
from statistics import mean

from .sabores import intancia_sabor_por_nome
import math

tempos_pedidos = []


@dataclass
class Pedido:
    tempo_chegada: int
    numero_pedido: int
    items: list

    def __post_init__(self):
        self.tempo_chegada = int(self.tempo_chegada)
        self.numero_pedido = int(self.numero_pedido)
        self.items = [item.strip().lower() for item in self.items.split(',')]
        self.items = [intancia_sabor_por_nome(sabor) for sabor in self.items]
        self.tempo_total_preparo = self.__tempo_total_preparo()

    def __tempo_total_preparo(self, capacidade_preparo_simultaneo: int = 3):
        items_sorted_by_time = [_.minutos_preparo for _ in self.items]
        items_sorted_by_time.sort(reverse=True)
        tempo_total_preparo = 0
        for i in range(0, len(self.items), capacidade_preparo_simultaneo):
            tempo_total_preparo += max(
                items_sorted_by_time[i : i + capacidade_preparo_simultaneo]
            )
        tempos_pedidos.append(tempo_total_preparo)
        return tempo_total_preparo


with open('data/pedidos.json', encoding='utf-8') as f_pedidos:
    pedidos = [Pedido(*pedido.values()) for pedido in json.load(f_pedidos)]


print(f'tempo medio de preparo por pedido: {math.floor(mean(tempos_pedidos))} minutos')


def get_pedido_por_numero(numero_pedido: int):
    for pedido in pedidos:
        if pedido.numero_pedido == numero_pedido:
            return pedido


def get_pedido_maior_numero_items():
    pedido_mais_items = [pedidos[0]]
    for pedido in pedidos:
        if len(pedido.items) == len(pedido_mais_items[0].items):
            pedido_mais_items.append(pedido)
        elif len(pedido.items) > len(pedido_mais_items[0].items):
            pedido_mais_items = [pedido]
    return pedido_mais_items
