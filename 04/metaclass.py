"""
Custom Class
"""


class CustomMeta(type):
    """
    Add "custom_" class
    """
    def __new__(cls, name, bases, classdict):
        custom_class_dict = {}
        for method, val in classdict.items():
            if not method.startswith('__'):
                custom_class_dict["custom_" + method] = val
            else:
                custom_class_dict[method] = val

        custom_class_dict['__setattr__'] = CustomMeta.__setattr__
        custom_cls = super().__new__(cls, name, bases, custom_class_dict)
        return custom_cls

    def __setattr__(cls, name, value):
        cls.__dict__['custom_' + name] = value


class CustomClass(metaclass=CustomMeta):
    """
    Meta class
    """
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        """
        Class method
        """
        return 100

    def __str__(self):
        return "Custom_by_metaclass"

    def static_line__(self):
        """
        method with "__" on the end
        """
        return 100
