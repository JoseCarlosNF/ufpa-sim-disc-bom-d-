import json
from dataclasses import dataclass

from data.sabores import intancia_sabor_por_nome


@dataclass
class Pedido:
    tempo_chegada: int
    numero_pedido: int
    items: list

    def __post_init__(self):
        self.items = [item.strip().lower() for item in self.items.split(',')]
        self.items = [intancia_sabor_por_nome(sabor) for sabor in self.items]


with open('data/pedidos.json', encoding='utf-8') as f_pedidos:
    pedidos = [Pedido(*pedido.values()) for pedido in json.load(f_pedidos)]


def get_pedido_por_numero(numero_pedido: int):
    for pedido in pedidos:
        if int(pedido.numero_pedido) == numero_pedido:
            return pedido
