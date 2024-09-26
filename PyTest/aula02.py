def soma(x, y):
    """ Soma x e y

    >>> soma(10, 20)
    30

    >>> soma(20, 50)
    70

    >>> soma(21, 34)
    55

    """

    assert isinstance(x, (int, float)), 'Valor x precisa ser int ou float'
    assert isinstance(y, (int, float)), 'Valor y precisa ser int ou float'
    return x + y

try:
    print(soma(2, 2))
except Exception as e:
    print(e)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)