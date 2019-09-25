# Classe para descrição do supermercado

from Product import Product
from Functionary import Functionary

class Supermarket:
    def __init__(self):
        self.productList =[]
        self.functionaryList = [Functionary('Eduardo', '123')]

    # Função responsável pela consulta de produtos
    def consulteProduct(self,barCode):
        for product in self.productList:
            if(product.barCode == barCode):
                return product

    # Função responsável pelo registro de produtos
    def registerProduct(self,barCode, price, name, type):
        product = Product(barCode, price, name, type)
        self.productList.append(product)

    # Função responsável pelo login
    def tryLogin(self,username, password):
         for functionary in self.functionaryList:
             if(functionary.name == username and functionary.password == password):
                 return True
         return False
