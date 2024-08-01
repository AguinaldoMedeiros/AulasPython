from abc import ABC, abstractmethod

class Account:
    def __init__(self, agency, account_number, balance):
        self.agency = agency
        self.account_number = account_number
        self.balance = balance
        
    @abstractmethod
    def account(self): ...
    
    @abstractmethod
    def deposit_method(self): ...
    
    @abstractmethod
    def withdraw_method(self): ...
    
class CurrentAccount(Account):
    def __init__(self, agency, account_number, balance):
        self.type = 'CourrentAccount'
        super().__init__(agency, account_number, balance)
    
    def account(self):
        return self.type
    
class SavingAccount(Account):
    def __init__(self, agency, account_number, balance):
        self.type = 'SavingAccount'
        self.extra_limit = balance * 1.2
        super().__init__(agency, account_number, balance)
    
    def account(self):
        return self.type