from abc import ABC, abstractmethod


class contaBancaria(ABC):
    # Classe abstrata que representa uma conta bancária

    def __init__(self, titular, saldo):
        # Construtor da classe abstrata
        self.titular = titular  # Nome do titular da conta
        self.saldo = saldo  # Saldo da conta em reais

    @abstractmethod
    def cadastrar(self):
        # Método abstrato que deve ser implementado pelas subclasses
        pass

    @abstractmethod
    def depositar(self, valor):
        # Método abstrato que deve ser implementado pelas subclasses
        pass
