from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivymd.uix.screen import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton
import qrcode

class TelaEstudante(MDApp):
    def build(self):
        self.screen = Screen()

        # Adicionando a imagem de fundo
        self.background = Image(source="/Users/emill/Downloads/fundo de tela.jpg", allow_stretch=True, keep_ratio=False)
        self.screen.add_widget(self.background)

        # Layout principal
        self.layout = MDBoxLayout(orientation='vertical', padding=40, spacing=20)

        # Adicionando o rótulo no topo da tela
        self.label = MDLabel(text="Sua Carteira Digital", halign="center", theme_text_color="Secondary", text_color=(0, 1, 0, 1))  # Cor vermelha
        self.layout.add_widget(self.label)

        # Campos de texto para nome e série
        self.name_field = MDTextField(hint_text="Nome", size_hint_y=None, height=50)
        self.series_field = MDTextField(hint_text="Série", size_hint_y=None, height=50)

        # Adicionando os campos de texto ao layout
        self.layout.add_widget(self.name_field)
        self.layout.add_widget(self.series_field)

        # Botão para gerar o QR Code
        self.generate_button = MDFlatButton(text="Gerar QR Code", on_release=self.generate_qr_code)
        self.layout.add_widget(self.generate_button)

        # Adicionando o layout principal à tela
        self.screen.add_widget(self.layout)

        return self.screen

    def generate_qr_code(self, instance):
        # Verificando se os campos de texto estão preenchidos
        if self.name_field.text.strip() == "" or self.series_field.text.strip() == "":
            self.label.text = "Por favor, preencha todos os campos."
            return

        # Criando e exibindo o QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data("Nome: {}\nSérie: {}".format(self.name_field.text, self.series_field.text))
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color="black", back_color="white")
        qr_image.save("qrcode.png")

        qr_code_image = Image(source="qrcode.png", size_hint=(None, None), size=(200, 200), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.screen.add_widget(qr_code_image)

if __name__ == '__main__':
    TelaEstudante().run()
