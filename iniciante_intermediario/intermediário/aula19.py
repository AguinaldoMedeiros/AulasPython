# Função lambda em Python
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que comtémm apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'Miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]

# lista = [4, 32, 1, 34, 5, 6, 21]
# lista.sort()          # Utiliza a tabela unicod
# print(lista)
# lista.sort(reverse=True)
# print(lista)

lista = [
    {"nome": "Luiz", "sobrenome": "Miranda"},
    {"nome": "Maria", "sobrenome": "Oliveira"},
    {"nome": "Daniel", "sobrenome": "Silva"},
    {"nome": "Eduardo", "sobrenome": "Moreira"},
    {"nome": "Aline", "sobrenome": "Souza"},
]

# def ordena(item):
#     return item['nome']

# lista.sort(key=ordena)


# lista.sort(key=lambda item: item['nome'])     # Altera diretamente sua lista, ou seja, muda a ordem interna dela


def exibir(lista):
    for i in lista:
        print(i)


l1 = sorted(lista, key=lambda item: item["nome"])
l2 = sorted(lista, key=lambda item: item["nome"])

exibir(l1)
print()
exibir(l2)

# for i in lista:
#     print(i)
