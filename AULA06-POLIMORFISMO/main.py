from cidade import Cidade
from pessoa import Pessoa
from fisica import Fisica
from juridica import Juridica

c1 = Cidade(1, "Porto Alegre")
c2 = Cidade(2, "Capão da Canoa")
c3 = Cidade(3, "Canoas")

p1 = Pessoa("Maria", "98764321", c1)
pf1 = Fisica("Joao", "123456", c2, "000.222")

# p1.imprimir()
pf1.imprimir()

print(p1)
print("------------------------------------------------")
print(pf1)
