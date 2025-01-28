# src/email_sender.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class EmailSender:
    def __init__(self, sender_email: str, sender_password: str, recipient_email: str):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.recipient_email = recipient_email
        self.smtp_server = 'smtp.gmail.com'  # Usando Gmail como ejemplo
        self.smtp_port = 587  # Puerto para Gmail

    def send_email(self, subject: str, attachment_file: str, total_all_products: float, total_top_10_products: float, percentage_top_10: float):
        try:
            # Crear el mensaje
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = self.recipient_email
            msg['Subject'] = subject

            # Generar el cuerpo del correo con los datos proporcionados
            body = f"""
            Resumen de productos vendidos:

            Total de productos vendidos: {total_all_products:.2f}
            Total de los 10 productos más vendidos: {total_top_10_products:.2f}
            Porcentaje de los 10 productos más vendidos respecto al total: {percentage_top_10:.2f}%

            Adjuntamos el archivo con los 10 productos más vendidos.
            """
            msg.attach(MIMEText(body, 'plain'))

            # Adjuntar el archivo
            with open(attachment_file, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={attachment_file}')
                msg.attach(part)

            # Conectar al servidor SMTP y enviar el correo
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Inicia la conexión segura
                server.login(self.sender_email, self.sender_password)  # Iniciar sesión
                server.sendmail(self.sender_email, self.recipient_email, msg.as_string())  # Enviar el correo

            print(f"Correo enviado con éxito a {self.recipient_email}")

        except Exception as e:
            print(f"Error al enviar el correo: {e}")
