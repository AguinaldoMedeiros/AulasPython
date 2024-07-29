# @staticmethod (métodos estáticos)
# Métodos estáticos são métodos que estão dentro da
# classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua
# classe.

class Classe:
    
    def __init__(self, idade, idade2):
        self.idade = idade
        self.idade2 = idade2
    
    @staticmethod
    def soma_idade(idade, idade2):
        return idade + idade2
    
p1 = Classe(20, 23)

print(Classe.soma_idade(p1.idade, p1.idade2))