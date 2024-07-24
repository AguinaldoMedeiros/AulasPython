a = 'A'
b = 'B' 
c = 1.1
formato = 'a={} b={} c={}'.format(a, b, c)
formato_2 = 'a={0} b={1} c={2:.2f}'.format(a, b, c)
formato_3 = 'a={nome1} b={nome2} c={nome3:.2f}'.format(nome1=a, nome2=b, nome3=c)

print(formato)
print(formato_2)
print(formato_3)