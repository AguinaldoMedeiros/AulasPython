# Introdução às Generator functions em Python
# generator = (n for n in range(10))

def generator(n=0, m=0):
    while True:
        yield n
        n += 1 

        if n > m:
            return
        
gen = generator(m=10)

for i in gen:
    print(i)