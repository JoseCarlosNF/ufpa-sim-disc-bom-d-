import json
from dataclasses import dataclass


@dataclass
class Sabor:
    nome: str
    minutos_preparo: int


with open('data/sabores.json', encoding='utf-8') as f_sabores:
    sabores = [
        Sabor(item['nome'], item['minutos_preparo'])
        for item in json.load(f_sabores)
    ]


def intancia_sabor_por_nome(sabor: str):
    for _ in sabores:
        if _.nome == sabor:
            return _
