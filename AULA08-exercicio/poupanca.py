from contaBancaria import contaBancaria


class contaPoupanca(contaBancaria):
    # Classe concreta que representa uma conta poupança

    def __init__(self, titular, saldo, rendimento):
        # Construtor da classe concreta
        super().__init__(titular, saldo)  # Chama o construtor da superclasse
        self.rendimento = rendimento  # Rendimento mensal da conta poupança em porcentagem

    def cadastrar(self):
        # Método concreto que implementa o método abstrato da superclasse
        print(
            f"Cadastrando a conta poupança de {self.titular} com saldo de {self.saldo} e rendimento de {self.rendimento}%")

    def depositar(self, valor):
        # Método concreto que implementa o método abstrato da superclasse
        if valor > 0:  # Verifica se o valor é positivo
            self.saldo += valor  # Atualiza o saldo da conta
            print(
                f"Depositando {valor} na conta poupança de {self.titular}. Saldo atual: {self.saldo}")
        else:
            print("Valor inválido para depósito")
