from abc import ABC, abstractmethod
from account import Account, SavingAccount

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @abstractmethod
    def client(self): ...
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
class Client(Person):
    def __init__(self, name, age, type_account: Account):
        self._name = name
        self._age = age
        self.type_account = type_account
    
    def client(self):
        return self.name, self.type_account.account()

# if __name__ == '__main__':
#     client = Client('Medeiros', 62834324, SavingAccount())
#     print(client.client())