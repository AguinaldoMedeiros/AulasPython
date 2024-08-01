from abc import ABC, abstractmethod

class Account:
    def __init__(self, agency, account_number, balance):
        self._agency = agency
        self.account_number = account_number
        self.balance = balance
    
    @property
    def agency(self):
        return self._agency
    
    @abstractmethod
    def withdraw_method(self): ...
    
    def deposit_method(self, value): 
        self.balance += value
    
class CurrentAccount(Account):
    def __init__(self, agency, account_number, balance):
        self.type = 'CourrentAccount'
        super().__init__(agency, account_number, balance)

    def withdraw_method(self, value):
        if value <= self.balance:
            self.balance -= value
        else:
            print('Insufficient balance!')
    
class SavingAccount(Account):
    def __init__(self, agency, account_number, balance):
        self.type = 'SavingAccount'
        self.extra_limit = balance * 1.2
        super().__init__(agency, account_number, balance)
        
    def withdraw_method(self, value):
        if value <= self.balance:
            self.balance -= value
        elif value <= self.extra_limit:
            self.extra_limit -= value
        else:
            print('Insufficient balance!')