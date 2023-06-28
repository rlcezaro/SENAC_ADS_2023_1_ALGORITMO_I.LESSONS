jogadores = "João", "Maria", "José", "Júlia"
print(jogadores)
print(jogadores[1:3])
print(jogadores[1:-1])
selecionados = jogadores[2:],jogadores[0]
print(selecionados)
print("---------------------------------")
print(jogadores[2:],jogadores[0])
print(jogadores[:-2])

def calcular(x,y):
    return x+y,x-y,x*y,x/y

resultado = calcular(10,5)
print(resultado)
print("Multiplicaçao: ",resultado[2])
print("Divisão: ",resultado[3])
print("---------------------------------")
a,b,c,d = calcular (9,3)
print("Soma: ",a,"Subtração: ",b,"Multiplicação: ",c,"Divisão: ",d)