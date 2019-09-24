from Product import Product
from Functionary import Functionary

class Supermarket:
    def __init__(self):
        self.productList =[]
        self.functionaryList = [Functionary('Eduardo', '123')]

    def consulteProduct(self,barCode):
        for product in self.productList:
            if(product.barCode == barCode):
                print('achei porra')
                return product

    def registerProduct(self,barCode, price, name, type):
        product = Product(barCode, price, name, type)
        self.productList.append(product)

    def tryLogin(self,username, password):
         for functionary in self.functionaryList:
             if(functionary.name == username and functionary.password == password):
                 return True
         return False
