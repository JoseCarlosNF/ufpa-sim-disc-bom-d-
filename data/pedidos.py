import json
from dataclasses import dataclass

from .sabores import intancia_sabor_por_nome


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
        self.tempo_total_preparo = max([item.minutos_preparo for item in self.items])


with open('data/pedidos.json', encoding='utf-8') as f_pedidos:
    pedidos = [Pedido(*pedido.values()) for pedido in json.load(f_pedidos)]


def get_pedido_por_numero(numero_pedido: int):
    for pedido in pedidos:
        if pedido.numero_pedido == numero_pedido:
            return pedido
