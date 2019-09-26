###############################################
#   Sistema Genérico para Papelaria (Prova 1) #
#   Eduardo Borges Siqueira                   #                  
#   INE5404 - POO2                            #
#   26/09/2019                                #
###############################################

# Usuário padrão: root
# Senha padrão: toor

# Bibliotecas e classes
from tkinter import *
from tkinter import messagebox
from Papelaria import Papelaria
from Produto import Produto

# Criação do supermercado
papelaria = Papelaria()

# Criação da janela principal
janelaPrincipal = Tk()
# Título da janela principal
janelaPrincipal.title('Papelaria')

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
def enviarFormulario(usuario, senha):
    if(papelaria.realizaLogin(usuario, senha)):
        raise_frame(framePrincipal)
    else:
        messagebox.showerror("ERRO", "O nome de usuário e/ou a senha são inválidos!")

# Função de troca de frame para a consulta de produtos
def consultaProduto():
    raise_frame(frameConsulta)

# Função de cadastro de produtos
def cadastraProduto():
        papelaria.registraProduto(stringCodigo.get(), preco.get(), nome.get(), stringFuncao.get())
        messagebox.showinfo("Cadastro", "Cadastro do produto realizado com sucesso!")
        raise_frame(framePrincipal)

# Função que retorna as informações do produto, baseado no código de barras
def retornaInfo(codigo, nomeString, codigoString, categoriaString, precoString):
    produto = papelaria.consultaProduto(codigo)
    if(produto == 0):
        messagebox.showerror("ERRO", "Não foram encontrados produtos com esse código!")
        return 0
    if(produto.tipo == 'Brinquedo'):
        nomeString.set('Nome: '+produto.nome)
        codigoString.set('Codigo: '+produto.codigo)
        categoriaString.set('Tipo: '+produto.tipo)
        precoString.set('Preco: R$'+produto.preco)
        brindeString.set('Você ganhou um brinde!!!')
    else:
        nomeString.set('Nome: '+produto.nome)
        codigoString.set('Codigo: '+produto.codigo)
        categoriaString.set('Tipo: '+produto.tipo)
        precoString.set('Preco: R$'+produto.preco)

# Laço de "empilhamento" dos frames na tela principal
for frame in (frameInicial, framePrincipal, frameProduto, frameConsulta):
    # Coloca todos os frames na tela, em todas as orientações
    frame.grid(row=0, column=0, sticky='news')

# Frame Inicial #
# Campo de usuário
stringUsuario = StringVar(value='Usuario')
usuario = Entry(frameInicial, textvariable=stringUsuario)
usuario.pack(pady=15, padx=15, side=TOP)

# Campo de senha
stringSenha = StringVar(value="********")
senha = Entry(frameInicial, textvariable=stringSenha, show='*')
senha.pack(pady=15, padx=15, side=TOP)

# Botão de envio
envio = Button(frameInicial, text='ENVIAR', command= lambda:
enviarFormulario(usuario.get(),senha.get()))
envio.pack(pady=15, padx=15, side=TOP)
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
    'Escritório',
    'Arte',
    'Informática',
    'Papel',
    'Escolar',
    'Mochila',
    'Presente',
    'Cadernos',
    'Jogos',
    'Embalagens',
    'Brinquedo'
]

# Menu com as categorias dos produtos
stringFuncao = StringVar(value='Categoria')
funcao = OptionMenu(frameProduto, stringFuncao, *funcoesList)
funcao.pack(pady=0, side=TOP)

# Botão de confirmação
confirmarButton = Button(frameProduto, text='CONFIRMAR', command= lambda:
cadastraProduto())
confirmarButton.pack(pady=15, side=TOP)

# Botão para voltar ao menu principal
voltarButton = Button(frameProduto, text='VOLTAR', command= lambda:
raise_frame(framePrincipal))
voltarButton.pack(pady=15, side=TOP)
# Fim do frame de cadastro de produtos #

# Frame de consulta de produtos #
# Título do campo de busca
nomeString = StringVar(value='Digite o código do produto:')
nomeLabel = Label(frameConsulta, textvariable=nomeString)
nomeLabel.pack(pady=1, padx=15, side=TOP)

# Campo de código do produto para busca
stringProduto = StringVar()
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

# Label com o preço do produto
brindeString = StringVar()
brindeLabel = Label(frameConsulta, textvariable=brindeString)
brindeLabel.pack(pady=1, padx=15, side=TOP)

# Botão de envio
enviarButton = Button(frameConsulta, text='ENVIAR', command= lambda:
retornaInfo(stringProduto.get(), nomeString, codigoString, categoriaString, precoString))
enviarButton.pack(pady=14, padx=15, side=TOP)

# Botão para voltar ao menu principal
voltarButton = Button(frameConsulta, text='VOLTAR', command= lambda:
raise_frame(framePrincipal))
voltarButton.pack(pady=0, padx=15, side=TOP)
# Fim do frame de consulta de produtos #

# Definição do primeiro frame a ser apresentado
raise_frame(frameInicial)

# Laço infinito da janela principal
janelaPrincipal.mainloop()
