"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
break - para encerrar o while
"""

condicao = True

while condicao:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')

    if numero_1.isdigit() or numero_2.isdigit():
        print(f'A soma do {numero_1} e do {numero_2} é {int(numero_1) + int(numero_2)}')
    else:
        print('Digite apenas números inteiros!')
        break