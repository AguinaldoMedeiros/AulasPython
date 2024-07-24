# Try, except, else e finally

try:
    a = 9
    b = 2
    print(a/b)

except ZeroDivisionError:
    print('ZeroDivisionError')

else:
    print('Não deu erro')   # Executa quanto o try não gera nenhum erro

finally:
    print('Finally')        # Finally sempre vai executar, mesmo que haja um erro