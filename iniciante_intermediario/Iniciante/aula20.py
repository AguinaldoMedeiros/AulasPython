#  Operadores lógicos 
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor 
# São consideradas falsy
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('Digite [E]ntrar ou [S]air: ')
senha_digitada = input('Digite sua senha: ')
senha_permitida = 'abcd1234'

if(entrada == 'E' and senha_digitada == senha_permitida):
    print('Entrando')
else:
    print('Saindo')