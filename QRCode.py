from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
import mysql.connector
import qrcode

class GeradorQRCode(BoxLayout):
    def gerar_qrcode(self):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='carteira_sesi'
            )
            cursor = conn.cursor()

            matricula = self.ids.input_matricula.text
            senha = self.ids.input_senha.text

            query = 'SELECT conteudo FROM carteira_sesi WHERE matricula = %s AND senha = %s'
            cursor.execute(query, (matricula, senha))
            resultado = cursor.fetchone()

            if resultado:
                conteudo = resultado[0]
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4
                )

                qr.add_data(conteudo)
                qr.make(fit=True)
                imagem = qr.make_image(fill_color='black', back_color='white')
                imagem.save('qrcode.png')
                self.ids.resultado.text = 'QR Code gerado com sucesso!'
            else:
                self.ids.resultado.text = 'Dados inválidos'

            conn.close()
        except Exception as e:
            self.ids.resultado.text = str(e)

class QRCodeApp(MDApp):
    def build(self):
        return Builder.load_file('main.kv')

if __name__ == '__main__':
    QRCodeApp().run()
