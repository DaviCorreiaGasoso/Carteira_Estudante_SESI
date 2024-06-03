from flask import Flask, request, jsonify
from conexao_bd import connect

main_teste_stress = Flask(__name__)

@main_teste_stress.route('/login_funcionarios', methods=['POST'])
def login_funcionarios():
    data = request.get_json()
    user = data.get('user')
    password = data.get('password')

    mydb = connect()
    mycursor = mydb.cursor()
    sql = 'SELECT nome FROM porteiro WHERE email = %s AND senha = %s;'
    val = (user, password)
    mycursor.execute(sql, val)
    v = mycursor.fetchone()
    mydb.commit()
    mydb.close()

    if v is None:
        return jsonify({"message": "Credenciais incorretas"}), 401
    else:
        return jsonify({"message": "Login bem-sucedido", "nome": v[0]}), 200

@main_teste_stress.route('/login_pais', methods=['POST'])
def login_pais():
    data = request.get_json()
    user = data.get('user')
    password = data.get('password')

    mydb = connect()
    mycursor = mydb.cursor()
    sql = 'SELECT id_responsavel FROM responsavel WHERE email = %s AND senha = %s;'
    val = (user, password)
    mycursor.execute(sql, val)
    v = mycursor.fetchone()
    mydb.commit()
    mydb.close()

    if v is None:
        return jsonify({"message": "Credenciais incorretas"}), 401
    else:
        v = v[0]
        mydb = connect()
        mycursor = mydb.cursor()
        sql = 'SELECT nome, turma, stts FROM aluno WHERE responsavel_id = %s'
        val = (v,)
        mycursor.execute(sql, val)
        aluno_info = mycursor.fetchone()
        nome, turma, stts = aluno_info
        status = 'Presente' if stts == 1 else 'Ausente'
        mydb.close()

        return jsonify({"nome": nome, "turma": turma, "status": status}), 200

@main_teste_stress.route('/login_estudantes', methods=['POST'])
def login_estudantes():
    data = request.get_json()
    user = data.get('user')
    password = data.get('password')

    mydb = connect()
    mycursor = mydb.cursor()
    sql = 'SELECT matricula FROM aluno WHERE email = %s AND senha = %s;'
    val = (user, password)
    mycursor.execute(sql, val)
    v = mycursor.fetchone()
    mydb.commit()
    mydb.close()

    if v is None:
        return jsonify({"message": "Credenciais incorretas"}), 401
    else:
        v = v[0]
        mydb = connect()
        mycursor = mydb.cursor()
        sql = 'SELECT nome, turma, stts FROM aluno WHERE matricula = %s'
        val = (v,)
        mycursor.execute(sql, val)
        aluno_info = mycursor.fetchone()
        nome, turma, stts = aluno_info
        status = 'Presente' if stts == 1 else 'Ausente'
        mydb.close()

        return jsonify({"nome": nome, "turma": turma, "status": status}), 200

if __name__ == '__main__':
    main_teste_stress.run(debug=False)