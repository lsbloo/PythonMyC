#
import sqlite3
from matplotlib import pyplot as plt
import random
import time
import os
import re


regra_N = 3
medias=[]
nome_alunos=[]
def pegarN():
    
    n = int(input("Digite o numero de alunos: "))
    for i in range(n):
        name=str(input("Digite o nome do aluno %d: "%i))
        notas = str(input("Digite as notas p1,p2,p3: ")).split()
        
        media = (float(notas[0])+float(notas[1])+float(notas[2])) / regra_N
        nome_alunos.append(name)
        medias.append(media)


    print("!OK")
    print();

def createDatabase():
    
    conexao = sqlite3.connect("cad.db")
    cursor = conexao.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS notas ( medias text, nome text) ''')

    conexao.commit()
   
    print("Create Database... sucess!")
        

def request_datas_inf():
        request_me=[]
        request_na=[]
        data_request=[]
        x=[]
        y=[]
        #Vetores auxiliares para o tratamento dos dados vindo do db

        ###################################
        conexao = sqlite3.connect("cad.db")
        cursor = conexao.cursor()
        regex_f = re.compile(r'[+-]?([0-9]*[.])?[0-9]+')
        cursor.execute(''' select * from notas ''' )
        result_ok = cursor.fetchall()
        for register in result_ok:
            data_request.append(register)
            #print("M",data_request)
        w = len(data_request)
        for k in range(w):
            x.append(data_request[k][1])
            y.append(data_request[k][0])
            
        for cd in x:

            if regex_f.match(cd):
                request_me.append(cd)
               
            else:
                request_na.append(cd)

        for cw in y:
            if regex_f.match(cw):
                request_me.append(cw)
            else:
                request_na.append(cw)
                
        

        return request_me,request_na
                

         
    

def insertMedias(medias,nome_alunos):
    try:
        conexao = sqlite3.connect("cad.db")
        conexao.row_factory = sqlite3.Row
        cursor = conexao.cursor()
        data = []
        for x,y in medias,nome_alunos:
            data.append((x,y))
        
        
        
        cursor.executemany(''' insert into notas ( medias, nome ) values(?,?) ''',data)
    except ValueError:
        print("Error Insert, minimo dois alunos!")
    finally:
        conexao.commit()
    

def createGrafico(medias,nome_alunos):
    medias.sort()
    plt.plot(nome_alunos,medias, color='blue', marker='o',linestyle='solid')
    plt.title("Grafico de Medias dos alunos!")
    plt.ylabel("Médias não ordenadas")
    plt.show();
    
    

def menu():
    print("Utilize numeros inteiros para insercão das notas, é mais facil de entender o grafico!")
    print(" digite as 3 notas em sequencia exemplo 10 9 8 ")
    print("Minino de alunos que voce pode inserir são 2 ")
    print("Digite [s], se deseja somente visualizar o grafico!")    
    print("Digite: [X] se quiser deletar os dados ou [0] para continuar")
    print()
    ver1 = str(input("Visualizar grafico? ")).upper()
    if ver1 == 'S':
        x=[]
        y=[]
        x,y=request_datas_inf()
        createGrafico(x,y)
    else:
        pass;
    ver = str(input("Deletar: ? ")).upper()
    if ver == 'X':
        delete_register()
    else:
        pass;

def update_conf():
    cont =20
    i=0
    print()
    print("Carregando...!")
    while i < cont:
        time.sleep(0.1)
        print("#",end="")
        i+=1
    print()
    #createDatabase()
          
def delete_register():
    
    conexao = sqlite3.connect("cad.db")
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()

    cursor.execute(''' DROP TABLE IF EXISTS notas ''' );

    conexao.commit();
    cursor.close()
    conexao.close()
   
            
    
def main():
    x=[]
    y=[]
    createDatabase()
    update_conf()
    pegarN();    
    insertMedias(medias,nome_alunos)
    x,y=request_datas_inf()
    createGrafico(x,y)
    


menu()
main()
