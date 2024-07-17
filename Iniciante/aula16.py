# if |    elif   | else
# se | se não se | se não
# pass - para passar, pular

numero = input('Digite um número para a verificação: ')

int_numero = int(numero)

if int_numero % 2 == 0:
    print(f'O número {int_numero} é par')
elif int_numero % 2 == 1:
    print(f'O número {int_numero} é ímpar e o resto da divisão é 1')
else:
    print(f'O número {int_numero} é ímpar')