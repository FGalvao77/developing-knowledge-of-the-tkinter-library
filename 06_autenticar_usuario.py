# 06) autenticação de usuário Id e senha

from tkinter import Tk, Frame, Label, Entry, Button, LEFT


class App():
    def __init__(self, master=None):
        self.fontePadrao = ('Arial', '10')

        self.primeiroContainer = Frame(master)
        self.primeiroContainer['pady'] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer['padx'] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer['padx'] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer['pady'] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text='DADOS DO USUÁRIO')
        self.titulo['font'] = ('Arial', '10', 'bold')
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer, text='Nome: ')
        self.nomeLabel['font'] = ('Arial', '10', 'bold')
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer, font=self.fontePadrao)
        self.nome['width'] = 30
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text='Senha: ')
        self.senhaLabel['font'] = ('Arial', '10', 'bold')
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha['width'] = 30
        self.senha['font'] = self.fontePadrao
        self.senha['show'] = '*'
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar['text'] = 'Autenticar'
        self.autenticar['font'] = ('Calibri', '8', 'bold')
        self.autenticar['width'] = 12
        self.autenticar['command'] = self.verificaSenha
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text='')
        self.mensagem['font'] = self.fontePadrao
        self.mensagem.pack()

    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()

        if usuario == 'usuario' and senha == '1234':
            self.mensagem['text'] = '\nUsuário autenticado'
        else:
            self.mensagem['text'] = '\nErro na autenticação'


root = Tk()
App(root)
root.mainloop()