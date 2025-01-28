import os
from src.dane_file_downloader import DaneFileDownloader

def test_descargar_archivo(mocker):
    # Mock de requests.get para evitar la necesidad de hacer una solicitud real
    mock_request = mocker.patch('requests.get', autospec=True)
    mock_request.return_value.ok = True
    mock_request.return_value.content = b"Contenido del archivo descargado"

    # Archivo simulado
    output_file = './data/anexo_referencias_mas_vendidas.xlsx'

    # Crear instancia de DaneFileDownloader con el directorio de descarga
    downloader = DaneFileDownloader(download_directory='./downloads')

    # Ejecutar la función de descarga
    downloader.descargar_archivo(url="https://example.com", selector=".download-link")  # URL y selector para el enlace de descarga

    # Verificar que el archivo fue descargado correctamente
    assert os.path.exists(output_file)

    # Verificar que requests.get fue llamado
    mock_request.assert_called_once()

    # Limpiar archivo descargado
    os.remove(output_file)
