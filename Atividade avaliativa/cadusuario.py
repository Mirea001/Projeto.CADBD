from tkinter import *


class Paginacad:
    def __init__(self, master=None):
        self.widget2 = Frame(master)
        self.fontp = ("Calibri", "12")
        self.widget2.pack()

        self.msg = Label(self.widget2, text="Informe os dados:")
        self.msg["font"] = ("Calibri", "13", "bold")
        self.msg.pack()

        self.janela2 = Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.idLabel = Label(self.janela2, text="idUsuário:", font=self.fontp, width=10)
        self.idLabel.pack(side=LEFT)

        self.id = Entry(self.janela2)
        self.id["font"] = ("Calibri", "10")
        self.id["width"] = 10
        self.id.pack(side=LEFT)

        self.buscar = Button(self.janela2, text="Buscar", width=10)
        self.buscar["font"] = ("Calibri", "10")
        self.buscar["width"] = 10
        self.buscar.pack(side=RIGHT)

        self.janela3 = Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack()

        self.nomeLabel = Label(self.janela3, text="Nome:", font=self.fontp, width=10)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.janela3)
        self.nome["font"] = self.fontp
        self.nome["width"] = 25
        self.nome.pack(side=LEFT)

        self.janela4 = Frame(master)
        self.janela4["padx"] = 20
        self.janela4.pack()

        self.telefoneLabel = Label(self.janela4, text="Telefone:", font=self.fontp, width=10)
        self.telefoneLabel.pack(side=LEFT)

        self.telefone = Entry(self.janela4)
        self.telefone["font"] = self.fontp
        self.telefone["width"] = 25
        self.telefone.pack(side=LEFT)

        self.janela5 = Frame(master)
        self.janela5["padx"] = 20
        self.janela5.pack()

        self.emailLabel = Label(self.janela5, text="E-mail:", font=self.fontp, width=10)
        self.emailLabel.pack(side=LEFT)

        self.email = Entry(self.janela5)
        self.email["font"] = self.fontp
        self.email["width"] = 25
        self.email.pack(side=LEFT)

        self.janela6 = Frame(master)
        self.janela6["padx"] = 20
        self.janela6.pack()

        self.usuarioLabel = Label(self.janela6, text="Usuário:", font=self.fontp, width=10)
        self.usuarioLabel.pack(side=LEFT)

        self.usuario = Entry(self.janela6)
        self.usuario["font"] = self.fontp
        self.usuario["width"] = 25
        self.usuario.pack(side=LEFT)

        self.janela7 = Frame(master)
        self.janela7["padx"] = 20
        self.janela7.pack()

        self.senhaLabel = Label(self.janela7, text="Senha:", font=self.fontp, width=10)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.janela7)
        self.senha["font"] = self.fontp
        self.senha["width"] = 25
        self.senha.pack(side=LEFT)

        self.janela8 = Frame(master)
        self.janela8["padx"] = 20
        self.janela8.pack()

        self.inserir = Button(self.janela8)
        self.inserir["text"] = "Inserir"
        self.inserir["font"] = ("Calibri", "10")
        self.inserir["width"] = 10
        self.inserir.pack(side=LEFT)

        self.alterar = Button(self.janela8)
        self.alterar["text"] = "Alterar"
        self.alterar["font"] = ("Calibri", "10")
        self.alterar["width"] = 10
        self.alterar.pack(side=LEFT)

        self.excluir = Button(self.janela8)
        self.excluir["text"] = "Excluir"
        self.excluir["font"] = ("Calibri", "10")
        self.excluir["width"] = 10
        self.excluir.pack(side=LEFT)


root = Tk()
Paginacad(root)
root.mainloop()
