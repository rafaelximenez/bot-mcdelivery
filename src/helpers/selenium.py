from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import time

class Selenium:
    def __init__(self):
        # Verifique se a versão atual do chromedriver existe
        # e se não existir, baixe-o automaticamente,
        # em seguida, adicione chromedriver ao caminho
        chromedriver_autoinstaller.install()    

        self.driver = webdriver.Chrome()

    def login(self):
        url = 'https://mcdelivery.mcdonalds.com.br/'
        zipcode = ''
        number = ''
        complement = ''

        self.driver.get(url)

        self.driver.find_element_by_xpath('/html/body/main/div/div/div/div/div[1]/div[2]/div[2]/form/div/input').send_keys(zipcode + Keys.RETURN)

        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/main/div/div/div/div/div[1]/form/div[4]/div[1]/input').send_keys(number)
        self.driver.find_element_by_xpath('/html/body/main/div/div/div/div/div[1]/form/div[4]/div[2]/input').send_keys(complement + Keys.RETURN)

