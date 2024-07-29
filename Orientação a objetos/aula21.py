# Herança Múltipla - Python Orientado a Objetos
# Quer dizer que no Python, uma classe pode estender
# várias outras classes.
# Herança simples:
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Herança múltipla e mixins
# Log -> FileLog
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Cliente(Pessoa, FileLog)
#
# A, B, C, D
# D(B, C) - C(A) - B(A) - A
#
# método -> falar
#           A
#         /   \
#        B     C
#         \   /
#           D
#
# Python 3 usa C3 superclass linearization
# para gerar o mro.
# Você não precisa estudar isso (é complexo)
# https://en.wikipedia.org/wiki/C3_linearization
#
# Para saber a ordem de chamada dos métodos
# Use o método de classe Classe.mro()
# Ou o atributo __mro__ (Dunder - Double Underscore)

class Teste():
    ...


    def quem_sou(self):
        print('Teste')

class T1(Teste):
    ...

    def quem_sou(self):
        print('T1')

class T2(Teste):
    ...


    def quem_sou(self):
        print('T2')

class T3(T1, T2):
    ...


    def quem_sou(self):
        print('T3')


class A:
    ...

    def quem_sou(self):
        print('A')

class B(A):
    ...

    # def quem_sou(self):
    #     print('B')

class C(A):
    ...

    # def quem_sou(self):
    #     print('C')

class D(B, C):
    ...

    # def quem_sou(self):
    #     print('D')

class E(T3, D):
    ...

    # def quem_sou(self):
    #     print('D')

eu = E()

eu.quem_sou()
print(E.mro())