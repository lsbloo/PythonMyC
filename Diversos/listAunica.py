
class ListaUnica():
    def __init__(self,elem_class):
        self.lista=[]
        self.elem_class = elem_class
    def __len__(self):
        return len(self.lista)
    def __iter__(self):
        return iter(self.lista)
    def __getitem(self,p):
        return self.lista[p]
    def indiceValido(self,i):
        return i>=0 and i< len(self.lista)
    def adiciona(self,elemento):
        if self.pesquisa(elemento)== -1:
            self.lista.append(elemento)

    def remove(self,elemento):
        self.lista.remove(elemento)
    def pesquisa(self,elemento):
        self.verifica_TIPO(elemento)
        try:
            return self.lista.index(elemento)
        except ValueError:
            return -1

    def verifica_TIPO(self,elemento):
        if type(elemento)!=self.elem_class:
            raise TypeError("TIpo invalido!")
    def ordena(self,chave=None):
        self.lista.sort(key=chave)
