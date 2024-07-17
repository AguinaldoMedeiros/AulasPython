"""
Exercício
Peça ao usuário para digitar seu nome e idade
se ambos forem digitados, exiba:
    Seu nome é {nome}
    Seu nome invetido é {nome invertido}
    Se nome contém (ou não) espaços
    Seu nome tem {n} letras
    A primeira letra do seu nome é {letra}
    A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade, exiba:
    "Campos vazios, tente novamente!"
"""

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome !='' and idade != '':
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[-1:-len(nome)-1:-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    print(f'A primeir aletra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print("Campos vazios, tente novamente!")