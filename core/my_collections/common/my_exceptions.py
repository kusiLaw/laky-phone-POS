from my_enum import Laky_Enum
import json
import datetime

"""
##################################
THIS MODEL CONTAINS ALL THE Exception CLASS
By: Lawrence Kusi Addai
##################################
"""

# Base Exception
class LakyException(Exception):
    """
    this is the base exception all custom exceptions inherit from
    it accept Enum object or a raw stringe message, or empty/None
    if enum object(_message) is provided one or both (error_code,error_message) should be True
    else may show different results


    LakyException(
    args: any positional string arg.
    _message: enumerator instance,
    error_code: bool,
    error_message: bool,
    )

    example
    2. LakyException('hi, something wrong" , _message= Laky_Enum.Timeout)

    """
    default_error_message = Laky_Enum["unknown_error"].message
    default_error_code = Laky_Enum["unknown_error"].code
    extra_message = ""

    def __init__(self, *args, _message:enumerate = None, error_code = True, error_message= True):
        if args:
            self.reduce_(*args)

        if _message and isinstance(_message, Laky_Enum):
            # enum object, pass in to find it code and message
            self.default_error_message = _message.message
            self.default_error_code = _message.code

            if not error_code:
                super().__init__(f'{self.extra_message}{self.default_error_message}')
                return
            if not error_message:
                super().__init__(f'{self.extra_message} error code:{self.default_error_code}')
                return

            super().__init__(f'{self.extra_message} error code:{self.default_error_code} {self.default_error_message}')
            print("Emum type")
        elif self.extra_message:
            # Raw message provided
            super().__init__(f'{self.extra_message}')
            # print("raw message")
        else:
            # no message provided, used internal error message
            super().__init__(self.default_error_message)
            print("no meesage")


    def reduce_(self, *args) -> None:
        for x in args:
            if not isinstance(x, str):
                raise ValueError(f"Improper message type {type(x).__name__}")
            self.extra_message += x


    def to_json(self):
        caches = {
            'Error Type': type(self).__name__,
            'Error Code': self.default_error_code,
            'user_error_msg': self.default_error_message,
            'time ': datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        }

        return json.dumps(caches, indent=4)

    def log(self):
        log = {
            'Error Typpe': type(self).__name__,
            'Error Code': self.default_error_code,
            'user_error_msg': self.default_error_message,
            'time ': datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        }

        with open('log.txt', 'w') as f:
            f.write(json.dumps(log, indent=3))


class OutOfStockException(LakyException):
    pass


class SalesException(LakyException):
    pass


class InvalidSalesPrice(SalesException, ValueError):
    """
    it  inherit from sales exception
    """
    pass

class InvalidDiscount(SalesException):
    """
    it  inherit from sales exception
    """
    pass

if __name__ == "__main__":
    # print(help(LakyException))
    raise InvalidSalesPrice("",_message=Laky_Enum.Failed)

