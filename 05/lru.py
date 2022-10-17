"""
dynamic lru_cache
"""


class LRUCache:
    """
    LRUCache class
    """

    def __init__(self, limit=42):
        self.limit = limit
        self.current_size = 0
        self.key_delete_list = []
        self.cache = {}

    def get(self, key):
        """
        getter
        """
        try:
            self.key_delete_list.remove(key)
            self.key_delete_list.append(key)
            return self.cache[key]
        except ValueError:
            return None

    def set(self, key, value):
        """
        setter
        """
        if key in self.key_delete_list:
            self.key_delete_list.remove(key)
            self.cache.pop(key)
            self.current_size -= 1
        elif self.current_size == self.limit:
            self.cache.pop(self.key_delete_list[0])
            self.key_delete_list.pop(0)
            self.current_size -= 1

        self.key_delete_list.append(key)
        self.cache[key] = value
        self.current_size += 1
