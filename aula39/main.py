from account import SavingAccount, CurrentAccount
from person import Client
from bank import Bank

client1 = Client('Medeiros', 23)
account1 = SavingAccount(2323, 123, 2.500)
bank1 = Bank(2323)

bank1.add_account(account1)
bank1.add_client(client1)

bank1.authenticate(client1, account1)