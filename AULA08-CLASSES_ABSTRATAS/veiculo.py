from abc import ABC, abstractclassmethod


class Veiculo(ABC):
    def __init__(self, modelo=None, ano=None):
        self.modelo = modelo
        self.ano = ano

    def imprimir(self):
        print("Modelo: "+str(self.modelo))
        print("Ano: "+str(self.ano))

    @abstractclassmethod
    def imprimirEspecifico(self):
        pass
