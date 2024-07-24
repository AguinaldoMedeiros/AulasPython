"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf_cliente = input('Digite o cpf: ')

# cpf_cliente_formatado = cpf_cliente.split('.')
# cpf_cliente_formatado[2].split('-')
# cpf_cliente_formatado = ''.join(cpf_cliente_formatado)
cpf_cliente_formatado = ''

i = 0

for number in cpf_cliente:
    try:
        int(number)
        cpf_cliente_formatado += str(number)
    except:
        continue
    
    i += 1
    
    if i == 9:
        break

i = 10  
soma_cpf = 0
soma_cpf_2 = 0

for number in cpf_cliente_formatado:
    try:
        soma_cpf += int(number)*i
        i -= 1
    except:
        continue
    
soma_cpf = (soma_cpf * 10) % 11
primeiro_digito = '0' if soma_cpf >= 10 else soma_cpf

cpf_cliente_mais_primeiro_digito = cpf_cliente_formatado + str(primeiro_digito)

i  = 11

for number in cpf_cliente_mais_primeiro_digito:
    try:
        soma_cpf_2 += int(number)*i
        i -= 1
    except:
        continue
    
soma_cpf_2 = (soma_cpf_2 * 10) % 11
segundo_digito = '0' if soma_cpf_2 >= 10 else soma_cpf_2

if int(cpf_cliente[-2]) == int(primeiro_digito) and int(cpf_cliente[-1]) == int(segundo_digito):
    print(f'O cpf {cpf_cliente} é valido!')
else:
    print(f'O cpf {cpf_cliente} NÃO é valido!')

    
    