"""
this module writes to a file input from user
"""
import threading
import queue

q = queue.Queue()


def read():
    """
    takes input from user and put it into global queue
    """
    global q
    while True:
        x = input('please enter a number')
        q.put(int(x))


def write():
    """
    takes arguments from global queue and writes them to file.
    """
    global q

    while True:
        file = open("file5.txt", "a")
        t = q.get()
        file.write(str(t))


def main():
    """
    starts threads of read and write.

    :return:
    """
    global q
    r = threading.Thread(target=read)
    w = threading.Thread(target=write)
    r.start()
    w.start()


if __name__ == "__main__":
    main()
