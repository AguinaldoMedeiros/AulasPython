import testes_m              # Cada módulo só pode, por padrão, ser importado uma única vez
import importlib            # Utilizando o importlib, conseguimos dar reload no import
import intermediário.aula01

for i in range(10):
    importlib.reload(testes_m)
