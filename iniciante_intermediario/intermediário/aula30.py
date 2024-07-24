# Generator expression, Itarables e Iterators em Python

# iterable = ['Eu', 'Tenho', '__iter__']
# iterator = iterable.__iter__()  # tem __iter__ e __next__
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))     # Se chegar ao final, o próximo next vai gerar erro (pode ser tratado pelo except)

generator = (n for n in range(1000))      # Generator expression, mude os [] para ()

for i in generator:
    print(i)