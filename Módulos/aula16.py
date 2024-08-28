# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário

import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula16.csv'

# with open(CAMINHO_CSV, 'r') as file:
#     reader = csv.reader(file)

#     for linha in reader:
#         print(linha)

with open(CAMINHO_CSV, 'r') as file:
    reader = csv.DictReader(file)

    for linha in reader:
        print(linha['Nome'], linha['Idade'])
