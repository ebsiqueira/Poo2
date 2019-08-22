class Imovel:
    def __init__(self, endereco, preco):
        self.__endereco = endereco
        self.__preco = preco
    
class Novo(Imovel):
    def __init__(self, endereco, preco, adicional):
        self.__endereco = endereco
        self.__preco = preco
        self.adicional = adicional

    def printPreco(self):
        print(self.__preco)

    def getAdicional(self):
        return self.__adicional

class Velho(Imovel):
    def __init__(self, endereco, preco):
        self.__endereco = endereco
        self.__preco = (preco * 0.85)
        self.adicional = adicional

    def printPreco(self):
        print(self.__preco)

    def getAdicional(self, preco):
        self.__preco = (preco * 0.85)
