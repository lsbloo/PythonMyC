# Herança e Polimorfismo


class Mamifero(object):
    def __init__(self,cor_de_pelo,genero,andar):
        self.cor=cor_de_pelo
        self.genero=genero
        self.andar=andar

    def falar(self):
        print("Olá sou um mamifero!")


class Pessoa(Mamifero):
    def __init__(self,cor_de_pelo,genero,andar,cor_cabelo):

        #Refere-se a super classe e "pega os atributos do pai"
        # evitando o polimorfismo de objetos
        #SUPER
        super(Pessoa,self).__init__(cor_de_pelo,genero,andar)
        self.cabelo=cor_cabelo


    def falar(self):
        super(Pessoa,self).falar()
        #print("sou uma pessoa e sei falar!")




osvaldo = Pessoa("preto","m","sim","preto")
print(osvaldo.andar)
        
