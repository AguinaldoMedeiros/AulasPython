# List comprehension em Python
# List comprehension é uma fomr arápida para criar listas
# a partir de iteráveis

# print(list(range(10)))

# lista = []
# for numero in range(10):
#     lista.append(numero)
# print(lista)

lista = [numero + numero for numero in range(100)]
print(lista)
