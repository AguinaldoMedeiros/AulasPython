# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)

class MyError(Exception):
    ...
    
class OtherError(Exception):
    ...
    
def rise():
    exception_error = MyError('MyError')
    exception_error.add_note('This is my error test for to pratice Python Error and Exceptions')
    raise exception_error
try: 
    rise()
except MyError as error:
    print(error.__class__.__name__)
    print()
    exception_error = OtherError('Other Error')
    raise exception_error from error