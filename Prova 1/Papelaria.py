# Classe para descrição do supermercado
from Produto import Produto
from Funcionario import Funcionario

class Papelaria:
    def __init__(self):
        self.listaProdutos =[]
        # Usuario cadastrado por default
        self.listaFuncionarios = [Funcionario('root', 'toor')]

    # Função responsável pela consulta de produtos
    def consultaProduto(self,codigo):
        for produto in self.listaProdutos:
            if(produto.codigo == codigo):
                return produto
            else:
                a = 0
        return a

    # Função responsável pelo registro de produtos
    def registraProduto(self, codigo, preco, nome, tipo):
        produto = Produto(codigo, preco, nome, tipo)
        self.listaProdutos.append(produto)

    # Função responsável pelo login
    def realizaLogin(self, usuario, senha):
         for funcionario in self.listaFuncionarios:
             if(funcionario.nome == usuario and funcionario.senha == senha):
                 return True
         return False
