"""
runs a kahoot server with multiple guests
"""
import socket

dict = {"who controlls this?": ["matan", "elad", "nadav", "losha","matan"],
        "who is the king?": ["matan", "of course matan", "definately matan",
                             "maybe matan","definately matan"]}


def main():
    """
    creates kahoot server, sending question and answers to connected guests
    :return:
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('192.168.43.53', 1521))
    server.listen()
    guestlist = []
    d, a = server.accept()
    guestlist.append(d)
    print("connected")
    answer = "matan"
    keylist = list(dict.keys())
    guestnames = []
    scoredict = {}

    for i in guestlist:
        r = i.recv(1000).decode()
        guestnames.append(r)

    for guest in guestnames:
        scoredict[guest] = 0

    for i in keylist:
        for soc in guestlist:
            x = i
            for num in dict[i]:
                x += ","
                x += num
            soc.send(x.encode())
        count = 0
        for soc in guestlist:
            rec = soc.recv(1000).decode()
            if (rec == "True"):
                scoredict[guestnames[count]] += 1
            else:
                pass
            count += 1
        scoreboard = []
        for name in guestnames:
            scoreboard.append(name + ": " + str(scoredict[name]))
        for soc in guestlist:
            soc.send(str(scoreboard).encode())


main()
