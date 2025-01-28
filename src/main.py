from dane_file_downloader import DaneFileDownloader
from processor import DataProcessor
from email_sender import EmailSender
import os


def main():
    # Directorio de descarga
    download_directory = r"H:\Cursos y Proyectos\Prueba Python\data"

    # Nombre del archivo descargado y procesado
    downloaded_file = os.path.join(download_directory, "pvpapn-2021-03-18-anexo-referencias-mas-vendidas.xlsx")
    processed_file = os.path.join(download_directory, "top_10_productos.xlsx")

    # URL y selector del enlace a descargar
    url = "https://www.dane.gov.co/index.php/estadisticas-por-tema/precios-y-costos/precios-de-venta-al-publico-de-articulos-de-primera-necesidad-pvpapn"
    selector = ".btn.btn-gray[title='Anexo referencias mas vendidas']"

    # Descargar archivo
    print("Iniciando la descarga del archivo...")
    downloader = DaneFileDownloader(download_directory)
    downloader.descargar_archivo(url, selector)

    # Procesar datos
    print("Iniciando procesamiento de datos...")
    processor = DataProcessor(input_file=downloaded_file)
    total_all_products, total_top_10_products, percentage_top_10 = processor.extract_top_products(output_file=processed_file)

    # Enviar email con el resumen
    print("Iniciando envío de email...")
    sender_email = "brandonkovenan@gmail.com"
    sender_password = "dwgc xpeb cals onqo"
    recipient_email = "brandonkovenan@gmail.com"

    email_sender = EmailSender(sender_email, sender_password, recipient_email)
    email_sender.send_email(
        subject="Resumen de Productos Vendidos",
        attachment_file=processed_file,
        total_all_products=total_all_products,
        total_top_10_products=total_top_10_products,
        percentage_top_10=percentage_top_10
    )

    print("Proceso completado exitosamente.")


if __name__ == "__main__":
    main()
