def divisores(x):
    divisores = []
    for i in range(1, x+1):
        if x % i == 0:
            divisores.append(i)

    return divisores

def maior_divisor(x,y):
    result = 0

    for i in x:
        for j in y:
            if i == j:
                if result<j:
                    result = j
    return result

n = int(input())

f1 = []
f2 = []
saidas = []

for i in range(0, n):
    valores = input()
    f1, f2 = valores.split()
    divisores_f1 = divisores(int(f1))
    divisores_f2 = divisores(int(f2))
    saidas.append(maior_divisor(divisores_f1,divisores_f2))

print(*saidas, sep='\n')