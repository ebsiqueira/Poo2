class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def eibirDados(self):
        print(self.nome)
        print(self.salario)

class Gerente:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def eibirDados(self):
        print(self.nome)
        print(self.salario)

class Assistente(Funcionario):
    def __init__(self, nome, salario, matricula):
        self.nome = nome
        self.salario = salario
        self.__matricula = matricula

    def getMatricula(self):
        return self.__matricula

    def eibirDados(self):
        print(self.nome)
        print(self.salario)
        print(self.__matricula)

class AssistenteTecnico(Assistente):
    def __init__(self, nome, salario, bonus, matricula):
        self.nome = nome
        self.salario = salario
        self.bonus = bonus
        self.__matricula = matricula
    
    def getMatricula(self):
        return self.__matricula

    def eibirDados(self):
        print(self.nome)
        print(self.salario)
        print(self.bonus)
        print(self.__matricula)

class AssistenteAdministrativo(Assistente):
    def __init__(self, nome, salario, turno, matricula):
        self.nome = nome
        self.salario = salario
        self.turno = turno
        self.__matricula = matricula

    def getMatricula(self):
        return self.__matricula
    
    def eibirDados(self):
        print(self.nome)
        print(self.salario)
        print(self.turno)
        print(self.__matricula)