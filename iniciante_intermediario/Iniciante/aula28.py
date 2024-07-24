"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero = input('Digite um número, o seu valor será dobrado a seguir: ')

try:
    numero = float(numero)
    print(f'O dobro de {numero} é {numero * 2}')

except:
    print('O texto digitado não é um número!')