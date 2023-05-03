from contaBancaria import contaBancaria


class contaCorrente(contaBancaria):
    # Classe concreta que representa uma conta corrente

    def __init__(self, titular, saldo, limite):
        # Construtor da classe concreta
        super().__init__(titular, saldo)  # Chama o construtor da superclasse
        self.limite = limite  # Limite de cheque especial da conta corrente

    def cadastrar(self):
        # Método concreto que implementa o método abstrato da superclasse
        print(
            f"Cadastrando a conta corrente de {self.titular} com saldo de {self.saldo} e limite de {self.limite}")

    def depositar(self, valor):
        # Método concreto que implementa o método abstrato da superclasse
        if valor > 0:  # Verifica se o valor é positivo
            self.saldo += valor  # Atualiza o saldo da conta
            print(
                f"Depositando {valor} na conta corrente de {self.titular}. Saldo atual: {self.saldo}")
        else:
            print("Valor inválido para depósito")
