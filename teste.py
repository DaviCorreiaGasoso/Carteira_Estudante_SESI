from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from conexao_bd import connect

class MinhaApp(MDApp):
    def build (self):
        return Builder.load_file('tela_teste.kv')
    
if __name__ == '__main__':
    MinhaApp().run()