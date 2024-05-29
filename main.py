from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from conexao_bd import connect

class Gerenciador (ScreenManager):
    pass

class Login_Estudantes(Screen):
    pass

class Tela_Estudantes(Screen):
    pass

class Login_Inicial(Screen):
    pass

class Login_Pais(Screen):
    pass

class Tela_Pais (Screen):
    pass

class Login_Funcionarios(Screen):
    pass

class Tela_Funcionarios(Screen):
    pass

class LoginInicial(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file('main.kv')
    
    def verificar_login_funcionarios(self):
        from conexao_bd import connect
        mydb = connect()

        user = self.root.get_screen('login_funcionarios').ids.user.text
        password = self.root.get_screen('login_funcionarios').ids.password.text
        
        mycursor = mydb.cursor()
        sql = 'SELECT nome FROM porteiro WHERE email = %s AND senha = %s;'
        val = (user, password)
        mycursor.execute(sql, val)
        v = mycursor.fetchone()
        mydb.commit()
        mydb.close()

        if (v==None):
            self.root.get_screen('login_funcionarios').ids.text_color.text = "Credenciais incorretas"
            self.root.get_screen('login_funcionarios').ids.text_color.text_color = (1,0,0,1)

        else:
            v = v[0]
            self.root.current = 'tela_funcionarios'
            mydb = connect()


    def verificar_login_pais(self):
        from conexao_bd import connect
        mydb = connect()

        user = self.root.get_screen('login_pais').ids.user.text
        password = self.root.get_screen('login_pais').ids.password.text

        mycursor = mydb.cursor()
        sql = 'SELECT id_responsavel FROM responsavel WHERE email = %s AND senha = %s;'
        val = (user, password)
        
        mycursor.execute(sql, val)
        v = mycursor.fetchone()
        mydb.commit()
        mydb.close()

        if (v==None):
            self.root.get_screen('login_pais').ids.text.text = "Credenciais incorretas"
            self.root.get_screen('login_pais').ids.text.text_color = (1,0,0,1)

        else:
            v = v[0]
            self.root.current = 'Tela_Pais'
            mydb = connect()

            mycursor = mydb.cursor()
            sql = 'SELECT nome FROM aluno WHERE responsavel_id = %s'
            val = (v,)
            mycursor.execute(sql, val)
            nome = mycursor.fetchone()[0]
            str(nome)
            sql = 'SELECT turma FROM aluno WHERE responsavel_id = %s'
            val = (v,)
            mycursor.execute(sql,val)
            serie = mycursor.fetchone()[0]
            str(serie)
            sql = 'SELECT stts FROM aluno WHERE responsavel_id = %s'
            val = (v,)
            mycursor.execute(sql, val)
            stts = mycursor.fetchone()[0]
            int(stts)
            if (stts==1):
                stts = 'Presente'
                self.root.get_screen('Tela_Pais').ids.status_aluno_pais.text = stts
                self.root.get_screen('Tela_Pais').ids.status_aluno_pais.text_color = (0,1,0,1)
                
            else:
                stts = 'Ausente'
                self.root.get_screen('Tela_Pais').ids.status_aluno_pais.text = stts
                self.root.get_screen('Tela_Pais').ids.status_aluno_pais.text_color = (1,0,0,1)
                
            self.root.get_screen('Tela_Pais').ids.nome_aluno_pais.text = nome
            self.root.get_screen('Tela_Pais').ids.serie_aluno_pais.text = serie
    
    def verificar_login_estudantes(self):
        from conexao_bd import connect
        mydb = connect()

        user = self.root.get_screen('login_estudantes').ids.user.text
        password = self.root.get_screen('login_estudantes').ids.password.text

        mycursor = mydb.cursor()
        sql = 'SELECT matricula FROM aluno WHERE email = %s AND senha = %s;'
        val = (user, password)
        mycursor.execute(sql, val)
        v = mycursor.fetchone()
        mydb.commit()
        mydb.close()

        if (v==None):
            self.root.get_screen('login_estudantes').ids.text.text = "Credenciais incorretas"
            self.root.get_screen('login_estudantes').ids.text.text_color = (1,0,0,1)

        else:
            v = v[0]
            self.root.current = 'Tela_Estudantes'
            mydb = connect()

            mycursor = mydb.cursor()
            sql = 'SELECT nome FROM aluno WHERE matricula = %s'
            val = (v,)
            mycursor.execute(sql, val)
            nome = mycursor.fetchone()[0]
            str(nome)
            sql = 'SELECT turma FROM aluno WHERE matricula = %s'
            val = (v,)
            mycursor.execute(sql,val)
            serie = mycursor.fetchone()[0]
            str(serie)
            sql = 'SELECT stts FROM aluno WHERE matricula = %s'
            val = (v,)
            mycursor.execute(sql, val)
            stts = mycursor.fetchone()[0]
            int(stts)
            if (stts==1):
                stts = 'Presente'
                self.root.get_screen('Tela_Estudantes').ids.status_aluno.text = stts
                self.root.get_screen('Tela_Estudantes').ids.status_aluno.text_color = (0,1,0,1)
                
            else:
                stts = 'Ausente'
                self.root.get_screen('Tela_Estudantes').ids.status_aluno.text = stts
                self.root.get_screen('Tela_Estudantes').ids.status_aluno.text_color = (1,0,0,1)
                
            self.root.get_screen('Tela_Estudantes').ids.nome_aluno.text = nome
            self.root.get_screen('Tela_Estudantes').ids.serie_aluno.text = serie

    def gerarqr(self):
        pass


LoginInicial().run()