"""
Valores padrão para parâmetro
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: Editar o código
"""

def soma(x, y, z = None):
    if z is not None:
        print(x + y + z)
    else:
        print(x + y) 


soma(1, 2, 10)


