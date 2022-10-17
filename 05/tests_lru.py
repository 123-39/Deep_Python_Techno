""" LRUCache class tests """
import unittest

from lru import LRUCache


class TestLRUCache(unittest.TestCase):

    def test_initialization(self):

        cache = LRUCache(2)

        self.assertTrue(cache.limit, 2)

    def test_overflow_first(self):

        cache = LRUCache(3)

        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")
        cache.set("k4", "val4")

        self.assertEqual(cache.get("k4"), "val4")

    def test_double_overflow(self):

        cache = LRUCache(3)

        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")
        cache.set("k4", "val4")

        self.assertEqual(cache.get("k1"), None)
        cache.set("k5", "val5")
        self.assertEqual(cache.get("k2"), None)

    def test_overflow_last(self):

        cache = LRUCache(3)

        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")
        cache.set("k4", "val4")

        self.assertEqual(cache.get("k1"), None)

    def test_fake_overflow(self):

        cache = LRUCache(3)

        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")
        cache.set("k2", "val4")

        self.assertEqual(cache.get("k1"), "val1")
        self.assertEqual(cache.get("k2"), "val4")


if __name__ == "__main__":

    unittest.main()
