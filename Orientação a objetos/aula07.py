# __dict__ e vars para atributos de instância

class Pessoa:
    ano_atual = 2024
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def get_ano_nascimento(self):
        return self.ano_atual - self.idade      # Pessoa.ano_atual (mais indicado)
    
p1 = Pessoa('João', 23)
# print(p1.get_ano_nascimento())

# p1.__dict__['nome'] = 'Eita'
# del p1.__dict__['nome']
print(p1.__dict__)
print(vars(p1))     # Mesma função do __dict__