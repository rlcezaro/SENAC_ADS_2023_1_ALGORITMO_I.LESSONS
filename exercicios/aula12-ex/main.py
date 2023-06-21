# arquivo main.py
from apartamento import Apartamento
from torre import Torre
from fila_de_espera import FilaDeEspera

# crie uma instância da fila de espera
fila = FilaDeEspera()

# crie algumas instâncias de apartamentos e torres
ap1 = Apartamento(1, 101, Torre(1, "A", "Rua 1"), 0)
ap2 = Apartamento(2, 102, Torre(1, "A", "Rua 1"), 0)
ap3 = Apartamento(3, 201, Torre(2, "B", "Rua 2"), 0)
ap4 = Apartamento(4, 202, Torre(2, "B", "Rua 2"), 0)

# cadastre os apartamentos e as torres
ap1.cadastrar()
print("------------------------------------------------")
ap2.cadastrar()
print("------------------------------------------------")
ap3.cadastrar()
print("------------------------------------------------")
ap4.cadastrar()
print("------------------------------------------------")

# adicione os apartamentos na fila de espera
fila.adicionar_apartamento(ap1)
fila.adicionar_apartamento(ap2)
fila.adicionar_apartamento(ap3)
fila.adicionar_apartamento(ap4)

# imprima a fila de espera
fila.imprimir_fila()
print("------------------------------------------------")

# retire um apartamento da fila e informe o número de vaga que ele recebeu
apartamento = fila.retirar_apartamento()
apartamento = fila.retirar_apartamento()
apartamento = fila.retirar_apartamento()
if apartamento:
    apartamento.vaga = 1  # suponha que a primeira vaga disponível seja a número 1
    print(f"O apartamento {apartamento.id} recebeu a vaga {apartamento.vaga}")
    print("------------------------------------------------")
else:
    print("A fila está vazia")
    print("------------------------------------------------")

# imprima a fila de espera novamente
fila.imprimir_fila()
