from account import Account, SavingAccount, CurrentAccount
from person import Client

class Bank:
    def __init__(self, agency):
        self._clients = []
        self._accounts = []
        self._agency = agency
        
    def add_client(self, client: Client):
        self._clients.append(client)
    
    def add_account(self, account: Account):
        self._accounts.append(account)
        
    def authenticate(self, client, account):
        if not isinstance(client, Client) and not isinstance(account, Account):
            return
        
        if self._agency == account._agency and client in self._clients and account in self._accounts:
            print('Authentication completed')