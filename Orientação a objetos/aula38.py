# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de
#       definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:DIREÇÕES
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value

import enum

# DIRECTIONS = enum.Enum('Directions',['LEFT', 'RIGTH', 'ABOVE', 'BELLOW'])

class Directions(enum.Enum):
    LEFT = enum.auto()
    RIGTH = enum.auto()
    ABOVE = enum.auto()
    BELLOW = enum.auto()

def move(direction: Directions):
    
    if not isinstance(direction, Directions):
        raise ValueError('Direction not match')
    
    print(f'Moving for {direction.name}')
    

move(Directions.LEFT)

help(enum)