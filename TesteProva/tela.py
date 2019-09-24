from tkinter import *
from Supermarket import Supermarket
from Product import Product

supermarket = Supermarket()
janelaPrincipal = Tk()

frameInicial = Frame(janelaPrincipal)
framePrincipal = Frame(janelaPrincipal)
frameProduto = Frame(janelaPrincipal)
frameConsulta = Frame(janelaPrincipal)

def raise_frame(frame):
    frame.tkraise()

def sair():
    janelaPrincipal.destroy()

def enviarFormulario(username, password):
    if(supermarket.tryLogin(username, password)):
        raise_frame(framePrincipal)

def consultaProduto():
    raise_frame(frameConsulta)

def retornaInfo(barCode, nomeString, codigoString, categoriaString, precoString):
    produto = supermarket.consulteProduct(barCode)
    print('BarCode sendo passado:', barCode)
    if(produto == 0):
        return 0
    print(produto)
    nomeString.set('Nome:'+produto.name)
    codigoString.set('Codigo:'+produto.barCode)
    categoriaString.set('Tipo: '+produto.type)
    precoString.set('Preco: '+produto.price)

for frame in (frameInicial, framePrincipal, frameProduto, frameConsulta):
    frame.grid(row=0, column=0, sticky='news')

##Frame Inicial
stringUsername = StringVar(value='Username')
username = Entry(frameInicial, textvariable=stringUsername)
username.pack(pady=15, padx=15, side=TOP)
stringPassword = StringVar(value="********")
password = Entry(frameInicial, textvariable=stringPassword, show='*')
password.pack(pady=15, padx=15, side=TOP)
submit = Button(frameInicial, text='SUBMIT', command= lambda:
enviarFormulario(username.get(),password.get()))
submit.pack(pady=15, padx=15, side=TOP)

##Frame Principal
produtoButton = Button(framePrincipal, text='CADASTRAR', command= lambda:
raise_frame(frameProduto))
produtoButton.pack(pady=15, padx=15, side=TOP)

pedidoButton = Button(framePrincipal, text='CONSULTAR', command= lambda:
consultaProduto())
pedidoButton.pack(pady=15, padx=15, side=TOP)

sairButton = Button(framePrincipal, text='SAIR', command= lambda:
sair())
sairButton.pack(pady=15, padx=15, side=TOP)
####

##Frame Produto
stringNome = StringVar(value='Nome')
nome = Entry(frameProduto, textvariable=stringNome)
nome.pack(pady=15, padx=15, side=TOP)

stringPreco = StringVar(value='Preço')
preco = Entry(frameProduto, textvariable=stringPreco)
preco.pack(pady=0, padx=15, side=TOP)

stringCodigo = StringVar(value='Código')
codigo = Entry(frameProduto, textvariable=stringCodigo)
codigo.pack(pady=15, padx=15, side=TOP)

funcoesList = [
    'Açougue',
    'Bebida',
    'Aves',
    'Bazar',
    'Frios',
    'Higiene',
    'Hortifruti',
    'Mercearia',
    'Padaria',
    'Pescados',
    'Eletrotônico'
]

stringFuncao = StringVar(value='Categoria')
funcao = OptionMenu(frameProduto, stringFuncao, *funcoesList)
funcao.pack(pady=0, side=TOP)

confirmarButton = Button(frameProduto, text='CONFIRMAR', command= lambda:
supermarket.registerProduct(stringCodigo.get(), preco.get(), nome.get(), stringFuncao.get()))
confirmarButton.pack(pady=15, side=TOP)

voltarButton = Button(frameProduto, text='VOLTAR', command= lambda:
raise_frame(framePrincipal))
voltarButton.pack(pady=15, side=TOP)
####

##Frame Consulta
stringProduto = StringVar(value='Digite o código')
codigo = Entry(frameConsulta, textvariable=stringProduto)
codigo.pack(pady=15, padx=15, side=TOP)

nomeString = StringVar()
nomeLabel = Label(frameConsulta, textvariable=nomeString)
nomeLabel.pack(pady=1, padx=15, side=TOP)

codigoString = StringVar()
codigoLabel = Label(frameConsulta, textvariable=codigoString)
codigoLabel.pack(pady=1, padx=15, side=TOP)

categoriaString = StringVar()
categoriaLabel = Label(frameConsulta, textvariable=categoriaString)
categoriaLabel.pack(pady=1, padx=15, side=TOP)

precoString = StringVar()
precoLabel = Label(frameConsulta, textvariable=precoString)
precoLabel.pack(pady=1, padx=15, side=TOP)

enviarButton = Button(frameConsulta, text='ENVIAR', command= lambda:
retornaInfo(stringProduto.get(), nomeString, codigoString, categoriaString, precoString))
enviarButton.pack(pady=0, padx=15, side=TOP)

voltarButton = Button(frameConsulta, text='VOLTAR', command= lambda:
raise_frame(framePrincipal))
voltarButton.pack(pady=0, padx=15, side=TOP)

raise_frame(frameInicial)
janelaPrincipal.mainloop()
