from veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, modelo=None, ano=None, qtdPortas=4):
        super().__init__(modelo, ano)
        self.qtdPortas = qtdPortas

    def imprimirEspecifico(self):
        super().imprimir()
        print("Portas: "+str(self.qtdPortas))
