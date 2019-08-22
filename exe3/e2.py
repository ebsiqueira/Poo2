class Ingresso:
    def __init__(self, preco):
        self.__preco = preco

    def imprimeValor(self):
        return self.__preco

class Vip(Ingresso):
    def __init__(self, preco, adicional):
        self.__preco = preco
        self.__adicional = adicional

    def imprimeValor(self):
        return (self.__preco + self.__adicional)

    def imprimeAdicional(self):
        return self.__adicional

class Normal(Ingresso):
    def __init__(self, preco):
        self.__preco = preco

    def imprimeValor(self):
        return self.__preco

    def tipoIngresso():
        print('Ingresso Normal')

class CamaroteInferior(Vip):
    def __init__(self, preco, localizacao):
        self.__preco = preco
        self.__localizacao = localizacao

    def setLocalizacao(self, localizacao):
        self.__localizacao = localizacao

    def getLocalizacao(self):
        return self.__localizacao

class CamaroteSuperior(Vip):
    def __init__(self, preco, localizacao, adicional):
        self.__preco = preco
        self.__adicional = adicional
        self.__localizacao = localizacao

    def setLocalizacao(self, localizacao):
        self.__localizacao = localizacao

    def getLocalizacao(self):
        return self.__localizacao

    def imprimeValor(self):
        return (self.__preco + self.__adicional)