# Classe com tipo especial de produto para uso de herança (Produto especial)
from Produto import Produto

class Brinquedo(Produto):
    def __init__(self, codigo, preco, nome, tipo, brinde):
        super().__init__(self, codigo, preco, nome, tipo)
        self.brinde = brinde
