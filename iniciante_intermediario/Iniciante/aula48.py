"""
enumarate = enumerate iteráveis (índice)
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

lista_enumerada = enumerate(lista)

# for item in lista_enumerada:      # O iterator acaba após ser utilizado
#     print(item)

for item in enumerate(lista):       # Cria um interador por for
    print(item)
    
for indice, nome in enumerate(lista):
    print(indice, nome)