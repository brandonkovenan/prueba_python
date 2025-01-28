import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class DaneFileDownloader:
    def __init__(self, download_directory):
        self.download_directory = download_directory
        self.driver = None

    def configurar_driver(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": self.download_directory,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def descargar_archivo(self, url, selector):
        try:
            # Configurar el driver
            self.configurar_driver()

            # Paso 1: Acceder al sitio web
            self.driver.get(url)

            # Esperar a que el enlace esté disponible
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector))
            )

            # Paso 2: Localizar el enlace usando el selector
            enlace = self.driver.find_element(By.CSS_SELECTOR, selector)

            # Desplazar hasta el enlace
            self.driver.execute_script("arguments[0].scrollIntoView(true);", enlace)

            # Esperar a que el enlace sea clickeable
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
            )

            # Imprimir el enlace para verificar
            print(f"Este es el enlace a descargar: {enlace.get_attribute('href')}")

            # Paso 3: Intentar hacer clic en el enlace usando ActionChains
            action = ActionChains(self.driver)
            action.click(enlace).perform()

            # Esperar un tiempo fijo para que el archivo se descargue
            time.sleep(10)  # Ajusta el tiempo según la velocidad de tu conexión

        finally:
            # Paso 4: Cerrar el navegador
            if self.driver:
                self.driver.quit()

        print("Archivo descargado con éxito.")
