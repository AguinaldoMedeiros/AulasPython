# Entendendo self em classes Python
# Classe - Molde (geralmente sem dados)
# Instância de class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.

class Carro:
    def __init__(self, nome):
        self.name = nome
        
    def acelerar(self):
        print(f'{self.name} está acelerando...')
   

fusca = Carro('Fusca')     
print(fusca.name)
fusca.acelerar()
Carro.acelerar(fusca)