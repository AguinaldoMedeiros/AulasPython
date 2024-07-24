#  Operadores lógicos 
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado verdadeira,
# a expressão inteira será avaliada naquele valor 

entrada = input('Digite [E]ntrar ou [S]air: ')
senha_digitada = input('Digite sua senha: ')
senha_permitida = 'abcd1234'

if((entrada == 'E' or entrada =='e') and senha_digitada == senha_permitida):
    print('Entrando')
else:
    print('Saindo')