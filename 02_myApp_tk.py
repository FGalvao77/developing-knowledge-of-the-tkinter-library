# 02) criando uma janela gráfica com componentes - texto e botão

from tkinter import Tk, Frame, Label, Button, BOTTOM, TOP


class MyApp:

    def __init__(self, master=None):
        self.widget = Frame(master)
        self.widget.pack(side=TOP)

        self.msg = Label(self.widget, text='My first widget')
        self.msg['font'] = ('Verdana', '10', 'italic', 'bold')
        self.msg.pack()

        self.exit = Button(self.widget)
        self.exit['text'] = 'Exit'
        self.exit['font'] = ('Verdana', '10')
        self.exit['width'] = 5
        self.exit['command'] = self.widget.quit
        self.exit.pack(side=BOTTOM)


root = Tk()
MyApp(root)
root.mainloop()
