# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']


tarefas = []
lista_desfeitos = []

def opcoes(user_response):
        
    if user_response == 'listar':
        return list_items()
    elif user_response == 'desfazer':
        return desfazer()
    elif user_response == 'refazer':
        return refazer()
    else:
        return adicionar(user_response)

def list_items():
    print('\nTAREFAS:')
    print(*tarefas, sep='\n')
    print()
    return console()

def desfazer():
    if len(tarefas) > 0:
        lista_desfeitos.append(tarefas.pop())
    return list_items()

def refazer():
    if len(lista_desfeitos) > 0:
        tarefas.append(lista_desfeitos.pop())
    return list_items()

def adicionar(items):
    tarefas.append(items)
    return list_items()

def console():
    
    opcoes(input('Comandos: listar, desfazer, refazer\nDigite uma tarefa ou um comando: '))

console()

