"""
Escopo de função em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e o local.
O escopo global é o escopo onde todo o código é alcançável.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1           # Variável interna do módulo (Global a todos os itens dentro do módulo)

def escopo():
    # global x  # Definindo a variável global x, estaria mexendo na variável global, não a interna
    x = 10      # Variável interna do escopo
    def escopo_interno():
        x = 100 # Variável interna do escopo initerno
        print(x)
    escopo_interno()
    print(x)

print(x)
escopo()
print(x)