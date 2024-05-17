from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.core.window import Window

Window.clearcolor = [1,1,1,1]

class tela_responsavel(MDApp):
    def build(self):

        return Builder.load_file('tela_2.kv')
    
tela_responsavel().run()
