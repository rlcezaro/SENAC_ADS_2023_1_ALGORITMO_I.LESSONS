from cidade import Cidade
from pessoa import Pessoa

from categoria import Categoria
from produto import Produto
from pedido import Pedido

poa = Cidade(1, "Porto Alegre")

p1 = Pessoa("Joao", '3344-5566', poa)
p2 = Pessoa("Maria", '2233-4455', poa)

print("---- 29/03/2023 --------")
cat1 = Categoria(1, "Bebidas")
cat2 = Categoria(2, "Alimentos")

prod1 = Produto("Coca-cola", 7.99, cat1)
prod2 = Produto("Fanta", 6.95, cat1)
prod3 = Produto("Arroz", 3.99, cat2)

ped01 = Pedido("Rua A, 100", p2)
ped01.imprimir()

print("Soma: ", ped01.addProduto(prod1))
print("Soma: ", ped01.addProduto(prod3))

print("------------------------")
ped01.imprimir()


# print("Nome da cidade da ", p2.nome, ": ", p2.cidade.nome)
# p1.imprimir()
