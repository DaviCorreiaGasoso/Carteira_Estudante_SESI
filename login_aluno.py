from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window


Window.size= (500,700)

class Tela_Login_Aluno(App):
    def build(self):
            layout_main = FloatLayout()
            self.orientation= "vertical"
            self.padding= [50, 20]
            self.spacing= 10

            Window.clearcolor=(1, 1, 1, 0)

            l_login = Label(
                text=" L O G I N   D O   A L U N O ", 
                size_hint=(.35, .36),
                pos=(200, 410),
                font_size= 25,
                color = [0,0,0.1,1],
                halign = ('center')
            )



            with l_login.canvas.before:
                Color (1, 1, 1, 1),
                Rectangle (
                pos=(200,350),
                size=(200, 100)
            )

            layout_main.add_widget(l_login)

            l_login2 = Label(
                text=" M A T R Í C U L A  O U  C P F: ", 
                size_hint=(.35, .37),
                pos=(60, 320),
                font_size= 17,
                color = [0,0,0,1],
                halign = ('center')
            )

            layout_main.add_widget(l_login2)

            self.input = TextInput(
                multiline= False,
                size_hint=(.50, .1),
                pos=(300, 430),
                hint_text='Digite a matrícula ou o CPF aqui...',
                padding_y=(30)
            )
        
            layout_main.add_widget(self.input)
            
            l_login3 = Label(
                text="S E N H A: ", 
                size_hint=(.35, .37),
                pos=(70, 220),
                font_size= 17,
                color = [0,0,0,1],
                halign = ('center')
            )

            layout_main.add_widget(l_login3)
            
            self.input2 = TextInput(
                multiline= False,
                size_hint=(.50, .1),
                pos=(300, 330),
                hint_text='Digite a senha...',
                padding_y=(30)
            )
        
            layout_main.add_widget(self.input2)
            
            botaoL = Button(
                    text="E N T R A R",
                    color=(1, 1, 1, 1),
                    pos_hint={'x': 0.3, 'y':0.29},
                    halign=('center'),
                    size_hint=(0.4, 0.050),
                    background_color=(1, 3, 1, 3),
                    font_size=(15),
                    
                )
            
            layout_main.add_widget(botaoL)

            return layout_main
    
    def login(self, instance):
        login = self.matricula_cps_input.text
        print('Matrícula ou CPF:', login)
        print (" ")



Tela_Login_Aluno().run()