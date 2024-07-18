"""
split e join com list e str
split - divide uma string
join - une uma string
"""

frase = 'Olhe só que, coisa interessante'
lista_palavras =  frase.split(',')      # Não inclui o separador

# for i, frase in enumerate(lista_palavras):
    # print(lista_palavras[i])
    # print(lista_palavras[i].strip())    # Retira os espaços antes e depois
    # print(lista_palavras[i].rstrip())   # Retira o espaço da direita
    # print(lista_palavras[i].lstrip())   # Retira o espaço da esquerda

# print(lista_palavras)

frases_unidas = '-'.join(lista_palavras)
print(frases_unidas)