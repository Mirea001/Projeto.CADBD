from tkinter import *


class Aplication:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()

        self.msg = Label(self.widget1, text="Cadastro de Usuário")
        self.msg["font"] = ("Calibri", "13", "bold")
        self.msg.pack()

        self.usuarios = Button(self.widget1)
        self.usuarios["text"] = "Usuários"
        self.usuarios["font"] = ("Calibri", "10")
        self.usuarios["width"] = 7
       # self.usuarios["command"] = self.mudarpagina
        self.usuarios.pack(side=LEFT)

        self.cidade = Button(self.widget1)
        self.cidade["text"] = "Cidades"
        self.cidade["font"] = ("Calibri", "10")
        self.cidade["width"] = 5
        self.cidade.pack(side=LEFT)

        self.cliente = Button(self.widget1)
        self.cliente["text"] = "Clientes"
        self.cliente["font"] = ("Calibri", "10")
        self.cliente["width"] = 6
        self.cliente.pack(side=LEFT)

        self.fechar = Button(self.widget1)
        self.fechar["text"] = "Fechar"
        self.fechar["font"] = ("Calibri", "10")
        self.fechar["width"] = 5
        self.fechar["command"] = self.widget1.quit
        self.fechar.pack()


# def mudarpagina(self):
    #if self.msg["text"] == "Cadastro de Usuário":
     #   self.msg["text"] = "Informe os Dados"
    #else:
     #   self.msg["text"] = "Cadastro de Usuário"

    #self.msg2 = Label(self.widget1, text="Informe ps Dados")


root = Tk()
Aplication(root)
root.mainloop()
