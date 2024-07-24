# Exercício - sistema de perguntas e respotas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    index = 0
    for opcao in pergunta['Opções']:
        print(f'{index}) {opcao}')
        index += 1
    
    # for i, opcao in enumerate(pergunta['Opções']):
    #     print(f'{i}) {opcao}')
    
    resposta_usuario = input('Escolha uma opção: ')
  
    try: 
        int(resposta_usuario)
    except:
        print('Escolha apenas números interios!')
        break
    
    if resposta_usuario == pergunta['Resposta']:
        print(f'Parabéns, a resposta {resposta_usuario} está correta!!!🥳🎉🎉', end='\n\n')
    else:
        print(f'Infelizmente a resposta {resposta_usuario} está errada... 🙁☹️ Tente novamente.', end='\n\n')
  
    # resposta_usuario_int = None
    # if resposta_usuario.isdigit():
    #     resposta_usuario_int = int(resposta_usuario)
        
    # if resposta_usuario_int is not None:
        
    #     if resposta_usuario == pergunta['Resposta']:
    #         print(f'Parabéns, a resposta {resposta_usuario} está correta!!!🥳🎉🎉', end='\n\n')
    #     else:
    #         print(f'Infelizmente a resposta {resposta_usuario} está errada... 🙁☹️ Tente novamente.', end='\n\n')