"""
Introdução ao desempacotamento + tuplas (tuplas)
"""

nomes = ['Maria', 'Helena', 'Luiz']
# nome1, nome2, nome3 = nomes
# nome1, *resto = nomes
_, nome1, *_ = nomes

print(nome1, _)