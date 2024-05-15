from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen


class MinhaApp(MDApp):
    def build(self):
        return Builder.load_file('kv_tela-inicial.kv')

if __name__ == "__main__":
    MinhaApp().run()