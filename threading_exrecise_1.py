"""
this module writes to a file a word using 2 threads
"""
from pathlib import Path
from threading import Event, Thread

STRING = "synchronization"
FILE = Path.cwd() / "file.txt"
printed_odd = Event()
printed_even = Event()


def write_even():
    """
    write odd placed letters from STRING
    """
    for char in STRING[1::2]:
        printed_odd.wait()
        print(char)
        printed_even.set()
        printed_odd.clear()


def main():
    """
    write even and odd letters from String using two threads
    """
    even_printer = Thread(target=write_even)
    even_printer.start()

    printed_even.set()

    for char in STRING[::2]:
        printed_even.wait()
        print(char)
        printed_odd.set()
        printed_even.clear()

    even_printer.join()


if __name__ == '__main__':
    main()
