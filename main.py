from src.helpers import selenium as slnm
import config

selenium = slnm.Selenium(config)
selenium.login()