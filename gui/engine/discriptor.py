from decimal import Decimal
import decimal
import re

class BaseValidator:
    def __init__(self , _min = None , _max = None ):
        self.low_bound = _min
        self.upper_bound = _max

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
    def __init__(self, _min=0):
        super().__init__(_min)

    def  validate(self, value):
        if not isinstance(value, int):
            raise ValueError(f'{self.name} must be integer value')
        if value < self.low_bound:
            raise ValueError(f'{self.name} must not be less than {self.low_bound}')

        # if value > self.upper_bound:
        #     raise ValueError(f'{self.name} must not be above {self.upper_bound}')


class CharField(BaseValidator):
    def __init__(self, _min=0, _max=255):
        super().__init__(_min, _max)

    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.name} must be string')
        if len(value) < self.low_bound:
            raise ValueError(f'{self.name} must not be less than {self.low_bound}')
        if len(value) > self.upper_bound:
            raise ValueError(f'{self.name} must not be above {self.upper_bound}')


class Decimalfield(BaseValidator):
    def __init__(self, _min=0):
        super().__init__(_min)

    def validate(self, value):
        if value and value < self.low_bound:
            raise ValueError(f'{self.name} must not be less than {self.low_bound}')
        try:
            # will set this when perform calculations
            # w = decimal.getcontext()
            # w.prec = 2
            # w.rounding = decimal.ROUND_HALF_UP

            # print("prec:", w.prec)
            # print("rounding", w.rounding)
            d = Decimal(str(value))
            # print(d)
        except ValueError as ex:
            return "Improper value"
        else:
            return d

    def __set__(self, instance, value):
        a = self.validate(value)
        instance.__dict__[self.name] = a


        # if not isinstance(value, float):
        #     raise ValueError(f'{self.name} must be decimal value')

        # if len(value) > self.upper_bound:
        #     raise ValueError(f'{self.name} must not be above {self.upper_bound}')


class Boolean(BaseValidator):
    # def __init__(self, _min=0, _max=255):
    #     super().__init__(_min, _max)

    def validate(self, value):
        if not isinstance(value, bool):
            raise ValueError(f'{self.name} invalid value')


class EmailField(BaseValidator):
    def __init__(self, _min=4, _max=30):
        super().__init__(_min, _max)

    def validate(self, value):
        if not re.match('\S+@\S+', value):
            raise ValueError(f'{self.name} invalid email')
        if len(value) < self.low_bound:
            raise ValueError(f'{self.name} invalid email')

# class Person:
#     name = CharField(low_bound=2 , upper_bound =24)
#     age = IntegerField(low_bound= 0 , upper_bound= 150)
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return self.name
#
#     def __repr__(self):
#         return f'{type(self)}(name = {self.name}, age = {self.age})'


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