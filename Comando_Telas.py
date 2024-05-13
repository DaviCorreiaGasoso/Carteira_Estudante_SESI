from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.image import AsyncImage

Window.size = (900,500)

class Login_Responsavel(App):
    def build(self):
        Window.clearcolor=(1, 1, 1, 0)
        
        layout_principal = FloatLayout()

        label_login = Label(
            text="Login", 
            size_hint=(.2, .1),
            pos=(195, 350),
            font_size= 40,
            color = [1,1,1,1],
            halign = ('center')
        )
        with label_login.canvas.before:
            Color (0.2, 0.5, 0.7, 1),
            Rectangle (
            pos=(200,350),
            size=(200, 60)
            )

        layout_principal.add_widget(label_login)

        self.input_login = TextInput(
            multiline= False,
            size_hint=(.4, .1),
            pos=(400, 350),
            hint_text='Digite o seu email aqui...',
            padding_y=(20)
            )
        
        layout_principal.add_widget(self.input_login)
        
        label_senha = Label(
            text="Senha", 
            size_hint=(.2, .1),
            pos=(195, 250),
            font_size= 40,
            color = [1,1,1,1],
            halign = ('center')
        )
        with label_senha.canvas.before:
            Color (0.2, 0.5, 0.7, 1),
            Rectangle (
            pos=(200,250),
            size=(200, 60)
            )
        
        layout_principal.add_widget(label_senha)

        input_senha = TextInput(
            multiline= False,
            size_hint=(.4, .1),
            pos=(400, 250),
            hint_text='Digite o sua senha aqui...',
            padding_y=(20)
        )

        layout_principal.add_widget(input_senha)

        return layout_principal

Login_Responsavel().run()