# Try, except, else e finally

try:
    a = 1
    b = 0
    c = a / b
    print(c)

except ZeroDivisionError:           # except error, trata o erro específico
    print('Dividsão por zero.')

except (TypeError, IndexError):     # Adiciona mais de uma exceção de erro por except
    print('Type + Index error')

except Exception as error:          # Excpetion agrega todos os erros, as agrega o erro a uma variável
    print(error.__class__.__name__) # Exibe o erro agregado a variável na tela
