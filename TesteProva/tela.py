###############################################
#   Sistema Genérico para Supermercado v0.1   #
#   Eduardo Borges Siqueira                   #
#   Bernardo Gomes Duarte                     #
#   INE5404 - POO2                            #
#   24/09/2019                                #
###############################################

# Bibliotecas e classes
from tkinter import *
from Supermarket import Supermarket
from Product import Product

# Criação do supermercado
supermarket = Supermarket()

# Criação da janela principal
janelaPrincipal = Tk()

# Criação dos frames da janela principal
frameInicial = Frame(janelaPrincipal)
framePrincipal = Frame(janelaPrincipal)
frameProduto = Frame(janelaPrincipal)
frameConsulta = Frame(janelaPrincipal)

# Função de troca de frames
def raise_frame(frame):
    frame.tkraise()

# Função de saída do programa
def sair():
    janelaPrincipal.destroy()

# Função de validação de login
def enviarFormulario(username, password):
    if(supermarket.tryLogin(username, password)):
        raise_frame(framePrincipal)

# Função de troca de frame para a consulta de produtos
def consultaProduto():
    raise_frame(frameConsulta)

# Função que retorna as informações do produto, baseado no código de barras
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

# Laço de "empilhamento" dos frames na tela principal
for frame in (frameInicial, framePrincipal, frameProduto, frameConsulta):
    frame.grid(row=0, column=0, sticky='news')

# Frame Inicial #
# Campo de usuário
stringUsername = StringVar(value='Username')
username = Entry(frameInicial, textvariable=stringUsername)
username.pack(pady=15, padx=15, side=TOP)

# Campo de senha
stringPassword = StringVar(value="********")
password = Entry(frameInicial, textvariable=stringPassword, show='*')
password.pack(pady=15, padx=15, side=TOP)

# Botão de envio
submit = Button(frameInicial, text='SUBMIT', command= lambda:
enviarFormulario(username.get(),password.get()))
submit.pack(pady=15, padx=15, side=TOP)
# Fim do frame inicial #

# Frame Principal #
# Botão de cadastro de produtos
produtoButton = Button(framePrincipal, text='CADASTRAR', command= lambda:
raise_frame(frameProduto))
produtoButton.pack(pady=15, padx=15, side=TOP)

# Botão de consulta de produtos
pedidoButton = Button(framePrincipal, text='CONSULTAR', command= lambda:
consultaProduto())
pedidoButton.pack(pady=15, padx=15, side=TOP)

# Botão de saída do programa
sairButton = Button(framePrincipal, text='SAIR', command= lambda:
sair())
sairButton.pack(pady=15, padx=15, side=TOP)
# Fim do frame principal #

# Frame de cadastro de produtos #
# Campo de nome do produto
stringNome = StringVar(value='Nome')
nome = Entry(frameProduto, textvariable=stringNome)
nome.pack(pady=15, padx=15, side=TOP)

# Campo de preço do produto
stringPreco = StringVar(value='Preço')
preco = Entry(frameProduto, textvariable=stringPreco)
preco.pack(pady=0, padx=15, side=TOP)

# Campo de código do produto
stringCodigo = StringVar(value='Código')
codigo = Entry(frameProduto, textvariable=stringCodigo)
codigo.pack(pady=15, padx=15, side=TOP)

# Lista com as categorias dos produtos
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

# Menu com as categorias dos produtos
stringFuncao = StringVar(value='Categoria')
funcao = OptionMenu(frameProduto, stringFuncao, *funcoesList)
funcao.pack(pady=0, side=TOP)

# Botão de confirmação
confirmarButton = Button(frameProduto, text='CONFIRMAR', command= lambda:
supermarket.registerProduct(stringCodigo.get(), preco.get(), nome.get(), stringFuncao.get()))
confirmarButton.pack(pady=15, side=TOP)

# Botão para voltar ao menu principal
voltarButton = Button(frameProduto, text='VOLTAR', command= lambda:
raise_frame(framePrincipal))
voltarButton.pack(pady=15, side=TOP)
# Fim do frame de cadastro de produtos #

# Frame de consulta de produtos #
# Campo de código do produto para busca
stringProduto = StringVar(value='Digite o código')
codigo = Entry(frameConsulta, textvariable=stringProduto)
codigo.pack(pady=15, padx=15, side=TOP)

# Label com o nome do produto
nomeString = StringVar()
nomeLabel = Label(frameConsulta, textvariable=nomeString)
nomeLabel.pack(pady=1, padx=15, side=TOP)

# Label com o código do produto
codigoString = StringVar()
codigoLabel = Label(frameConsulta, textvariable=codigoString)
codigoLabel.pack(pady=1, padx=15, side=TOP)

# Label com a categoria do produto
categoriaString = StringVar()
categoriaLabel = Label(frameConsulta, textvariable=categoriaString)
categoriaLabel.pack(pady=1, padx=15, side=TOP)

# Label com o preço do produto
precoString = StringVar()
precoLabel = Label(frameConsulta, textvariable=precoString)
precoLabel.pack(pady=1, padx=15, side=TOP)

# Botão de envio
enviarButton = Button(frameConsulta, text='ENVIAR', command= lambda:
retornaInfo(stringProduto.get(), nomeString, codigoString, categoriaString, precoString))
enviarButton.pack(pady=0, padx=15, side=TOP)

# Botão para voltar ao menu principal
voltarButton = Button(frameConsulta, text='VOLTAR', command= lambda:
raise_frame(framePrincipal))
voltarButton.pack(pady=0, padx=15, side=TOP)
# Fim do frame de consulta de produtos #

# Definição do primeiro frame a ser apresentado
raise_frame(frameInicial)

# Laço infinito da janela principal
janelaPrincipal.mainloop()
