from abc import ABC, abstractclassmethod


class ctaBancaria(ABC):
    def __init__(self, agencia=1111, nome="Centro", saldo=0.00):
        self.agencia = agencia
        self.nome = nome
        self.saldo = saldo

    def imprimir(self):
        print("Agencia: "+str(self.agencia))
        print("Nome: "+str(self.nome))
        print("Saldo: "+str(self.saldo))

    @abstractclassmethod
    def imprimirEspecifico(self):
        pass
