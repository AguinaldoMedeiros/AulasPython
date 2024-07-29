# Relação entre classes: associação, agregação e composição
# Composição é uma especialização de agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também serão apagados.

class Cliente:
    
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
        
    def inserir_enderecos(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))
        
    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)
        
class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
        
cliente1 = Cliente('Maria')
cliente1.inserir_enderecos('Jetúlio Vargas', 1.100)

cliente1.inserir_enderecos('Tira Dentes', 34)

cliente1.listar_enderecos()