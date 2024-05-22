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
    
    def verificar_login_f(self):
        from conexao_bd import connect
        mydb = connect()

        user = self.root.get_screen('login_funcionarios').ids.user.text
        password = self.root.get_screen('login_funcionarios').ids.password.text
        
        mycursor = mydb.cursor()
        sql = 'SELECT nome FROM aluno WHERE email = %s AND senha = %s;'
        val = (user, password)
        mycursor.execute(sql, val)
        v = mycursor.fetchone()
        mydb.commit()

        if (v==None):
            self.root.get_screen('login_funcionarios').ids.text_color.text = "Credenciais incorretas"
            self.root.get_screen('login_funcionarios').ids.text_color.text_color = (1,0,0,1)

        else:
            print ('oi, suave?')

    def verificar_login_r(self):
        from conexao_bd import connect
        mydb = connect()

        user = self.root.get_screen('login_funcionarios').ids.user.text
        password = self.root.get_screen('login_funcionarios').ids.password.text

        mycursor = mydb.cursor()
        sql = 'SELECT nome FROM responsavel WHERE email = %s AND senha = %s;'
        val = (user, password)
        mycursor.execute(sql, val)
        v = mycursor.fetchone()
        mydb.commit()

        if v is None:
            self.root.get_screen('login_pais').ids.text.text = "Credenciais incorretas"
            self.root.get_screen('login_pais').ids.text.text_color = (1,0,0,1)

        else:
            print ('oi')


LoginInicial().run()