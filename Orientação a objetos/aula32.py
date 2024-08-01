# Funções decoradoras e decoradores com classes

def add_repr(class_):
    def my_repr(self):
        return f'{self.__class__.__name__}({self.__dict__})'
    class_.__repr__ = my_repr
    return class_

class MyReprMixin:
    # def __repr__(self):
    #     class_name = self.__class__.__name__
    #     class_dict = self.__dict__
    #     class_repr = f'{class_name}({class_dict})'
    #     return class_repr
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.__dict__})'

@add_repr
class Time:
    def __init__(self, name):
        self.name = name

@add_repr
class Planeta:
    def __init__(self, name):
        self.name = name
        
# Time = add_repr(Time)

brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)