from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import mysql.connector
import qrcode

class GeradorQRCode(BoxLayout):
    def __init__(self, **kwargs):
        super(GeradorQRCode, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        
        self.add_widget(Label(text='Gerador de QR Code', font_size=24, size_hint_y=None, height=40))
        
        box = BoxLayout(size_hint_y=None, height=40)
        box.add_widget(Label(text='ID:'))
        self.input_id = TextInput(multiline=False)
        box.add_widget(self.input_id)
        self.add_widget(box)
        
        self.button = Button(text='Gerar QR Code', size_hint_y=None, height=50)
        self.button.bind(on_press=self.gerar_qrcode)
        self.add_widget(self.button)
        
        self.resultado = Label(text= '', color=(1, 0, 0, 1), halign='center', valign='middle', size_hint_y=None, height=40)
        self.add_widget(self.resultado)

    def gerar_qrcode(self):
        try:
            conn = mysql.connector.connect(
                   host = 'localhost',
                   user = 'root',
                   password = ' ',
                   database = 'carteira_sesi'       
                )
            cursor = conn.cursor()
            
            id = int(self.ids.input_id.text)
            query= 'SELECT conteudo FROM carteira_sesi WHERE id = %s'
            cursor.execute(query,(id,))
            resultado= cursor.fetchone()

            if resultado:
                conteudo = resultado[0]
                qr = qrcode.QRCode(
                    version = 1,
                    error_connection = qrcode.constants.ERROR_CORRECT_L,
                    box_size= 10,
                    border= 4
                )
                
                qr.add_data(conteudo)
                qr.make(fit=True)
                imagem = qr.make_imagem(fil_color='black', back_color= 'white')
                imagem.save('qrcode.png')
                print('QR Code gerado com sucesso!')
            else:
                print('Nenhum dado encontrado para o ID especificado')
                
            conn.close()
        except Exception as e:
            self.ids.resultado.text = str(e)
            
class QRCodeApp(App):
    def build(self):
        return GeradorQRCode()

if __name__ == '__main__':
    QRCodeApp().run()