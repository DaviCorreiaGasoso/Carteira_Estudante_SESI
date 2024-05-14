from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
from kivy.graphics import Canvas, SmoothRoundedRectangle, Color, Line

Window.size = (900,500)
Window.clearcolor = (1,1,1,1)

class MyCanvasWidget(FloatLayout):
    def __init__ (self, **kwargs):
        super(MyCanvasWidget, self).__init__(**kwargs)

        with self.canvas:
            Color(0, 0.2, 1, 0.4)
            tamanho = (500, 100)
            pos_x = (312)
            pos_y = (370)
            SmoothRoundedRectangle(pos=(pos_x, pos_y), size=tamanho)

            lwidth = 100
            lx = 50
            ly = 700
            lc = Color(0,0.5,1,0.5)
            lp = [lx, 0, lx, ly]
            Line(points=lp, width=lwidth)

            lwidth2 = 100
            lx2 = 1080
            ly2 = 700
            lc2 = Color(0,0.5,1,0.5)
            lp2 = [lx2, 0, lx2, ly2]
            Line(points=lp2, width=lwidth2)

class Tela_Login(App):
    def build(self):
        l = MyCanvasWidget()
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
                      font_size=(20),
                      background_normal='',
                      background_color=(0,0,1,0.5))
        
        btnr = Button(text="RESPONSÁVEL",
                      pos_hint={'x':0.4, 'y':0.30},
                      halign=('center'),
                      size_hint=(0.2, 0.075),
                      font_size=(20),
                      background_normal='',
                      background_color=(0,0,1,0.5))
        
        btnf = Button(text="FUNCIONÁRIO",
                      pos_hint={'x': 0.4, 'y':0.20},
                      halign=('center'),
                      size_hint=(0.2, 0.075),
                      font_size=(20),
                      background_normal='',
                      background_color=(0,0,1,0.5))

        l.add_widget(lo)
        l.add_widget(btna)
        l.add_widget(btnr)
        l.add_widget(btnf)
        return l

if __name__ == "__main__":
    Tela_Login().run()