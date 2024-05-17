from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window

Window.size = (300, 500)


# KV
KV = '''
ScreenManager:
    Screen:
        name: 'first_screen'
        MDFlatButton:
            text: "Login"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1  # Cor do texto branca
            md_bg_color: 0, 0, 0, 1  # Cor de fundo preta
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            on_release: app.root.current = 'second_screen'

    Screen:
        name: 'second_screen'
        MDFlatButton:
            text: "Voltar"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1  # Cor do texto branca
            md_bg_color: 0, 0, 0, 1  # Cor de fundo preta
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            on_release: app.root.current = 'first_screen'
'''

class TestApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

TestApp().run()