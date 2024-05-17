from kivymd.app import App 

from conexao_bd import connect

mydb = connect()

def insert_responsavel(mydb, nome, telefone, email, senha):
    mycursor = mydb.cursor()
    sql = "INSERT INTO responsavel (nome, telefone, email, senha) VALUES (%s, %s, %s, %s)"
    val = (nome, telefone, email, senha)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
    
def insert_aluno(mydb, nome, idade, responsavel_id, email, senha):
    mycursor = mydb.cursor()
    sql = "INSERT INTO aluno (nome, idade, responsavel_id, email, senha) VALUES (%s, %s, %s, %s, %s)"
    val = (nome, idade, responsavel_id, email, senha)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
    
def insert_porteiro(mydb, nome, email, senha):
    mycursor = mydb.cursor()
    sql = "INSERT INTO porteiro (nome, email, senha) VALUES (%s, %s, %s)"
    val = (nome, email, senha)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()

def insert_supervisao(mydb, email, senha):
    mycursor = mydb.cursor()
    sql = "INSERT INTO supervisao (email, senha) VALUES (%s, %s)"
    val = (email, senha)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
    
def delete_responsavel(mydb, id):
    mycursor = mydb.cursor()
    sql = "DELETE FROM responsavel WHERE id_responsavel=%s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
        
def delete_aluno(mydb, id):
    mycursor = mydb.cursor()
    sql = "DELETE FROM aluno WHERE id_aluno=%s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
    
def delete_porteiro(mydb, id):
    mycursor = mydb.cursor()
    sql = "DELETE FROM porteiro WHERE id_porteiro=%s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()

