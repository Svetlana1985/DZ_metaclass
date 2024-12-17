class InfoMeta(type):
    def __new__(cls, name, base, dct):
        def info(self):
            attr = [key for key in self.__class__.__dict__.keys() if not key.startswith('__') and key != 'info']
            return f'Класс: {self.__class__.__name__} атрибуты: {attr}'
        dct['info'] = info
        return super().__new__(cls, name, base, dct)

class MyClass(metaclass=InfoMeta):
    x=14
    y=28

class HisClass(metaclass=InfoMeta):
    name = 'Rectangle'
    width = 10
    height = 25

class OurClass(metaclass=InfoMeta):
    author = 'А.С.Пушкин'
    title = 'Руслан и людмила'
    stile = 'Поэма'

obj1 = MyClass()
print(obj1.info())

obj2 = HisClass()
print(obj2.info())

obj3 = OurClass()
print(obj3.info())



