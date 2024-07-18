# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def mult(*args):
    result = 1
    for number in args:
        result *= int(number)
    return result

print(mult(1,2,3,4,5))