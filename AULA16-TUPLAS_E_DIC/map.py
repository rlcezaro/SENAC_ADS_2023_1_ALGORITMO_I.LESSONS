precos = [10,20,30] # lista

def aumentarPrecos(preco):
    return preco * 1.1 # 10% de aumento

novosprecos = map(aumentarPrecos, precos) # map(função, lista)

print(novosprecos) # Imprimindo o objeto map
print(list(novosprecos)) # Imprimindo a lista de preços com aumento de 10%

valores = [(10,20),[30,40]] # Tupla de tuplas e lista, pode ser so tupla ou so lista tb
def somar(x): # Função para somar os valores da tupla
    return x[0]+x[1] # Soma dos valores da tupla

soma = map(somar, valores) # map(função, lista)
print(list(soma)) # Imprimindo a lista de somas