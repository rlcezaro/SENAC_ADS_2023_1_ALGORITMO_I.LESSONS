from cidade import Cidade
from pessoa import Pessoa
from fisica import Fisica
from juridica import Juridica

c1 = Cidade(1, "Porto Alegre")
c2 = Cidade(2, "Capão da Canoa")
c3 = Cidade(3, "Canoas")

joao = Fisica("João", "223-4455", c1, "000.111.222-33")
maria = Fisica("Maria", "3344-5566", c2, "111.222.333-44")
jose = Fisica("Jose", "3344-5566", c2, "222.333.444-55")

dosul = Juridica("Supermercado do Sul", "234-4321", c1, "01.234.567/0001-00")


# pf.nome = "Joao"
dosul.imprimir()
dosul.addFuncionarios(joao)
dosul.addFuncionarios(maria)

print("----------------\n\n")
dosul.imprimir()
