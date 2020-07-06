"""
this module checks for ports to adress
"""
import socket
from contextlib import suppress
import constant


def scan(adress):
    """
    scan for ports for adress given

    :param adress: the adress to which the socket tries to connect
    :return: valid port to adress
    """
    x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for num in range(constant.min, constant.max):
        with suppress(Exception):
            a, b = x.connect((adress, num))
            return num


def main():
    """
    activate scan() and connects to the '127.0.0.1' and the port returned
    """
    port = scan('127.0.0.1')
    x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    x.connect(('127.0.0.1', port))


if __name__ == "__main__":
    main()
