from dataclasses import dataclass
from statistics import mean

from rich import print
from simpy.core import Environment
from simpy.resources.resource import Resource

from data.pedidos import Pedido, pedidos


@dataclass
class Cozinheiro:
    capacidade_preparo_simultaneo: int = 3


class Tapiocaria:
    def __init__(self, env: Environment, cozinheiros: Resource):
        self.env = env
        self.cozinheiros = cozinheiros

    def simulate(self, pedido: Pedido):
        # O pedido chega até a cozinha
        yield self.env.timeout(pedido.tempo_chegada)
        print(
            f'O pedido [b]{pedido.numero_pedido}',
            f'[green]chegou[/] na cozinha em {self.env.now}',
        )

        # O pedido é encaminhado para o cozinheiro
        with self.cozinheiros.request() as cozinheiro:
            # Espera um cozinheiro ficar livre p/ iniciar o preparo
            yield cozinheiro
            print(
                f'O pedido [b]{pedido.numero_pedido}[/]',
                f'[b][blue]iniciou[/][/] o preparo em {self.env.now}',
            )

            # O preparo do pedido é finalizado
            yield self.env.timeout(pedido.tempo_total_preparo)
            print(
                f'O pedido [b]{pedido.numero_pedido}[/]',
                f'[b][red]finalizou[/][/] o preparo em {self.env.now}',
            )


if __name__ == '__main__':
    media_items_por_pedido = mean([len(pedido.items) for pedido in pedidos])
    env = Environment()

    cozinheiros = Resource(env, capacity=3)
    tapiocaria = Tapiocaria(env, cozinheiros)

    for pedido in pedidos:
        env.process(tapiocaria.simulate(pedido))

    env.run()
