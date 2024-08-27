# os.listdir para navegar em caminhos
# C:\Users\Aguinaldomedeiros\OneDrive - ASSOCIACAO BRASILEIRA DE REC EM TELECOMUNICACOES\VScode\AulasPython
import os

caminho = r'C:\\Users\\Aguinaldomedeiros\\OneDrive - ASSOCIACAO BRASILEIRA DE REC EM TELECOMUNICACOES\\VScode\\AulasPython'

for item in os.listdir(caminho):
    print(item)