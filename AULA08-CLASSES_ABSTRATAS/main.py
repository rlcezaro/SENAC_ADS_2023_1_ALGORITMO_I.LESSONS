# from veiculo import Veiculo
from carro import Carro
from moto import Moto

v = Carro("Doblo", 2006, 2)
m = Moto("Honda", 2015, 1500)
# v.imprimirEspecifico()
m.imprimir()
print("----------------------------------------------------------------")
m.imprimirEspecifico()
print("----------------------------------------------------------------")
v.imprimir()
print("----------------------------------------------------------------")
v.imprimirEspecifico()
