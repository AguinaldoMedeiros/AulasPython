# Mantendo estados dentro da classe

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
        
        
    def filmar(self):
        if self.filmando:
            print(f'A câmera {self.nome} já está filmando!')
            return
        
        print(f'A câmera {self.nome} começou a filmar...')
        self.filmando = True
        
    def fotografar(self):
        if self.filmando:
            print(f'A câmera {self.nome} não pode tirar fotos enqanto filma.')
            return
        print(f'A câmera {self.nome} está fotografando.')
            
    def parar_filmar(self):
        if self.filmando:
            self.filmando =  False
            print(f'A câmera {self.nome} parou de filmar.')
            return

c1 = Camera('Canon')
c2 = Camera('Sonny')
c2.filmar()
c2.filmar()
c2.fotografar()
c2.parar_filmar()
c2.parar_filmar()
c2.fotografar()