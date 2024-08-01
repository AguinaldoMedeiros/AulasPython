# Classes decoradoras (Decorator classes)
class Multiply:
    def __init__(self, multiplicador):
        self._multiply = multiplicador

    def __call__(self, func):
        def internal(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * self._multiply
        return internal


@Multiply(22)
def sum_(x, y):
    return x + y


dois_mais_quatro = sum_(2, 4)
print(dois_mais_quatro)