from ClienteTatu import Cliente
from ContaTatu import Conta
from ContaEspecial import ContaEspecial

joao= Cliente("Joao da silva","40028922")
maria = Cliente("Maria da Silva","91206391")



conta1 = Conta([joao],1,100)
conta2 = ContaEspecial([joao,maria],2,500)
conta1.saque(50)
conta1.saque(190)
conta2.saque(200)
conta1.extrato()
conta2.extrato()
conta2.saque(100)
conta2.extrato()
