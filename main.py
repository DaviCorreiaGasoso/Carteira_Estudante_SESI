from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp

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

class LoginApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file('main.kv')

    def verificar_login(self):
        user = self.root.get_screen('login').ids.user.text
        password = self.root.get_screen('login').ids.password.text
        if user == "admin" and password == "admin":
            print("Login bem-sucedido!")
        else:
            print("Usuário ou senha incorretos!")

if __name__ == "__main__":
    LoginApp().run()