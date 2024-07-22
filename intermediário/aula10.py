# Exercícios
# Crie funções que duplicam, triplicam e quadriplicam
# o número recebido como parâmetro

# def duplicar_num(x):
#     return x + x

# def triplicar_num(x):
#     return duplicar_num(x) + x

# def quadriplicar_num(x):
#     return triplicar_num(x) + x

# x = 2

# print(duplicar_num(x), triplicar_num(x), quadriplicar_num(x))

x = 3

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(x), triplicar(x), quadruplicar(x))