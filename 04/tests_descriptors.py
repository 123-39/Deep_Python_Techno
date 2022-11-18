""" CustomList class tests """
import unittest
from descriptors import Data


class TestDescriptors(unittest.TestCase):

    def test_right_type_check(self):

        inst = Data(-5, 'kek', 10)
        self.assertIsInstance(inst.num, int)
        self.assertIsInstance(inst.name, str)
        self.assertIsInstance(inst.price, int)

    def test_output(self):

        inst = Data(-5, 'kek', 10)
        output = f"num: {-5}, name: {'kek'}, price: {10}"
        self.assertEqual(str(inst), output)

    def test_false_num(self):

        with self.assertRaises(Exception):
            Data('5', 'kek', 10)

    def test_false_name(self):

        with self.assertRaises(Exception):
            Data(5, 2.3, 10)

    def test_false_price_type(self):

        with self.assertRaises(Exception):
            Data(5, 'kek', 3.2)

    def test_false_price_sign(self):

        with self.assertRaises(Exception):
            Data(5, 'kek', -10)

    def test_new_bad_num(self):

        data = Data(100, 'abc', 1)
        with self.assertRaises(Exception):
            data.num = 'a'

        self.assertEqual(data.num, 100)

    def test_new_good_num(self):

        data = Data(100, 'abc', 1)
        data.num = 42

        self.assertEqual(data.num, 42)

    def test_new_bad_name(self):

        data = Data(100, 'abc', 1)
        with self.assertRaises(Exception):
            data.name = 42

        self.assertEqual(data.name, 'abc')

    def test_new_good_name(self):

        data = Data(100, 'abc', 1)
        data.name = 'zxy'

        self.assertEqual(data.name, 'zxy')

    def test_new_bad_price(self):

        data = Data(100, 'abc', 1)
        with self.assertRaises(Exception):
            data.price = -3

        self.assertEqual(data.price, 1)

    def test_new_good_price(self):

        data = Data(100, 'abc', 1)
        data.price = 5

        self.assertEqual(data.price, 5)


if __name__ == "__main__":

    unittest.main()
