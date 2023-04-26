from Pessoa import Pessoa
class Fisica(Pessoa):

    def __init__(self, nome, fone, cidade, cpf):
        super().__init__(nome, fone, cidade)
        self.cpf = cpf
        self.empresa = None

    def setEmpresa(self, empresa):
        self.empresa = empresa

    def imprimir(self):
        super().imprimir()
        print("CPF: ", self.cpf)
        
    def __str__(self):
        return super().__str__() + "\nCPF: " + self.cpf