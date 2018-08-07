#### Busca Sequencial


def BuscaSequencial(vetor , chave):

    for i in range(len(vetor)):
        if vetor[i] == chave:
            return print(i)

    return print(-1)


vetor = []

for i in range(5):
    n = int(input())
    vetor.append(n)


key = int(input("key: "))

BuscaSequencial(vetor,key)
