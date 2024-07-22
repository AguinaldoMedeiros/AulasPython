#  Empacotamento e desempacotamenteo de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)

pessoa = {
    "nome": "Aline",
    "sobrenome": "Souza",
}

dados_pessoa = {
    "idade": 16,
    "altura": 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}

print(*pessoa_completa.values())


def mostrao_argumentos_nomeados(*args, **kwargs):
    print(*args)
    for chave, valor in kwargs.items():
        print(chave, valor)


# mostrao_argumentos_nomeados(nome="Joana", qualquer="123")

mostrao_argumentos_nomeados(**pessoa_completa)

print()

mostrao_argumentos_nomeados(pessoa_completa)

# args e kwargs
# args (já vimos)       # Pega qualquer argumento
# kwargs - keyword arguments (argumentos nomeados)
