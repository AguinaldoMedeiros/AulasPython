# Métodos de classe
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    
    ano = 2023  # atributo de classse
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')
        
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_pessoa_anonima(cls):
        return cls('Anônima', 0)
    
print(Pessoa.ano)
p1 = Pessoa.criar_com_50_anos('Teste')
print(p1.idade)
p2 = Pessoa.criar_pessoa_anonima()
print(p2.nome, p2.idade)