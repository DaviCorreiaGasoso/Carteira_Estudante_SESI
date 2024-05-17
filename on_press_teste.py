from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window



class TestApp(MDApp):
    def build(self):
        return Builder.load_file('on_press_teste.kv')

TestApp().run()