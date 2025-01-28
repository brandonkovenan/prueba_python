# Proyecto: Descarga y procesamiento de datos con Selenium y Python

## Descripción
Este proyecto automatiza la descarga de datos desde el sitio web del DANE, procesa los datos descargados para identificar los 10 productos más vendidos, y envía un correo electrónico con el resumen y los datos procesados adjuntos. Se utiliza Selenium para la automatización de la descarga del archivo, Pandas para procesar los datos y smtplib para enviar los correos electrónicos.

## Requisitos
- Python 3.8 o superior
- Navegador Google Chrome
- [Chromedriver](https://sites.google.com/chromium.org/driver/) compatible con tu versión de Chrome
- Dependencias adicionales que se instalan desde el archivo `requirements.txt`

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/brandonkovenan/prueba_python.git
   cd prueba_python

    
## Instalación de dependencias    
    pip install -r requirements.txt

## Ejecución de la prueba
    python src/main.py

## Ejecución de pruebas unitarias
    pip install pytest
    pytest tests/


## Estructura del Proyecto
    prueba_python/
    │
    ├── src/
    │   ├── main.py                # Script principal que descarga, procesa y envía los datos
    │   ├── dane_file_downloader.py  # Clase para gestionar la descarga del archivo
    │   ├── processor.py           # Clase para procesar los datos y extraer los productos más vendidos
    │   └── email_sender.py        # Clase para enviar el correo electrónico
    │
    ├── tests/                     
    │   ├── test_dane_file_downloader.py  # Pruebas para la clase DaneFileDownloader
    │   ├── test_processor.py           # Pruebas para la clase DataProcessor
    │   ├── test_email_sender.py        # Pruebas para la clase EmailSender
    │
    ├── requirements.txt          # Dependencias del proyecto
    ├── README.md                # Documentación del proyecto
    └── .gitignore               # Archivos a ignorar por Git