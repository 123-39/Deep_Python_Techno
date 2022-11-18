"""
CustomList
"""

import numpy as np


class CustomList(list):
    """
    CustomList class
    """

    @staticmethod
    def sub(left, right):
        """
        subtraction operation
        """
        if len(left) > len(right):
            add_val = left[:len(right)] - right
            add_val = np.append(add_val, left[len(right):])
        elif len(left) < len(right):
            add_val = left - right[:len(left)]
            add_val = np.append(add_val, -right[len(left):])
        else:
            return CustomList(left - right)
        return CustomList(add_val)

    @staticmethod
    def add(left, right):
        """
        addition operation
        """
        if len(left) > len(right):
            add_val = right + left[:len(right)]
            add_val = np.append(add_val, left[len(right):])
        elif len(left) < len(right):
            add_val = left + right[:len(left)]
            add_val = np.append(add_val, right[len(left):])
        else:
            return CustomList(left + right)
        return CustomList(add_val)

    def type_checking(self, other):
        """
        list or customlist checking
        """
        left = np.array(self)
        right = np.array(other)
        return left, right

    # def __init__(self, custm_list):
    #     super().__init__(self)
    #     self.custm_list = custm_list

    def __sub__(self, other):
        left, right = self.type_checking(other)
        return self.sub(left, right)

    def __rsub__(self, other):
        right, left = self.type_checking(other)
        return self.sub(left, right)

    def __add__(self, other):
        left, right = self.type_checking(other)
        return self.add(left, right)

    def __radd__(self, other):
        right, left = self.type_checking(other)
        return self.add(left, right)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __str__(self):
        return f"CustomList: {super().__str__()}." +\
             f" Sum of elements: {sum(self)}"
