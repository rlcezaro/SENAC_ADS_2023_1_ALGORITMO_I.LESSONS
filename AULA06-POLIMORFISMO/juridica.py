from pessoa import Pessoa
from fisica import Fisica


class Juridica(Pessoa):
    def __init__(self, nome, fone, cidade, cnpj):
        super().__init__(nome, fone, cidade)
        self.cnpj = cnpj
        self.qtd_funcionarios = 0
        self.funcionarios = []

    def addFuncionarios(self, funcionario):
        self.funcionarios.append(funcionario)
        self.qtd_funcionarios += 1

    def imprimir(self):
        print("Empresa: ", self.nome)
        print("Fone: ", self.fone)
        print("Cidade: ", self.cidade.nome)
        # super().imprimir()
        print("Qtd Funcionarios: ", self.qtd_funcionarios)
        print("Funcionarios: \n-----------------")
        if len(self.funcionarios) > 0:
            for func in self.funcionarios:
                print("Nome func.: ", func.nome)
                print("Fone func.: ", func.fone)
                print("Cidade func.: ", func.cidade.nome)
                print("--------------------------")
