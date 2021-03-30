from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller

class Browser:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        # Verifique se a versão atual do chromedriver existe
        # e se não existir, baixe-o automaticamente,
        # em seguida, adicione chromedriver ao caminho
        chromedriver_autoinstaller.install()    

        # Ocultar navegador
        #chrome_options.add_argument("--headless")
        #chrome_options.add_argument("--no-sandbox")
        #chrome_options.add_argument("--mute-audio")
        # Guardando cache de cookies
        #chrome_options.add_argument("--profile-directory=Default")
        #chrome_options.add_argument("--user-data-dir=/tmp/browser/")

        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.maximize_window()