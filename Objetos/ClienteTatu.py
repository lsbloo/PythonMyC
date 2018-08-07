## Banco Tatu -- Classe Clientes


class Cliente(object):
    def __init__(self,nome,telefone):
        self.nome=nome
        self.telefone=telefone

    def showNames(self):
        print("Nome cliente: ",self.nome)
