"""
this module does competition for threads doing a function
"""
import threading

event = threading.Event()
word_for_input = 'djweiodw'
list_of_finished_names = []
winners = []


def competitor(y, name):
    """
    append to a list the name when finishes

    :param y: a num given
    :param name: the name of the thread
    :return:
    """
    global list_of_finished_names
    event.wait()
    x = y
    list_of_finished_names.append(name)


def main():
    """
    creates and event that runs 10 threads of competitor in same time,
    then append to a list the thread who finished first.
    """
    global list_of_finished_names
    global winners
    list_of_threads = []
    flag = True
    for num in range(10):
        list_of_threads.append(
            threading.Thread(target=competitor, args=[word_for_input, num]))
    for num in list_of_threads:
        num.start()
    event.set()
    while flag:
        if len(list_of_finished_names) == 10:
            winners.append(list_of_finished_names[0])
            flag = False
    list_of_finished_names = []


for num in range(5):
    event.clear()
    main()
print(winners)
