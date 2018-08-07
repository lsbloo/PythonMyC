#Criando connect banck

import sqlite3

dados =[ ("Joao","1821982"),("Maria",'12121'),('JOSE','12121')]
#Conecta ao banco de dados!
conexao = sqlite3.connect("agenda.db")

#Cria um objeto do tipo cursor que executa querrys
cursor = conexao.cursor()

#cursor.execute(''' create table agenda ( nome text , telefone text ) ''')
#cursor.execute(''' insert into agenda (nome,telefone) values(?,?) ''',("Osvaldo","40028922"))
#Querys sendo criadas
cursor.executemany(''' insert into agenda (nome,telefone) values(?,?) ''', dados)
cursor.execute(''' select * from agenda ''')

#Retorna uma tupla com a quantidade valores das tabela
resultado = cursor.fetchall()

for registro in resultado:
    print("Nome %s\n Telefone: %s " %(registro))

#Atualiza a conexao
conexao.commit()
#Fecha o cursor
cursor.close()
#Fecha a conexao
conexao.close()
