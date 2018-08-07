"""
def Buscabinaria(A,key):
    #kaspaskKPASKPSK
    n = len(A)
    lo = 0
    hi = n
    while(lo <= hi):
        mid =0
        mid = int(lo+(hi-lo)/2)
        if key <A[mid]:
            hi = mid -1
        else:
            if key>A[mid]:
                lo = mid +1
            else:
                return mid

    return -1


vetor = [2,3,4,5,6,7]
key = int(input("Digite chave: "))
print(Buscabinaria(vetor,key))
"""

vetor = [3,2,1,500,8]
maior = vetor[0]
for i in range(len(vetor)):
    if vetor[i] > maior:
        maior = vetor[i]

print(maior)

menor = vetor[0]

for i in range(1,len(vetor)):
    if menor > vetor[i]:
        menor = vetor[i]
    #fimse
    #fimpara
print(menor)

    
