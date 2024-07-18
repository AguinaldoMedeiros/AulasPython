"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores de sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""

# Selecione uma opção
# [i]nserir [a]pagar [l]istar: 

lista_compras = []

while True:
    user_option = input(f'Selecione uma opção\n[i]nserir [a]pagar [l]istar: ')
    
    if len(user_option) > 1:
        print('Digite apenas uma letra!')
        continue
    
    if user_option.upper() == 'I':
        add_valor = input('Valor: ')
        lista_compras.append(add_valor)
        continue
    
    elif user_option.upper() == 'A':
        for indice, item in enumerate(lista_compras):
            print(indice, item)
        remove_valor = input('Escolha o índice para apagar: ')
        try:
            remove_valor = int(remove_valor)
            lista_compras.remove(lista_compras[remove_valor])
            print('Item removido com sucesso!')
            continue
        except:
            print('Item não pode ser removido, por favor, tente novamente.')
            continue
    
    elif user_option.upper() == 'L':
        for indice, item in enumerate(lista_compras):
            print(indice, item)
        continue
        
    else:
        print("Digite apenas a letra inicial de cada opção.")
        continue