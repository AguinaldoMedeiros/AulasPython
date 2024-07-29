from log import LogPrintMixin

class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True
            print(f'{self._nome} ligando')

    def desligar(self):
        if self._ligado:
            self._ligado = False
            print(f'{self._nome} desligando')

class Smartphone(Eletronico, LogPrintMixin):
    def ligar(self):
        super().ligar()

        if self._ligado:
            msg = f'{self._nome} foi ligado'
            self.log_success(msg)
        
    def desligar(self):
        super().desligar()

        if not self._ligado:
            msg = f'{self._nome} foi desligado'
            self.log_success(msg)

if __name__ == '__main__':
    iphonex = Smartphone('Iphone X')
    iphonex.ligar()