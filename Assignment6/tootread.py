import socket
import os
import time
from mastodon import Mastodon, StreamListener

#############################
#   CHANGE BEFORE RUNNING   #
#############################

client_key = 'YOUR-CLIENT-KEY-HERE'
client_secret = 'YOUR-CLIENT-SECRET-HERE'
access_token = 'YOUR-ACCESS-TOKEN-HERE'

#############################

api_base_url = 'https://mastodon.social'


class TootListener(StreamListener):

    def __init__(self, c_socket):
        self.client_socket = c_socket

    def on_update(self, status):
        try:
            text = status['content'] + '\n'
            print(text.encode('utf-8'))
            self.client_socket.send(text.encode('utf-8'))
            return True
        except BaseException as e:
            print('Error on_update: {}'.format(e))
        return True


def send_data(c_socket):
    stream_listener = TootListener(c_socket)
    mastodon = Mastodon(client_key, client_secret, access_token, api_base_url)

    mastodon.stream_public(stream_listener)


if __name__ == '__main__':
    s = socket.socket()
    host = '127.0.0.1'
    port = 5555

    s.bind((host, port))

    print('Listening on port: {}'.format(port))

    s.listen(5)
    c, addr = s.accept()

    print('Received request from: {}'.format(addr))

    send_data(c)
