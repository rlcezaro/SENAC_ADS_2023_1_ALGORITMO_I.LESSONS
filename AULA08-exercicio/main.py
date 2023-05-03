from poupanca import contaPoupanca
from corrente import contaCorrente

# Criando objetos das classes concretas
# Conta corrente de João com saldo de 1000 e limite de 500
c1 = contaCorrente("João", 1000, 500)
# Conta poupança de Maria com saldo de 2000 e rendimento de 0.5%
c2 = contaPoupanca("Maria", 2000, 0.5)

# Chamando os métodos cadastrar e depositar
c1.cadastrar()  # Cadastra a conta corrente de João
c1.depositar(200)  # Deposita 200 na conta corrente de João
c2.cadastrar()  # Cadastra a conta poupança de Maria
c2.depositar(300)  # Deposita 300 na conta poupança de Maria
