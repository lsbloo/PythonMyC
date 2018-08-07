
def BuscaBinaria(A,key):
    n = len(A)
    esquerda = 0
    direita = n
    tentativa =0
    #print(hi)
    while esquerda<=direita:
        operacao =esquerda+(direita-esquerda)/2
        mid=int(operacao)
        #print(mid)
        if key <A[mid]:
            direita = mid -1
            print("hi",direita)
        else:
            if key > A[mid]:
                esquerda = mid+1
                print("lo",esquerda)
    
            else:
                return print("Índice",mid,"Tentativas",tentativa)
        tentativa+=1
    return print(-1)


vetor = [1,2,3,4,5,6,7,8,9,10]
chave = 5
BuscaBinaria(vetor,chave)
