
class BaseValidator:
    def __init__(self , low_bound = 0 , upper_bound = 1000 ):
        self.low_bound = low_bound
        self.upper_bound = upper_bound

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, 'N/A')

    def validate(self, value):
        # this will need to be implemented in specifically by each subclass
        pass


class IntegerField(BaseValidator):
    def  validate(self, value):
        if not isinstance(value, int):
            raise ValueError(f'{self.name} must be integer value')
        if value < self.low_bound:
            raise ValueError(f'{self.name} must not be less than {self.low_bound}')
        if value > self.upper_bound:
            raise ValueError(f'{self.name} must not be above {self.upper_bound}')


class CharField(BaseValidator):
    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.name} must be integer value')
        if len(value) < self.low_bound:
            raise ValueError(f'{self.name} must not be less than {self.low_bound}')
        if len(value) > self.upper_bound:
            raise ValueError(f'{self.name} must not be above {self.upper_bound}')


class Person:
    name = CharField(low_bound=2 , upper_bound =24)
    age = IntegerField(low_bound= 0 , upper_bound= 150)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{type(self)}(name = {self.name}, age = {self.age})'


def test():
    try:
        p = Person('lawrence', 12000000)
        print(p.__repr__())
        print(p.name)
        print(p.age)
    except ValueError as ex:
        print(ex)


def test2():
    try:
        p = Person('lawrence', '12')
    except ValueError as ex:
        print(ex)


if __name__ == '__main__':
    test()