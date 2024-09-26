def soma(x, y):
    assert isinstance(x, (int, float)), 'Valor x precisa ser int ou float'
    assert isinstance(y, (int, float)), 'Valor y precisa ser int ou float'
    return x + y

try:
    print(soma(2, 2))
except Exception as e:
    print(e)