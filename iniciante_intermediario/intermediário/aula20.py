def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y


def cria_multiplicador(multiplcador):
    def multiplica(numero):
        return numero * multiplcador

    return multiplica


print(executa(lambda x, y: x + y, 2, 3), executa(soma, 2, 3))
