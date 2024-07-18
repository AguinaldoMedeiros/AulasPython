"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""
condicao = 10 == 10
variavel_1 = 'Valor' if condicao else 'Outro valor'

condicao = 10 == 11
variavel_2 = 'Valor' if condicao else 'Outro valor'

print(variavel_1, variavel_2)

print('Valor' if True else 'Outro valor' if True else 'Outro valor')    #Não faça