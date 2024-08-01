# Context Manager com função - Criando e Usando gerenciadores de conexto

from contextlib import contextmanager

@contextmanager
def my_open(file_path, mode):
    try:
        print('OPEN FILE')
        file = open(file_path, mode, encoding='utf8')
        yield file
    # except Exception as e:
    #     print('Error ocurred', e)
    finally:
        print('CLOSE FILE')
        file.close()

with my_open('aula30.txt', 'w') as file:
    file.write('Line 1\n')
    file.write('Line 2\n', 123)
    file.write('Line 3\n')
    print('WITH', file)