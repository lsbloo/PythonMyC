from time import *

print("Loading... ")
def barra():
    for i in range(100):
        print("#",end="")
        sleep(0.01)

    print()
    print("Carregado!",i+1,"%")
            
        


def saida():
    barra()



saida()
