""" CustomList class tests """
import unittest
from unittest.mock import patch

from custom_list import CustomList


class TestCustomList(unittest.TestCase):

    # =================CustomList addition=================

    def test_true_custom_list_left_add(self):

        first = CustomList([1, 2])
        second = CustomList([3, 5, 6, 7])
        third = CustomList([4, 7, 6, 7])
        self.assertEqual(first + second, third)

    def test_true_custom_list_right_add(self):

        first = CustomList([3, 5, 6, 7])
        second = CustomList([1, 2])
        third = CustomList([4, 7, 6, 7])
        self.assertEqual(first + second, third)

    def test_false_custom_list_left_add(self):

        first = CustomList([1, 2])
        second = CustomList([3, 5, 6, 7])
        third = CustomList([0, 7, 3, 7])
        self.assertNotEqual(first + second, third)

    def test_false_custom_list_right_add(self):

        first = CustomList([3, 5, 6, 7])
        second = CustomList([1, 2])
        third = CustomList([0, 7, 3, 7])
        self.assertNotEqual(first + second, third)

    def test_true_custom_list_same_len_add(self):

        first = CustomList([1, 2])
        second = CustomList([3, 5])
        third = CustomList([4, 7])
        self.assertEqual(first + second, third)

    # =================CustomList with list addition=================

    def test_true_list_and_custom_list_left_add(self):

        first = [1, 2]
        second = CustomList([3, 5, 6, 7])
        third = CustomList([4, 7, 6, 7])
        self.assertEqual(first + second, third)

    def test_true_list_and_custom_list_right_add(self):

        first = CustomList([1, 2])
        second = [3, 5, 6, 7]
        third = CustomList([4, 7, 6, 7])
        self.assertEqual(first + second, third)

    def test_false_list_and_custom_list_right_add(self):

        first = CustomList([3, 5, 6, 7])
        second = [1, 2]
        third = CustomList([0, 7, 3, 7])
        self.assertNotEqual(first + second, third)

    def test_false_list_and_custom_list_left_add(self):

        first = [3, 5, 6, 7]
        second = CustomList([1, 2])
        third = CustomList([0, 7, 3, 7])
        self.assertNotEqual(first + second, third)

    # =================CustomList subtraction=================

    def test_true_custom_list_left_sub(self):

        first = CustomList([1, 2])
        second = CustomList([3, 5, 6, 7])
        third = CustomList([-2, -3, -6, -7])
        self.assertEqual(first - second, third)

    def test_true_custom_list_right_sub(self):

        first = CustomList([3, 5, 6, 7])
        second = CustomList([1, 2])
        third = CustomList([2, 3, 6, 7])
        self.assertEqual(first - second, third)

    def test_false_custom_list_left_sub(self):

        first = CustomList([1, 2])
        second = CustomList([3, 5, 6, 7])
        third = CustomList([0, -3, -6, -7])
        self.assertNotEqual(first - second, third)

    def test_false_custom_list_right_sub(self):

        first = CustomList([3, 5, 6, 7])
        second = CustomList([1, 2])
        third = CustomList([2, 0, 6, 7])
        self.assertNotEqual(first + second, third)

    def test_true_custom_list_same_len_sub(self):

        first = CustomList([1, 2])
        second = CustomList([3, 5])
        third = CustomList([-2, -3])
        self.assertEqual(first - second, third)

    # =================CustomList with list subtraction=================

    def test_true_list_and_custom_list_left_sub(self):

        first = [1, 2]
        second = CustomList([3, 5, 6, 7])
        third = CustomList([-2, -3, -6, -7])
        self.assertEqual(first - second, third)

    def test_true_list_and_custom_list_right_sub(self):

        first = CustomList([3, 5, 6, 7])
        second = [1, 2]
        third = CustomList([2, 3, 6, 7])
        self.assertEqual(first - second, third)

    def test_false_list_and_custom_list_right_sub(self):

        first = CustomList([3, 5, 6, 7])
        second = [1, 2]
        third = CustomList([0, -3, -6, -7])
        self.assertNotEqual(first - second, third)

    def test_false_list_and_custom_list_left_sub(self):

        first = [3, 5, 6, 7]
        second = CustomList([1, 2])
        third = CustomList([2, 0, 6, 7])
        self.assertNotEqual(first + second, third)

    # =================CustomList comparison=================

    def test_true_custom_lt(self):

        first = CustomList([1, 2, 3, 4])
        second = CustomList([40, 6])
        self.assertTrue(first < second)

    def test_true_custom_le(self):

        first = CustomList([1, 2, 3, 4])
        second = CustomList([4, 6])
        self.assertTrue(first <= second)

    def test_true_custom_eq(self):

        first = CustomList([1, 2, 3, 4, 5])
        second = CustomList([4, 5, 6])
        self.assertTrue(first == second)

    def test_true_custom_ne(self):

        first = CustomList([1, 2, 3, 3])
        second = CustomList([1, 2, 3])
        self.assertTrue(first != second)

    def test_true_custom_gt(self):

        first = CustomList([100, 2, 3, 3])
        second = CustomList([1, 2, 3])
        self.assertTrue(first > second)

    def test_true_custom_ge(self):

        first = CustomList([100, 2, 3, 2])
        second = CustomList([1, 2, 3, 50, 50])
        self.assertTrue(first >= second)

    # =================CustomList print=================

    @patch('builtins.print')
    def test_print(self, mock_print):
        """
        Print callback test
        """
        first = CustomList([100, 2, 3, 2])
        print(first.__str__())
        output = f"CustomList: {[100, 2, 3, 2]}. Sum of elements: {107}"
        mock_print.assert_called_with(output)


if __name__ == "__main__":

    unittest.main()
