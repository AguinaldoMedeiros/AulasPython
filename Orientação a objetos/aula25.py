# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)  🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅
from abc import ABC, abstractmethod

class Notification:
    def __init__(self, msg) -> None:
        self.msg = msg

    @abstractmethod
    def send(self) -> bool: ...

class EmailNotification(Notification):
    def send(self) -> bool:
        print('Sending e-mail: ', self.msg)
        return True

class SMSNotification(Notification):
    def send(self) -> bool:
        print('Sending SMS: ', self.msg)
        return True

def notify(notification: Notification):
    send_notification = notification.send()
    
    if send_notification:
        print('Notification send')
    else:
        print('Notification NOT send') 
        
notify(EmailNotification('Testing'))