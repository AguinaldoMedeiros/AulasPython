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

def par_impar(x):
    return f'O número {x} é par' if x % 2 == 0 else f'O número {x} é ímpar'

result_mult = mult(3,3,3,3,3,3,3,3,5)
print(par_impar(result_mult))