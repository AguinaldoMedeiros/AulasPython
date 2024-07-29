# Métodos em instâncias de classes Python

class Carro:
    def __init__(self, nome):
        # self.name = 'Fusca'     # Hard coded
        self.name = nome
        
    def acelerar(self):
        print(f'{self.name} está acelerando...')
   

fusca = Carro('Fusca')     
print(fusca.name)
fusca.acelerar()