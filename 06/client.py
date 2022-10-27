"""
url pumping client
"""
import json
import math
import socket
import threading

import click
import numpy as np


class Client:
    """
    client class
    """

    def __init__(self, urls=None, port=15_000, n_threads=5):
        self.urls = urls
        self.port = port
        self.n_threads = n_threads

    @staticmethod
    def separate_url(urls, n_threads):
        """
        separate urls for n threads
        """

        n_urls = math.ceil(len(urls) / n_threads)

        return np.array_split(urls, n_urls)

    def _worker(self, part_urls):
        """
        worker for each part urls
        """

        for urls in part_urls:

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('127.0.0.4', self.port))

            sock.send(urls.encode())
            data = sock.recv(4096)

            print(f'{urls}: ', data.decode())
            sock.close()

    def threads_creating(self):
        """
        creating and running threads
        """

        separated_urls = self.separate_url(self.urls, self.n_threads)

        threads = [
                   threading.Thread(target=self._worker, args=(part_urls,))
                   for part_urls in separated_urls
                   ]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()


@click.command(name='client_start')
@click.argument('n_threads', default=5)
@click.argument('data_path', default='urls.json')
def client_processing(data_path='urls.json', n_threads=5):
    """
    client commands for server
    """

    with open(data_path, 'r', encoding='utf-8') as json_file:
        urls = json.load(json_file)

    print('file: ', data_path)
    print('n_threds: ', n_threads)

    client = Client(urls, 15_000, n_threads)
    client.threads_creating()


if __name__ == '__main__':

    client_processing()
