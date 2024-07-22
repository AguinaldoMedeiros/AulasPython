# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

import copy

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda'
}

# pessoa2 = pessoa.copy()         # Faz uma cópia rasa, ou seja, apenas objetos imutáveis

# pessoa3 = copy.deepcopy(pessoa) # Faz uma cópia inteira, incluindo listas e sublistas

nome = pessoa.pop('nome')         # Remove o item, mas retorna qual item foi removido

nome2 = pessoa.popitem()           # Remove a última chave e o retorna

print(pessoa)
print(nome)
print(nome2)


pessoa.update({
    'nome': 'teste',
    'teste': '0'
})

# pessoa.setdefault('idade', None)      # Seta uma saída padrão para caso o 'idadde' seja chamado
# print(pessoa['idade'])

# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# for chave, valor in pessoa.items():
#     print(chave, valor)

