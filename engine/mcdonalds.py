from .browser import *
import time, logging, re

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

class Mcdonalds(Browser):
    def __init__(self, config):        
        self.config = config
        super().__init__()
        logger.info('Iniciando navedor!')

    def fill_delivery_data(self):
        url = self.config.BASE_URL
        zipcode = self.config.ZIPCODE
        number = self.config.NUMBER
        complement = self.config.COMPLEMENT

        self.driver.get(url)

        self.driver.find_element_by_xpath('/html/body/main/div/div/div/div/div[1]/div[2]/div[2]/form/div/input').send_keys(zipcode + Keys.RETURN)

        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/main/div/div/div/div/div[1]/form/div[4]/div[1]/input').send_keys(number)
        self.driver.find_element_by_xpath('/html/body/main/div/div/div/div/div[1]/form/div[4]/div[2]/input').send_keys(complement + Keys.RETURN)
        
        time.sleep(1)

        try:
            popup = self.driver.find_element_by_xpath('/html/body/main/div/div/div/div/div[4]/div[2]/div[2]/span')
            if re.search('McDelivery ainda não', popup.text, re.IGNORECASE):
                logger.error('Serviço indisponível!')
                return False
        except:
            logger.info('Serviço disponível!')
            time.sleep(1)

        logger.info('Dados de entrega preenchidos!')
        time.sleep(4)
        return True

    def order_standard_snack(self):
        self.driver.get(f'{self.config.BASE_URL}{self.config.STANDARD_SNACK}')
        time.sleep(5)
        self.driver.execute_script('window.scrollBy(0, 500)')
        self.driver.find_element_by_xpath('/html/body/main/div/section[1]/div/div/div/ul/li/div[3]/div/div[1]/form/div/ul/li[2]').click()
        self.driver.execute_script('window.scrollBy(0, 650)')
        self.driver.find_element_by_xpath('/html/body/main/div/section[1]/div/div/div/ul/li/div[3]/div/div[2]/form/div/ul/li[2]').click()
        self.driver.execute_script('window.scrollBy(0, 650)')
        self.driver.find_element_by_xpath('/html/body/main/div/section[1]/div/div/div/ul/li/div[3]/div/div[3]/form/div/ul/li[3]').click()
        self.driver.execute_script('window.scrollBy(0, 650)')
        self.driver.find_element_by_xpath('/html/body/main/div/section[1]/div/div/div/ul/li/div[3]/div/div[4]/form/div/ul/li[3]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/main/div/section[3]/div/div/div/div[2]/a').click()
        logger.info('Lanche(s) selecionado(s)!')
        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[8]/div/a[1]').click()
        logger.info('Finalizando pedido!')
        time.sleep(5)
    
    def check_out(self):        
        self.driver.execute_script('window.scrollBy(0, 300)')
        self.driver.find_element_by_xpath('/html/body/div[5]/div[3]/div[1]/div[4]/span[3]/a').click()
        self.driver.execute_script('window.scrollBy(0, -300)')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="client-pre-email"]').send_keys(self.config.EMAIL)
        
        logger.info('Pedido finalizado!')
