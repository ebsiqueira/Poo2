from tkinter import *

janelaPrincipal = Tk()

framePrincipal = Frame(janelaPrincipal)
frameFuncionario = Frame(janelaPrincipal)

def raise_frame(frame):
    frame.tkraise()

def sair():
    janelaPrincipal.destroy()

for frame in (framePrincipal, frameFuncionario):
    frame.grid(row=0, column=0, sticky='news')

##Frame Principal
funcionarioButton = Button(framePrincipal, text='FUNCIONÁRIO', command= lambda:
raise_frame(frameFuncionario))
funcionarioButton.pack(pady=15, side=TOP)

pedidoButton = Button(framePrincipal, text='FAZER PEDIDO', command= lambda:
enviarFormulario())
pedidoButton.pack(pady=15, side=TOP)

sairButton = Button(framePrincipal, text='SAIR', command= lambda:
sair())
sairButton.pack(pady=15, side=TOP)
####

##Frame Funcionario
funcionariosList = [
    'Novo Funcionário'
]

stringNovo = StringVar(value='Novo Funcionário')
funcionarioOm = OptionMenu(frameFuncionario, stringNovo, *funcionariosList)
funcionarioOm.pack(pady=0, side=TOP)

def AddFuncionario(funcionario):
    funcionariosList.append(funcionario.get())
    menu = funcionarioOm["menu"]
    menu.delete(0, "end")

    for string in funcionariosList:
            menu.add_command(label=string,
                             command=lambda value=string: funcionario.set(value))
    print(funcionariosList)


if(stringNovo.get() == 'Novo Funcionário'):
    stringNome = StringVar(value='Nome')
    nome = Entry(frameFuncionario, textvariable=stringNome)
    nome.pack(pady=15, padx=15, side=TOP)

    funcoesList = [
        'Atendente',
        'Caixa',
        'Gerente',
        'Pizzaiolo',
        'Garçom',
        'Entregador'
    ]

    stringFuncao = StringVar(value='Função')
    funcao = OptionMenu(frameFuncionario, stringFuncao, *funcoesList)
    funcao.pack(pady=0, side=TOP)

    confirmarButton = Button(frameFuncionario, text='CONFIRMAR', command= lambda:
    AddFuncionario(stringNome))
    confirmarButton.pack(pady=15, side=TOP)

voltarButton = Button(frameFuncionario, text='VOLTAR', command= lambda:
raise_frame(framePrincipal))
voltarButton.pack(pady=15, side=TOP)
####

raise_frame(framePrincipal)
janelaPrincipal.mainloop()
