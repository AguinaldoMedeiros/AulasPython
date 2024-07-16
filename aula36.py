"""" Calculadora com while """

while True:

    resultado = 0
    primeiro_num = input('Coloque o primeiro número: ')
    segundo_num = input('Coloque o segundo número: ')

    try:

        primeiro_num = int(primeiro_num)
        segundo_num = int(segundo_num)
    except:
        print('Um ou ambos os números digitados são inválidos!')
        continue

    operador = input('Coloque um operador (+ - * /): ')

    operadores_validos = '+-*/'

    if operador not in operadores_validos:
        print('Operador inválido!')
        continue

    if operador == '+':
        resultado = primeiro_num + segundo_num

    elif operador == '-':
        resultado = primeiro_num - segundo_num

    elif operador == '*':
        resultado = primeiro_num * segundo_num

    elif operador == '/':
        resultado = primeiro_num / segundo_num
    else:
        print('Operador inválido!')
        continue

    print(f'Resultado da operação {primeiro_num} {operador} {segundo_num} = {resultado:.2f}')

    if input('Escreva [S]air ou [C]ontinuar: ').lower().startswith('s'):
        print('Obrigado por utilizar a nossa calculadora!! ;)😊')
        break