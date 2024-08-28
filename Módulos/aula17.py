# csv.writer e csv.DictWriter para escrever em CSV
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário

import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula17.csv'

lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]

with open(CAMINHO_CSV, 'w', encoding='utf-8') as file:
    nomes_colunas = lista_clientes[0].keys()
    escritor = csv.writer(file)

    escritor.writerow(nomes_colunas)

    for clientes in lista_clientes:
        escritor.writerow(clientes.values())
