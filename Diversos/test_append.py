

def append(vetor,numeroADD):
    index = len(vetor)+1
    
    try:
        TAMANHO_VETOR = len(vetor)
        for i in range(TAMANHO_VETOR):
            if vetor[i+1] == None:
                print("x!")
    except IndexError:
        vetor_new = [0]*index
        for i in range(index-1):
            vetor_new[i]=vetor[i]
        vetor_new[index-1]=numeroADD
        print("ADD:",vetor_new)
    
    
def remove(vetor,valorElemento):
    vetor_aux=[]
    for i in vetor:
        if i != valorElemento:
            vetor_aux.append(i)
    print("Remove: ",vetor_aux)
    

lista=[1,2,3,4,5,6,7,8,9]
append(lista,10)
remove(lista,8)
