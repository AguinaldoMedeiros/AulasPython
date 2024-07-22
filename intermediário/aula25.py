# for dentro de for in comprehension

lista = []

# for x in range(2):
#     for y in range(3):
#         lista.append((x, y))
        
# lista = [(x, y) for x in range(3) for y in range(3)]

lista = [[x for x in range(3)] for x in range(3)]
        
print(lista)