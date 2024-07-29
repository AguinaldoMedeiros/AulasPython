# @property - um getter do modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo
# Geralmente é usada nas seguintes situações:
# -  como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar settar
# - p/ executar ações ao obter um atributo
# código cliente - é o código que usa seu código

class Caneta:
    def __init__(self, cor):
        self.cor = cor
        
    # def get_cor(self):
    #     print('GET COR')
    #     return self.cor
    
    @property
    def cor(self):
        print('PROPERTY')
        return self.cor
        
caneta = Caneta('Azul')

print(caneta.cor)

