from Conta import Conta

c1 = Conta()
c1.__saldo = -30
#print( "Saldo: ", str( c1.__saldo ) )
c1.imprimir()

#c1.setSaldo( 450 )
c1.saldo = 1100

#c1.imprimir()
#print("Novo Saldo: ", str( c1.getSaldo() ) )
print("Novo Saldo: ", str( c1.saldo ) )
c1.sacar( 1098 )
c1.imprimir()
c1.depositar(10)
c1.imprimir()