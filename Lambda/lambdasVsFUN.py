
def dict_lambdas():
    dictzin = {'soma' : lambda x,y: x+y,
               'subtracao': lambda x,y: x-y,
                'multiplicacao': lambda x,y: x*y,
                 'divisao': lambda x,y:x/y}
    return dictzin


def criaFun(dictz):
    soma_function=dictz['soma']
    sub_function=dictz['subtracao']
    multi_function=dictz['multiplicacao']
    divisao_function=dictz['divisao']

    return soma_function,sub_function,multi_function,divisao_function

def acess(list_,):
    """
    Mostra as funcoes lambdas e realiza as operacoes especificadas! !
    """
    cont=0
    x1 = int(input("value X: "))
    y1 = int(input("value Y: "))
    imp=[len(list_)]
    imp.append('soma')
    imp.append('subtracao')
    imp.append('multiplicacao')
    imp.append('divisao')
    for x in list_:
        cont+=1
        print(imp[cont],'e igual a: ',x(x1,y1))
        
dict_lambda=dict_lambdas()
list_F=[]
list_F=criaFun(dict_lambda)
if list_F != None:
    acess(list_F)

