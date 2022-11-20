"""
logger dynamic lru_cache
"""
import logging
import argparse

CACHE_SIZE = 12

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(name)s %(levelname)-7s: %(message)s',
    handlers=[
        logging.FileHandler('cache.log'),
    ]
)

logger = logging.getLogger('lru_cache')


class LRUCache:
    """
    LRUCache class
    """

    def __init__(self, limit=42):
        if limit < 1:
            logger.error('Cache size must be greater than or equal to 1')

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
            node = self.cache[key]
            logger.info('Was return element %s with key %s', node, key)
            return node
        except ValueError:
            logger.warning('Not existing key %s in cache', key)
            return None

    def set(self, key, value):
        """
        setter
        """
        if key in self.key_delete_list:
            logger.info('Key %s already exist in cache', key)
            self.key_delete_list.remove(key)
            self.cache.pop(key)
            self.current_size -= 1
            logger.info('Element with key %s was removed', key)
        elif self.current_size == self.limit:
            logger.warning('Cache is full')
            self.cache.pop(self.key_delete_list[0])
            self.key_delete_list.pop(0)
            self.current_size -= 1
            logger.info('Element with key %s was removed',
                        self.key_delete_list[0])

        logger.info('Adding new element %s with key %s in cache', value, key)
        self.key_delete_list.append(key)
        self.cache[key] = value
        self.current_size += 1


def logger_setting(cond: bool) -> None:
    """
    condition for stdout
    """

    if cond:
        stdout_log_format = logging.Formatter(
            '[%(asctime)s] [%(threadName)s] (%(name)s): %(message)s'
        )

        cli = logging.StreamHandler()
        cli.setFormatter(stdout_log_format)
        logger.addHandler(cli)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', type=int)  # -s can be 0 or 1

    args = parser.parse_args()

    logger_setting(args.s)

    cache = LRUCache(limit=CACHE_SIZE)

    for i in range(CACHE_SIZE):
        cache.set(i, "elem_" + str(i))

    cache.get(CACHE_SIZE - 1)
    cache.get(CACHE_SIZE - 2)
    cache.get(CACHE_SIZE - 3)

    for i in range(5):
        cache.set(CACHE_SIZE + i, "new_elem_" + str(CACHE_SIZE + i))

    cache.set(CACHE_SIZE + 1, CACHE_SIZE - 1)
