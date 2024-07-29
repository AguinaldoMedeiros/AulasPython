# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
# -> super classe, classe base, classe pai
# Classes filhas (Cliente)
# -> subclasse, classe filha, classe derivada 

class MinhaString(str):
    def upper(self):
        print('Usando o meu upper!')
        return super().upper()
    
string =  MinhaString('Teste')
print(string.upper())