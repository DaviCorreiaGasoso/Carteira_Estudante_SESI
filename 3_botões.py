from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Canvas, Rectangle

Window.size = (900,500)
Window.clearcolor
class Tela_Login(App):
    def build(self):
        l = FloatLayout()
        lo = Label(text="SELECIONE O LOGIN", 
                   pos_hint={'x':0.455, 'y':0.60}, 
                   size_hint=(None, None), 
                   font_size=(50),
                   bold=True,
                   color=[0,0,1,0.9])
        
        btna = Button(text="ALUNO", 
                      pos_hint={'x':0.4, 'y':0.40}, 
                      halign=('center'),
                      size_hint=(0.2, 0.075),
                      font_size=(30))
        
        btnr = Button(text="RESPONSÁVEL",
                      pos_hint={'x':0.4, 'y':0.30},
                      halign=('center'),
                      size_hint=(0.2, 0.075),
                      font_size=(30))
        
        btnf = Button(text="FUNCIONÁRIO",
                      pos_hint={'x': 0.4, 'y':0.20},
                      halign=('center'),
                      size_hint=(0.2, 0.075),
                      font_size=(30))
        
        
        l.add_widget(lo)
        l.add_widget(btna)
        l.add_widget(btnr)
        l.add_widget(btnf)
        return l

if __name__ == "__main__":
    Tela_Login().run()