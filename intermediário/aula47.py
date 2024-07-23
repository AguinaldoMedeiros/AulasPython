# Exercício - unir listas
# Cria uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado:
# [('Salvador', 'BA'),('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

def zipper(lista1, lista2):
    if len(cidades) >= len(estados):
        menor = len(estados)
    else:
        menor = len(cidades)
    i = 0
    resultado = []
    while i < menor:
        resultado.append((lista1[i], lista2[i]))
        i += 1

    return resultado


print(zipper(cidades, estados))


# def zipper(l1, l2):
#     intervalo = min(len(l1), len(l2))
#     return [(l1[i], l2[i]) for i in range(intervalo)]
# from itertools import zip_longest

# l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# l2 = ['BA', 'SP', 'MG', 'RJ']
# print(list(zip(l1, l2)))
# print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')))


"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

def soma(lista_a, lista_b):
    return [lista_a[i] + lista_b[i] for i in range(min(len(lista_a), len(lista_b)))]

lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

print(soma(lista_a, lista_b))