# Classe com tipo especial de produto para uso de herança 
from Product import Product

class Eletronic(Product):
    def __init__(self, barCode, price, name, type, voltage):
        super(Eletronic, self).__init__(self, barCode, price, name, type)
        self.voltage = voltage
