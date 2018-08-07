### MINIMO ELEMENTO DE VETOR
def Minimo(vetor):
    minimo = vetor[0]
    for i in range(len(vetor)):
        if minimo > vetor[i]:
            minimo = vetor[i]
    return print(minimo)
vetor = []
for i in range(5):
    n = int(input())
    vetor.append(n)

Minimo(vetor)
