# dir, hasattr e getattr em Python
# para utilizar, deve utilizar o modo debug para porteriore, acessar o modo debug console
# utilizando dir(string) por exemplo


string = 'Luiz'
metodo = 'remove'

if hasattr(string, metodo):
    print(f'Existe o método {metodo}!')
    print(getattr(string, metodo)())
else:
    print(f'Não existe o método {metodo}!')