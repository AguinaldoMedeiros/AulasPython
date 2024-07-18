"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

# Lembrete de desempacotamento

# x, y, *resto = 1, 2, 3, 4

# print( x, y, resto)

# def soma(x, y):
#     return x + y

# print(1)

def soma(*args):
    resultado_soma = 0
    for number in args:
        resultado_soma += number
    return resultado_soma

# *numeros (desempacotar uma tupla)