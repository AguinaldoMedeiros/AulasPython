# Funções recursivas e recursividade
#     - funções que podem ser chamar de volta
#     - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
#     - Um problema que possa ser dividido em partes mnores
#     - Um caso recursivo que resolve o pequeno problema
#     - Um caso base que para a recursão
#     - fatorial - n! = 5 * 4 * 3 * 2 * 1 = 120

# def recursiva(inicio=0, fim=10):
#     # caso base
#     if inicio >= fim:
#         return fim
    
#     print(inicio, fim)
    
#     # caso recursivo: contar até chegar ao final
#     inicio +=  1
#     return recursiva(inicio, fim)

def fat(numero): 
    
    if numero <= 1:
        return 1
    
    return numero * fat(numero - 1)

print(fat(5))