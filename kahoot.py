"""
runs a kahoot practicipant that answers questions shown
"""
import tkinter as tk
import socket
import time
global window3
global window1
def question(question, answer1, answer2, answer3, answer4, rightanswer):
    """
    asks a questuin with answers given using tkinter
    :param question: question to ask
    :param answer1: possible answer
    :param answer2: possible answer
    :param answer3: possible answer
    :param answer4: possible answer
    :param rightanswer: the right answer
    :return:
    """
    def checkanswer(answer, goodanswer):
        """
        cheks if answer given is right answer using tkinter
        :param answer: the answer chosen
        :param goodanswer: the right answer
        :return:
        """
        if answer == goodanswer:
            root.destroy()
            window.destroy()
            window1 = tk.Tk()
            window1.geometry("200x200+800+300")
            T1 = tk.Text(window1)
            T1.pack()
            T1.insert(tk.END, "you are right")
            T1.configure(background="blue")
            T1.config(font=("Courier", 15))
            soc.send("True".encode())
            r = soc.recv(10000).decode()
            window3 = tk.Tk()
            window3.title("score table")
            window3.geometry("400x400+300+300")
            T3 = tk.Text(window3)
            T3.pack()
            T3.insert(tk.END, r)
            T3.configure(background="green")
            T3.config(font=("Courier", 15))
            window3.after(5000, lambda: window3.destroy())
            window1.after(5000, lambda: window1.destroy())

        else:
            root.destroy()
            window.destroy()
            window1 = tk.Tk()
            window1.geometry("200x200+800+300")
            T1 = tk.Text(window1)
            T1.pack()
            T1.insert(tk.END, "you are wrong")
            T1.configure(background="red")
            T1.config(font=("Courier", 15))
            soc.send("False".encode())
            r = soc.recv(10000).decode()
            window3 = tk.Tk()
            window3.title("score table")
            window3.geometry("400x400+300+300")
            T3 = tk.Text(window3)
            T3.pack()
            T3.insert(tk.END, r)
            T3.configure(background="green")
            T3.config(font=("Courier", 15))
            window3.after(5000, lambda: window3.destroy())
            window1.after(5000, lambda: window1.destroy())

    root = tk.Tk()
    root.geometry("500x100+400+300")
    abutton1 = tk.Button(root, text=answer1, width=80,
                         command=lambda: checkanswer(answer1, rightanswer))
    abutton1.configure(bg="red")
    abutton1.pack(side=tk.TOP)

    abutton2 = tk.Button(root, text=answer2, width=80,
                         command=lambda: checkanswer(answer2, rightanswer))
    abutton2.pack(side=tk.TOP)
    abutton2.configure(bg="blue")
    abutton3 = tk.Button(root, text=answer3, width=80,
                         command=lambda: checkanswer(answer3, rightanswer))
    abutton3.pack(side=tk.TOP)
    abutton3.configure(bg="green")
    abutton4 = tk.Button(root, text=answer4, width=80,
                         command=lambda: checkanswer(answer4, rightanswer))
    abutton4.pack(side=tk.TOP)
    abutton4.configure(bg="purple")

    window = tk.Tk()
    window.geometry("700x60+400+100")
    T = tk.Text(window)
    T.pack()
    T.insert(tk.END, question)
    T.config(font=("Courier", 25))
    tk.mainloop()


global soc
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(('192.168.43.53', 1521))
print("please give yourself a name:")
name = input()
soc.send(name.encode())
while True:
    rec = soc.recv(10000).decode()
    lis = rec.split(",")
    question(lis[0], lis[1], lis[2], lis[3], lis[4], lis[5])
