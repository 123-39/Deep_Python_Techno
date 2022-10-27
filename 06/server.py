"""
url pumping server
"""
import json
import socket
import threading
import time
from collections import Counter
from urllib.request import urlopen

import click
from bs4 import BeautifulSoup

REPLACE_DATA = ['\xa0', '\u2060', '\n', '\r', '\t', '/', '°',
                '0', '1', '2', '3', '4', '5', '6', '7', '8',
                '9', '-', '©', ':', ';', ',', '.', '!', '?',
                '  ', '|', '—', '(', ')', '{', '}', '[', ']',
                '\\', '*', '+', '=', '&'
                ]


def get_top_count_words(url, top):

    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    text = soup.get_text().lower()

    for sym in REPLACE_DATA:
        text = text.replace(sym, ' ')

    count = dict(Counter(text.split(' ')))

    try:
        del count['']
    except KeyError:
        pass

    count = dict(sorted(count.items(), key=lambda x: x[1], reverse=True)[:top])

    json_data = json.dumps(count, ensure_ascii=False)

    return json_data


class Server:

    def __init__(self, top_words, port=15_000, n_workers=5):
        self.top_word = top_words
        self.port = port
        self.n_workers = n_workers
        self.lock = threading.Lock()
        self.n_processed_urls = 0
        self.num_threads = 0
        self.sock = None

    def start_master(self):
        serv = threading.Thread(target=self.server, daemon=True)
        serv.start()

    def server(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('127.0.0.4', self.port))

        self.sock.listen(1000)

        self.n_processed_urls = 0
        self.num_threads = 0

        while True:

            client, _ = self.sock.accept()

            data = client.recv(4096)

            while self.num_threads >= self.n_workers:
                continue

            with self.lock:
                self.num_threads += 1

            thread = threading.Thread(
                target=self.workers,
                args=(data.decode(), self.top_word, client)
            )

            thread.start()

    def workers(self, url, top_word, client):
        json_response = get_top_count_words(url, top_word)

        client.send(json_response.encode())
        client.close()

        with self.lock:
            self.num_threads -= 1
            self.n_processed_urls += 1
            print(f'n_urls: {self.n_processed_urls}')

    def stop(self):
        self.sock.close()


@click.command(name='server_start')
@click.option('-w', default=5, help='number of workers')
@click.option('-k', default=3, help='number of top words')
def server_processing(w=5, k=3):

    server = Server(k, 15_000, w)

    server.start_master()

    time.sleep(2)

    while True:
        time.sleep(1)


if __name__ == "__main__":

    server_processing()
