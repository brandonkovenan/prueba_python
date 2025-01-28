import os
from src.email_sender import EmailSender

def test_send_email(mocker):
    # Mock del servidor SMTP
    mock_smtp = mocker.patch('smtplib.SMTP', autospec=True)

    # Configurar datos del correo
    sender_email = "brandonkovenan@gmail.com"
    sender_password = "dwgc xpeb cals onqo"
    recipient_email = "brandonkovenan@gmail.com"
    subject = "Test Email"
    body = "Este es un correo de prueba."
    attachment_file = './tests/mock_attachment.txt'
    # Configurar valores para 'total_top_10_products' y 'percentage_top_10'
    total_top_10_products = [...]  # Los datos que se esperan
    percentage_top_10 = [...]      # Los datos que se esperan
    
    # Crear archivo adjunto simulado
    with open(attachment_file, 'w') as file:
        file.write("Contenido de prueba para el archivo adjunto.")

    # Enviar correo
    email_sender = EmailSender(sender_email, sender_password, recipient_email)
    email_sender.send_email(subject, body, attachment_file, total_top_10_products, percentage_top_10)

    # Verificar que SMTP fue llamado correctamente
    mock_smtp.assert_called_with('smtp.gmail.com', 587)
    server = mock_smtp.return_value
    server.starttls.assert_called_once()
    server.login.assert_called_once_with(sender_email, sender_password)
    server.sendmail.assert_called_once()

    # Limpiar archivo de prueba
    os.remove(attachment_file)
