""" CustomList class tests """
import unittest
from unittest.mock import patch

from custom_list import CustomList


class TestCustomList(unittest.TestCase):

    # =================CustomList addition=================

    def test_true_custom_list_left_add(self):

        init_list1 = [1, 2]
        init_list2 = [3, 5, 6, 7]
        init_list3 = [4, 7, 6, 7]

        first = CustomList(init_list1.copy())
        second = CustomList(init_list2.copy())

        third_pred = first + second

        for i, _ in enumerate(init_list3):
            if i <= len(init_list1) - 1:
                self.assertEqual(first[i], init_list1[i])
            if i <= len(init_list2) - 1:
                self.assertEqual(second[i], init_list2[i])
            self.assertEqual(third_pred[i], init_list3[i])

    def test_true_custom_list_right_add(self):

        init_list1 = [3, 5, 6, 7]
        init_list2 = [1, 2]
        init_list3 = [4, 7, 6, 7]

        first = CustomList(init_list1.copy())
        second = CustomList(init_list2.copy())

        third_pred = first + second

        for i, _ in enumerate(init_list3):
            if i <= len(init_list1) - 1:
                self.assertEqual(first[i], init_list1[i])
            if i <= len(init_list2) - 1:
                self.assertEqual(second[i], init_list2[i])
            self.assertEqual(third_pred[i], init_list3[i])

    def test_false_custom_list_left_add(self):

        init_list1 = [1, 2]
        init_list2 = [3, 5, 6, 7]
        init_list3 = [0, 7, 3, 7]

        first = CustomList(init_list1.copy())
        second = CustomList(init_list2.copy())

        third_pred = first + second

        for i, _ in enumerate(init_list3):
            if i <= len(init_list1) - 1:
                self.assertEqual(first[i], init_list1[i])
            if i <= len(init_list2) - 1:
                self.assertEqual(second[i], init_list2[i])

        self.assertNotEqual(third_pred, CustomList(init_list3))

    def test_false_custom_list_right_add(self):

        init_list1 = [3, 5, 6, 7]
        init_list2 = [1, 2]
        init_list3 = [0, 7, 3, 7]

        first = CustomList(init_list1.copy())
        second = CustomList(init_list2.copy())

        third_pred = first + second

        for i, _ in enumerate(init_list3):
            if i <= len(init_list1) - 1:
                self.assertEqual(first[i], init_list1[i])
            if i <= len(init_list2) - 1:
                self.assertEqual(second[i], init_list2[i])

        self.assertNotEqual(third_pred, CustomList(init_list3))

    def test_true_custom_list_same_len_add(self):

        init_list1 = [1, 2]
        init_list2 = [3, 5]
        init_list3 = [4, 7]

        first = CustomList(init_list1.copy())
        second = CustomList(init_list2.copy())

        third_pred = first + second

        for i, _ in enumerate(init_list3):
            if i <= len(init_list1) - 1:
                self.assertEqual(first[i], init_list1[i])
            if i <= len(init_list2) - 1:
                self.assertEqual(second[i], init_list2[i])
            self.assertEqual(third_pred[i], init_list3[i])

    # =================CustomList with list addition=================

    def test_true_list_and_custom_list_left_add(self):

        init_list1 = [1, 2]
        init_list2 = [3, 5, 6, 7]
        init_list3 = [4, 7, 6, 7]

        first = init_list1.copy()
        second = CustomList(init_list2.copy())

        third_pred = first + second

        for i, _ in enumerate(init_list3):
            if i <= len(init_list1) - 1:
                self.assertEqual(first[i], init_list1[i])
            if i <= len(init_list2) - 1:
                self.assertEqual(second[i], init_list2[i])
            self.assertEqual(third_pred[i], init_list3[i])

    def test_true_list_and_custom_list_right_add(self):

        init_list1 = [1, 2]
        init_list2 = [3, 5, 6, 7]
        init_list3 = [4, 7, 6, 7]

        first = CustomList(init_list1.copy())
        second = init_list2.copy()

        third_pred = first + second

        for i, _ in enumerate(init_list3):
            if i <= len(init_list1) - 1:
                self.assertEqual(first[i], init_list1[i])
            if i <= len(init_list2) - 1:
                self.assertEqual(second[i], init_list2[i])
            self.assertEqual(third_pred[i], init_list3[i])

    def test_false_list_and_custom_list_right_add(self):

        init_list1 = [3, 5, 6, 7]
        init_list2 = [1, 2]
        init_list3 = [0, 7, 3, 7]

        first = CustomList(init_list1.copy())
        second = init_list2.copy()

        third_pred = first + second

        for i, _ in enumerate(init_list3):
            if i <= len(init_list1) - 1:
                self.assertEqual(first[i], init_list1[i])
            if i <= len(init_list2) - 1:
                self.assertEqual(second[i], init_list2[i])

        self.assertNotEqual(third_pred, CustomList(init_list3))

    def test_false_list_and_custom_list_left_add(self):

        init_list1 = [3, 5, 6, 7]
        init_list2 = [1, 2]
        init_list3 = [0, 7, 3, 7]

        first = init_list1.copy()
        second = CustomList(init_list2.copy())

        third_pred = first + second

        for i, _ in enumerate(init_list3):
            if i <= len(init_list1) - 1:
                self.assertEqual(first[i], init_list1[i])
            if i <= len(init_list2) - 1:
                self.assertEqual(second[i], init_list2[i])

        self.assertNotEqual(third_pred, CustomList(init_list3))

    # =================CustomList subtraction=================

    def test_true_custom_list_left_sub(self):

        init_list1 = [1, 2]
        init_list2 = [3, 5, 6, 7]
        init_list3 = [-2, -3, -6, -7]

        first = CustomList(init_list1.copy())
        second = CustomList(init_list2.copy())

        third_pred = first - second

        for i, _ in enumerate(init_list3):
            if i <= len(init_list1) - 1:
                self.assertEqual(first[i], init_list1[i])
            if i <= len(init_list2) - 1:
                self.assertEqual(second[i], init_list2[i])
            self.assertEqual(third_pred[i], init_list3[i])

    def test_true_custom_list_right_sub(self):

        init_list1 = [3, 5, 6, 7]
        init_list2 = [1, 2]
        init_list3 = [2, 3, 6, 7]

        first = CustomList(init_list1.copy())
        second = CustomList(init_list2.copy())

        third_pred = first - second

        for i, _ in enumerate(init_list3):
            if i <= len(init_list1) - 1:
                self.assertEqual(first[i], init_list1[i])
            if i <= len(init_list2) - 1:
                self.assertEqual(second[i], init_list2[i])
            self.assertEqual(third_pred[i], init_list3[i])

    def test_false_custom_list_left_sub(self):

        init_list1 = [1, 2]
        init_list2 = [3, 5, 6, 7]
        init_list3 = [0, -3, -6, -7]

        first = CustomList(init_list1.copy())
        second = CustomList(init_list2.copy())

        third_pred = first - second

        for i, _ in enumerate(init_list3):
            if i <= len(init_list1) - 1:
                self.assertEqual(first[i], init_list1[i])
            if i <= len(init_list2) - 1:
                self.assertEqual(second[i], init_list2[i])

        self.assertNotEqual(third_pred, CustomList(init_list3))

    def test_false_custom_list_right_sub(self):

        init_list1 = [3, 5, 6, 7]
        init_list2 = [1, 2]
        init_list3 = [2, 0, 6, 7]

        first = CustomList(init_list1.copy())
        second = CustomList(init_list2.copy())

        third_pred = first - second

        for i, _ in enumerate(init_list3):
            if i <= len(init_list1) - 1:
                self.assertEqual(first[i], init_list1[i])
            if i <= len(init_list2) - 1:
                self.assertEqual(second[i], init_list2[i])

        self.assertNotEqual(third_pred, CustomList(init_list3))

    def test_true_custom_list_same_len_sub(self):

        init_list1 = [1, 2]
        init_list2 = [3, 5]
        init_list3 = [-2, -3]

        first = CustomList(init_list1.copy())
        second = CustomList(init_list2.copy())

        third_pred = first - second

        for i, _ in enumerate(init_list3):
            if i <= len(init_list1) - 1:
                self.assertEqual(first[i], init_list1[i])
            if i <= len(init_list2) - 1:
                self.assertEqual(second[i], init_list2[i])
            self.assertEqual(third_pred[i], init_list3[i])

    # =================CustomList with list subtraction=================

    def test_true_list_and_custom_list_left_sub(self):

        init_list1 = [1, 2]
        init_list2 = [3, 5, 6, 7]
        init_list3 = [-2, -3, -6, -7]

        first = init_list1.copy()
        second = CustomList(init_list2.copy())

        third_pred = first - second

        for i, _ in enumerate(init_list3):
            if i <= len(init_list1) - 1:
                self.assertEqual(first[i], init_list1[i])
            if i <= len(init_list2) - 1:
                self.assertEqual(second[i], init_list2[i])
            self.assertEqual(third_pred[i], init_list3[i])

    def test_true_list_and_custom_list_right_sub(self):

        init_list1 = [3, 5, 6, 7]
        init_list2 = [1, 2]
        init_list3 = [2, 3, 6, 7]

        first = CustomList(init_list1.copy())
        second = init_list2.copy()

        third_pred = first - second

        for i, _ in enumerate(init_list3):
            if i <= len(init_list1) - 1:
                self.assertEqual(first[i], init_list1[i])
            if i <= len(init_list2) - 1:
                self.assertEqual(second[i], init_list2[i])
            self.assertEqual(third_pred[i], init_list3[i])

    def test_false_list_and_custom_list_right_sub(self):

        init_list1 = [3, 5, 6, 7]
        init_list2 = [1, 2]
        init_list3 = [0, -3, -6, -7]

        first = CustomList(init_list1.copy())
        second = init_list2.copy()

        third_pred = first - second

        for i, _ in enumerate(init_list3):
            if i <= len(init_list1) - 1:
                self.assertEqual(first[i], init_list1[i])
            if i <= len(init_list2) - 1:
                self.assertEqual(second[i], init_list2[i])

        self.assertNotEqual(third_pred, CustomList(init_list3))

    def test_false_list_and_custom_list_left_sub(self):

        init_list1 = [3, 5, 6, 7]
        init_list2 = [1, 2]
        init_list3 = [2, 0, 6, 7]

        first = init_list1.copy()
        second = CustomList(init_list2.copy())

        third_pred = first - second

        for i, _ in enumerate(init_list3):
            if i <= len(init_list1) - 1:
                self.assertEqual(first[i], init_list1[i])
            if i <= len(init_list2) - 1:
                self.assertEqual(second[i], init_list2[i])

        self.assertNotEqual(third_pred, CustomList(init_list3))

    # =================CustomList comparison=================

    def test_true_custom_lt(self):

        init_list1 = [1, 2, 3, 4]
        init_list2 = [40, 6]

        first = CustomList(init_list1.copy())
        second = CustomList(init_list2.copy())

        for i, _ in enumerate(init_list1):
            if i <= len(init_list1) - 1:
                self.assertEqual(first[i], init_list1[i])
            if i <= len(init_list2) - 1:
                self.assertEqual(second[i], init_list2[i])

        self.assertTrue(first < second)

    def test_true_custom_le(self):

        init_list1 = [1, 2, 3, 4]
        init_list2 = [4, 6]

        first = CustomList(init_list1.copy())
        second = CustomList(init_list2.copy())

        for i, _ in enumerate(init_list1):
            if i <= len(init_list1) - 1:
                self.assertEqual(first[i], init_list1[i])
            if i <= len(init_list2) - 1:
                self.assertEqual(second[i], init_list2[i])

        self.assertTrue(first <= second)

    def test_true_custom_eq(self):

        init_list1 = [1, 2, 3, 4, 5]
        init_list2 = [4, 5, 6]

        first = CustomList(init_list1.copy())
        second = CustomList(init_list2.copy())

        for i, _ in enumerate(init_list1):
            if i <= len(init_list1) - 1:
                self.assertEqual(first[i], init_list1[i])
            if i <= len(init_list2) - 1:
                self.assertEqual(second[i], init_list2[i])

        self.assertTrue(first == second)

    def test_true_custom_ne(self):

        init_list1 = [1, 2, 3, 3]
        init_list2 = [1, 2, 3]

        first = CustomList(init_list1.copy())
        second = CustomList(init_list2.copy())

        for i, _ in enumerate(init_list1):
            if i <= len(init_list1) - 1:
                self.assertEqual(first[i], init_list1[i])
            if i <= len(init_list2) - 1:
                self.assertEqual(second[i], init_list2[i])

        self.assertTrue(first != second)

    def test_true_custom_gt(self):

        init_list1 = [100, 2, 3, 3]
        init_list2 = [1, 2, 3]

        first = CustomList(init_list1.copy())
        second = CustomList(init_list2.copy())

        for i, _ in enumerate(init_list1):
            if i <= len(init_list1) - 1:
                self.assertEqual(first[i], init_list1[i])
            if i <= len(init_list2) - 1:
                self.assertEqual(second[i], init_list2[i])

        self.assertTrue(first > second)

    def test_true_custom_ge(self):

        init_list1 = [100, 2, 3, 2]
        init_list2 = [1, 2, 3, 50, 50]

        first = CustomList(init_list1.copy())
        second = CustomList(init_list2.copy())

        for i, _ in enumerate(init_list1):
            if i <= len(init_list1) - 1:
                self.assertEqual(first[i], init_list1[i])
            if i <= len(init_list2) - 1:
                self.assertEqual(second[i], init_list2[i])

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
