# isinstance - para saber se o objeto é de determinado tipo
lista = ['a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nom1': 'Luiz'}]

for item in lista:
    print(item, isinstance(item, set))                  # Um argumento
    
    if isinstance(item, (int, float)):
        print(item, isinstance(item, (int, float)))     # Mais de um argumento