from enum import Enum, unique
"""
##################################
THIS MODEL CONTAINS ALL THE ENUMERATION CLASS
By: Lawrence Kusi Addai
##################################
"""
@unique
class Laky_Enum(Enum):
    Ok = (200, 'Successful')
    Failed = (203, 'Failed')
    Timeout = (404, 'timeout error, ')
    unknown_error = (-1, "Sorry, unknown error occurred")

    def __new__(cls, value, phrase):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.phrase = phrase
        return obj

    def __repr__(self):
        print("raper")
        return vars(self)

    # This wraps the property and allow to be called in different ways
    # Laky_Enum.Timeout.value OR Laky_Enum["Timeout"].code
    @property
    def message(self):
        return self.phrase

    @property
    def code(self):
        return self.value


if __name__ == "__main__":

    print(Laky_Enum["Timeout"].code, Laky_Enum["Timeout"].message)
    # or
    print(Laky_Enum.Timeout.value, Laky_Enum.Timeout.name, Laky_Enum.Timeout.phrase)
    print(isinstance(Laky_Enum.Timeout, Laky_Enum))