"""
for + range
range -> range(start, stop, setp)
"""

number = range(10)
number2 = range(5,10)
number3 = range(5,10,2)

for nu in number:
    print(nu)

print(f'Fim range(10)\n')

for nu2 in number2:
    print(nu2)

print(f'Fim range(5,10)\n')

for nu3 in number3:
    print(nu3)

print(f'Fim range(5,10,2)\n')

# continue, break e else funcionam no for da mesma forma que no while