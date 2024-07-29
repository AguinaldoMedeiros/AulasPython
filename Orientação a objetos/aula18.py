# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricantes na tela

class Carro:
    def __init__(self, nome, motor = None):
        self.nome = nome
        self._motor = motor
        
    @property    
    def motor(self, **kwargs):
        if self.motor is None:
            print(f'Adicionando motor ao carro {self.nome}.')
            self._motor = kwargs
        
        print(f'Atualizando o motor do carro {self.nome}.')
        self._motor = kwargs
        
class Motor:
    def __init__(self, nome, potencia):
        self.nome = nome
        self.cavalos = potencia
    
class fabricante:
    def __init__(self, nome):
        self.nome = nome
        self.carros = []
        
    def adicionar_carros(self, nome):
        self.carros.append(Carro(nome))
        
    def listar_carros(self):
        for carro in self.carros:
            print(carro.nome)
        
motor = Motor('Motor de fusca', 1.6)
volkswagen = fabricante('volkswagen')
volkswagen.adicionar_carros('Fusca')

print(volkswagen.carros[0].nome)
