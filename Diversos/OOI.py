### Orientação a Objetos.

class Quadrado(object):
    def __init__(self, tamanhoLado):
        self.lado=tamanhoLado
        print("construtor chamado!")

    def mudarValorLado(self,x):
        self.lado=x
        print("valor do lado alterado: ",self.lado)
    def retornarValorLado(self):
        return self.lado
    def calcularArea(self):
        return self.lado*self.lado


quadrado= Quadrado(100)

quadrado.mudarValorLado(10)
print("valor retornado:",quadrado.retornarValorLado())
print("Área: ",quadrado.calcularArea())

print()
print()

class Televisao(object):
    def __init__(self,ligada,canal,marca,tamanho, canalMinino = 2,canalMaximo=14):
        self.ligada=ligada
        self.canal =canla
        self.marca = marca
        self.tamanho=tamanho
        self.cmin=canalMinino
        self.cmax=canalMaximo

    def imprime(self):
        print("Televisao está %s no canal %d, sua marca é %s e tem tamanho de %d"%(self.ligada,self.canal,self.marca,self.tamanho))

    def muda_canal_cima(self):
        if(self.canal+1<=self.cmax):
            self.canal+=1
        if(self.canal>=self.cmax):
            self.canal = self.cmin
    def muda_canal_baixo(self):
        if(self.canal-1>=self.cmin):
            self.canal-=1
        if(self.canal<=self.cmax):
            self.canal = self.cmax
    


tv1 = Televisao("OK",2,"Samsung",40,2,10)

for x in range(2,10):
    tv1.muda_canal_cima()
print(tv1.canal)
for x in range(2,10):
    tv1.muda_canal_baixo()
print(tv1.canal)

