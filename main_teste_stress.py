from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
import requests

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
        user = self.root.get_screen('login_funcionarios').ids.user.text
        password = self.root.get_screen('login_funcionarios').ids.password.text
        
        response = requests.post('http://127.0.0.1:5000/login_funcionarios', json={'user': user, 'password': password})
        
        if response.status_code == 200:
            self.root.current = 'tela_funcionarios'
        else:
            self.root.get_screen('login_funcionarios').ids.text_color.text = "Credenciais incorretas"
            self.root.get_screen('login_funcionarios').ids.text_color.text_color = (1,0,0,1)

    def verificar_login_pais(self):
        user = self.root.get_screen('login_pais').ids.user.text
        password = self.root.get_screen('login_pais').ids.password.text
        
        response = requests.post('http://127.0.0.1:5000/login_pais', json={'user': user, 'password': password})
        
        if response.status_code == 200:
            data = response.json()
            self.root.current = 'Tela_Pais'
            self.root.get_screen('Tela_Pais').ids.nome_aluno_pais.text = data['nome']
            self.root.get_screen('Tela_Pais').ids.serie_aluno_pais.text = data['turma']
            self.root.get_screen('Tela_Pais').ids.status_aluno_pais.text = data['status']
            if data['status'] == 'Presente':
                self.root.get_screen('Tela_Pais').ids.status_aluno_pais.text_color = (0,1,0,1)
            else:
                self.root.get_screen('Tela_Pais').ids.status_aluno_pais.text_color = (1,0,0,1)
        else:
            self.root.get_screen('login_pais').ids.text.text = "Credenciais incorretas"
            self.root.get_screen('login_pais').ids.text.text_color = (1,0,0,1)

    def verificar_login_estudantes(self):
        user = self.root.get_screen('login_estudantes').ids.user.text
        password = self.root.get_screen('login_estudantes').ids.password.text
        
        response = requests.post('http://127.0.0.1:5000/login_estudantes', json={'user': user, 'password': password})
        
        if response.status_code == 200:
            data = response.json()
            self.root.current = 'Tela_Estudantes'
            self.root.get_screen('Tela_Estudantes').ids.nome_aluno.text = data['nome']
            self.root.get_screen('Tela_Estudantes').ids.serie_aluno.text = data['turma']
            self.root.get_screen('Tela_Estudantes').ids.status_aluno.text = data['status']
            if data['status'] == 'Presente':
                self.root.get_screen('Tela_Estudantes').ids.status_aluno.text_color = (0,1,0,1)
            else:
                self.root.get_screen('Tela_Estudantes').ids.status_aluno.text_color = (1,0,0,1)
        else:
            self.root.get_screen('login_estudantes').ids.text.text = "Credenciais incorretas"
            self.root.get_screen('login_estudantes').ids.text.text_color = (1,0,0,1)

LoginInicial().run()