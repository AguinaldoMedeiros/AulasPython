"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def teste(a, b):
    print(a + b)

teste(20, 30)       # Não nomeado
teste(b=30,a=20)    # Nomeado