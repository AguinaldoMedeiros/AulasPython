from abc import ABC, abstractmethod

class Account:
    def __init__(self, agency, account_number, balance=0):
        self._agency = agency
        self._account_number = account_number
        self._balance = balance
    
    @property
    def agency(self):
        return self._agency
    
    @abstractmethod
    def withdraw(self): ...
    
    def deposit(self, value): 
        self._balance += value
        self._details(f'(Deposit {value})')

    def _details(self, msg):
        print(f'Your balance is {self._balance} {msg}')
    
class SavingAccount(Account):
    def withdraw(self, value):
        if value <= self._balance:
            self._balance -= value
            self._details(f'(Withdraw {self._balance})')
        else:
            print('Insufficient balance!')
    
class CurrentAccount(Account):
    def __init__(self, agency, account_number, balance=0, limit=0):
        super().__init__(agency, account_number, balance)
        self._extra_limit = -limit
        
    def withdraw(self, value):
        if self._balance - value > self._extra_limit:
            self._balance -= value
            self._details(f'(Withdraw {value})')
        else:
            print(f'Insufficient balance! (Remaining Balance {self._balance})')

if __name__ == '__main__':
    c1 = CurrentAccount(111, 222, 20, 100)
    c1.deposit(23)
    c1.withdraw(23)
    c1.withdraw(3)
    c1.withdraw(100)
    c1.withdraw(20)