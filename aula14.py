# @property + @setter - getter e setter no modo Python
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começam com _ ou __, são da classe e não devem
# ser utilizados fora dela

class Caneta:
    def __init__(self, cor):
        self._cor = cor
        
    @property
    def cor(self):
        print('PROPERTY')
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        self._cor = valor
    
    @cor.deleter
    def cor(self):
        ...
    
caneta = Caneta('Azul')
print(caneta.cor)
caneta.cor = 'Verde'
print(caneta.cor)
caneta.cor