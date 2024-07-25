# Atributo de classe

class Pessoa:
    ano_atual = 2024
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def get_ano_nascimento(self):
        return self.ano_atual - self.idade      # Pessoa.ano_atual (mais indicado)
    
p1 = Pessoa('João', 23)
print(p1.get_ano_nascimento())