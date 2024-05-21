from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen


class LoginScreen(Screen):
    pass

class LoginApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        
        return Builder.load_file('main2.kv')

    def verificar_login(self):
        from conexao_bd import connect
        mydb = connect()

        user = self.root.get_screen('login').ids.user.text
        password = self.root.get_screen('login').ids.password.text
        
        mycursor = mydb.cursor()
        sql = "SELECT nome FROM aluno WHERE email = %s AND senha = %s;"
        val = (user, password)
        mycursor.execute(sql,val)
        v = mycursor.fetchone()
        mydb.commit()
        
        if (v==None):
            print ('n funciono')

        else:
            print ('funciono guys')


if __name__ == "__main__":
    LoginApp().run()