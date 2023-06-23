from statistics import mean
from data.pedidos import pedidos

if __name__ == '__main__':
    media_items_por_pedido = mean([len(pedido.items) for pedido in pedidos])
