class Integer:
    """
    Int value
    """
    def __init__(self):
        self.__data = 0

    def __get__(self, *args, **kwargs):
        return self.__data

    def __set__(self, obj, val):

        if not isinstance(val, int):
            raise Exception('Not integer value')

        self.__data = val


class String:
    """
    Str value
    """
    def __init__(self):
        self.__data = ""

    def __get__(self, *args, **kwargs):
        return self.__data

    def __set__(self, obj, val):

        if not isinstance(val, str):
            raise Exception('Not string value')

        self.__data = val


class PositiveInteger:
    """
    Positiv int value
    """
    def __init__(self):
        self.__data = 0

    def __get__(self, *args, **kwargs):
        return self.__data

    def __set__(self, obj, val):

        if not isinstance(val, int):
            raise Exception('Not integer value')

        if val < 0:
            raise Exception('Not positive value')

        self.__data = val


class Data:
    """
    Descriptor
    """
    num = Integer()
    name = String()
    price = PositiveInteger()

    def __init__(self, num, name, price):
        # Integer
        self.num = num
        # String
        self.name = name
        # PositiveInteger
        self.price = price

    def __str__(self):
        return f"num: {self.num}, name: {self.name}, price: {self.price}"
