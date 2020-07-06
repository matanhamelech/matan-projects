"""
this module checks for ports to adress with async.io
"""
import socket
import asyncio
import time
from contextlib import suppress
import constant

port = 0


def timer(func):
    async def wrapper(*args, **kwargs):
        t1 = time.time()
        result = await func(*args, **kwargs)
        t2 = time.time()
        print(t2 - t1)
        return result

    return wrapper


async def check_port(try_port: int):
    """
    check if a port for a socket is valid and save it as global i if True
    :param try_port: the port for the socket to try and connect with
    """
    with suppress(Exception):
        global port
        await asyncio.open_connection(constant.host, try_port)
        print(f"{try_port} found")
        port = try_port


@timer
async def main():
    """
    Scan a range of ports
    """
    await asyncio.gather(
        *[check_port(i) for i in range(constant.range_of_ports)])
    print(f'port for {constant.host} is {port}')


if __name__ == "__main__":
    asyncio.run(main())
