 # method vs @classmethod vs @staticmethod
 # method - self, método de instância
 # @classmethod - cls, método de classe
 # @staticmethod - método estático (não tem self, nem cls)
 
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None
        
    def set_user(self, user):
        # setter
        self.user = user
        
    def set_password(self, password):
        self.password = password
        
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def return_connection(user, password):
        print(f'O usuário {user} se conectou com sucesso utilizando a senha {password}')
        
        
p1 = Connection()
# p1.set_user('My')
# p1.set_password('abacaxi2342')
# print(p1.user, p1.password)

p1.create_with_auth('Aguinaldo', '1234')
print(p1.user, p1.password)
p1.return_connection(p1.user, p1.password)