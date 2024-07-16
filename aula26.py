"""
Fatiamento de strings

[i:f:p] [::]
Obs.: a função len retorna a quantidade
de caracteres da str
Obs.: O índice final geralmente
omite o valor selecionado
"""

variavel = 'Olá mundo!'
print(variavel)
print(variavel[0:10:3]) # O terceiro índice determina de quantos em quantos caracteres vai retornar
print(variavel[4:7]) # Obtem do índice 4 até o índice 6 (omitindo o índice solicitado)
print(variavel[:7]) # Obtem do início até o índice 6 (omitindo o índice solicitado)
print(variavel[4:]) # Obtem de índice 4 até o final
print(len(variavel)) # Retorna o valor da quantidade de caracteres da variável
print(len(variavel[5])) #Retorna o valor da quantidade de caracteres solicitados