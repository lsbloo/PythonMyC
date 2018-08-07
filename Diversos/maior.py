
vetor = []
n = int(input())
for i in range(n):
    numero = int(input())
    vetor.append(numero)
maior = vetor[0]
menor = maior
for i in range(len(vetor)):
    if vetor[i]>maior:
        maior = vetor[i]


print(maior)
#print(menor)



########## Pesquisa Sequencial !!
"""
def Pesquisa(vetor,chave):
    for i in range(len(vetor)):
        if vetor[i] == chave:
            return print(i)

    return -1


chave = int(input("Key: "))
Pesquisa(vetor,chave)
"""
