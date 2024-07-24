# Manipulando chaves e valores em dicionários

pessoa = {}

chave = 'nome'

pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'

print(pessoa[chave])

pessoa[chave] = 'Maria'

if pessoa.get('sobrenome') is None:  # Caso não exista, o método .get() retorna naturalmente o None
    print('existe')

del pessoa['sobrenome']
print(pessoa)