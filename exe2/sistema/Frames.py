from tkinter import *

class Frames:
    def __init__(self):
        self.janelaPrincipal = Tk()
        self.framePrincipal = Frame(self.janelaPrincipal)
        self.frameCadastro = Frame(self.janelaPrincipal)
        self.janelaPrincipal.mainloop()


    def updateFrameGrid(self):
        for frame in (self.framePrincipal, self.frameCadastro):
            frame.grid(row=0, column=0, sticky='news')

    def principalWindow(self):
        self.framePrincipal.tkraise()
        cadastrarButton = Button(self.framePrincipal, text='CADASTRAR', command= lambda:
        cadastro())
        cadastrarButton.pack(pady=15, side=TOP)

        pedidoButton = Button(self.framePrincipal, text='FAZER PEDIDO', command= lambda:
        enviarFormulario())
        pedidoButton.pack(pady=15, side=TOP)

        sairButton = Button(self.framePrincipal, text='SAIR', command= lambda:
        sair())
        sairButton.pack(pady=15, side=TOP)

    def cadastroWindow(self):
        raise_frame(self.frameCadastro)
        cadastrarButton = Button(self.frameCadastro, text='CADASTRAR', command= lambda:
        enviarFormulario())
        cadastrarButton.pack(pady=15, side=TOP)

    def sair(self):
        janelaPrincipal.destroy()
