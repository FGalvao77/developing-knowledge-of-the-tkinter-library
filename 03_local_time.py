# 03) visualizando a data e hora local

from tkinter import Tk, Button
from tkinter.messagebox import showinfo
from time import strftime, localtime


def clicked():
    time = strftime('Day: %d %b %Y\n Time: %H:%M:%S%p\n', localtime())
    showinfo(message=time)


root = Tk()
button = Button(root, text='Click', command=clicked)
button.pack()
root.mainloop()