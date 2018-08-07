# Selection Sort()


def SelectionSort(vetor):
    i = 1
    minimo =0
    for i in range(len(vetor)-1):
        minimo = i

        for j in range(len(vetor)):
            if vetor[j]<vetor[minimo]:
                minimo = j
                

        temp=vetor[minimo]
        vetor[minimo]=vetor[i]
        vetor[i]=temp
        #vetor[i]=vetor[minimo]

    return print(vetor)

vetor = [10,30,5,4,100,80,70,6]
SelectionSort(vetor)
