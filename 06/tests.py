"""
some tests
"""
import unittest
import time
from server import Server, get_top_count_words
from client import Client


class TestClientServer(unittest.TestCase):

    def test_url_parser(self):

        url = 'https://www.worldpressphoto.org/'

        res = get_top_count_words(url, 5)
        right_res = '{"the": 27, "and": 13, "to": 11, "world": 10, "of": 9}'
        self.assertEqual(right_res, res)

    def test_start_server_client(self):

        urls = [
            'https://edition.cnn.com/',
            'https://drive.google.com',
        ]

        server = Server(7, 15_000, 5)
        server.start_master()
        time.sleep(1)

        client = Client(urls, 15_000, 5)
        client.threads_creating()

        time.sleep(1)
        server.stop()


if __name__ == "__main__":
    unittest.main()
