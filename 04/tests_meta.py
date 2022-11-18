""" CustomList class tests """
import unittest
from metaclass import CustomClass


class TestCustomClass(unittest.TestCase):

    def test_class_var(self):

        self.assertTrue(hasattr(CustomClass, 'custom_x'))
        self.assertFalse(hasattr(CustomClass, 'x'))

    def test_class_var_value(self):

        self.assertEqual(CustomClass.custom_x, 50)

    def test_inst_class_var(self):

        inst = CustomClass()
        self.assertTrue(hasattr(inst, 'custom_x'))
        self.assertTrue(hasattr(inst, 'custom_val'))
        self.assertFalse(hasattr(inst, 'x'))
        self.assertFalse(hasattr(inst, 'val'))

    def test_inst_class_var_value(self):

        inst = CustomClass(45)
        self.assertEqual(inst.custom_x, 50)
        self.assertEqual(inst.custom_val, 45)

    def test_class_method(self):

        inst = CustomClass()
        self.assertTrue(hasattr(inst, 'custom_line'))
        self.assertFalse(hasattr(inst, 'line'))

    def test_right_class_method_val(self):

        inst = CustomClass()
        self.assertTrue(inst.custom_line(), 100)

    def test_right_class_magic_method_val(self):

        inst = CustomClass()
        self.assertTrue(str(inst), "Custom_by_metaclass")

    def test_class_magic_methods(self):

        inst = CustomClass()
        self.assertTrue(hasattr(inst, '__str__'))
        self.assertFalse(hasattr(inst, 'custom___str__'))

    def test_class_dynamic_var(self):

        inst = CustomClass()
        inst.dynamic = "added later"
        self.assertTrue(hasattr(inst, 'custom_dynamic'))
        self.assertFalse(hasattr(inst, 'dynamic'))

    def test_class_fake_magic_method(self):

        inst = CustomClass()
        self.assertTrue(hasattr(inst, 'custom_static_line__'))
        self.assertFalse(hasattr(inst, 'static_line__'))

    def test_false_class_fake_magic_method_val(self):

        inst = CustomClass()
        self.assertTrue(inst.custom_static_line__(), 100)


if __name__ == "__main__":

    unittest.main()
