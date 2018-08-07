

#

def isEVEN(numero):

    if(numero>=0):
        if(numero%2==0):
            return print(True)
        else:
            return print(False)

    else:
        return isEVEN(numero = int(input()))




isEVEN(-1)
