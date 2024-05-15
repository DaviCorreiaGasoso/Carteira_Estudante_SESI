from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.screen import MDScreen



KV = '''
ScreenManager:
    Screen:
        name: 'home'
        MDFlatButton:
            text: "Deletar"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1    # Cor do texto branca
            md_bg_color: 1, 1, 1, 1    # Cor de fundo preta
            pos_hint: {'center_x': 0.5, 'center_y': 0.4}
            on_release: app.root.current = 'TelaDeletar'
        
        MDFlatButton:
            text: "Inserir"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1    # Cor do texto branca
            md_bg_color: 0, 0, 0, 1    # Cor de fundo preta
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            on_release: app.root.current = 'TelaInserir'

        MDLabel:
            text: "Supervisão"
            halign: "center"
            theme_text_color: "Custom"
            text_color: "blue"
            pos_hint: {"center_x": .5, "center_y": .6}

    Screen:
        name: 'TelaInserir'
        MDFlatButton:
            text: "Voltar"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1  # Cor do texto branca
            md_bg_color: 0, 0, 0, 1  # Cor de fundo preta
            pos_hint: {'center_x': 0.4, 'center_y': 0.4}
            on_release: app.root.current = 'home'

        MDFlatButton:
            text: "Supervisão"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1  # Cor do texto branca
            md_bg_color: 0, 0, 1, 1  # Cor de fundo preta
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            on_release: app.root.current = 'home'
        
        MDFlatButton:
            text: "Porteiro"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1  # Cor do texto branca
            md_bg_color: 0, 0, 1, 1  # Cor de fundo preta
            pos_hint: {'center_x': 0.35, 'center_y': 0.5}
            on_release: app.root.current = 'home'
        
        MDFlatButton:
            text: "   Aluno   "
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1  # Cor do texto branca
            md_bg_color: 0, 0, 1, 1  # Cor de fundo preta
            pos_hint: {'center_x': 0.5, 'center_y': 0.6}
            on_release: app.root.current = 'home'
        
        MDFlatButton:
            text: "Responsável"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1  # Cor do texto branca
            md_bg_color: 0, 0, 1, 1  # Cor de fundo preta
            pos_hint: {'center_x': 0.35, 'center_y': 0.6}
            on_release: app.root.current = 'home'

        
    
    Screen:
        name: 'TelaDeletar'
        MDFlatButton:
            text: "Voltar"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1  # Cor do texto branca
            md_bg_color: 0, 0, 0, 1  # Cor de fundo preta
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            on_release: app.root.current = 'home'
'''


class CommonComponentLabel(MDLabel):
    pass


class MobileView(MDScreen):
    pass


class TabletView(MDScreen):
    pass


class DesktopView(MDScreen):
    pass


class ResponsiveView(MDResponsiveLayout, MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = MobileView()
        self.tablet_view = TabletView()
        self.desktop_view = DesktopView()


class Test(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Red'
        return Builder.load_string(KV)


Test().run()