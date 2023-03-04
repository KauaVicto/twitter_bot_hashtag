import os
from selenium import webdriver

class BotTwitter:

    def __init__(self) -> None:
        self.iniciarSelenium()


    def iniciarSelenium(self):
        dir_path = os.getcwd()
        profile = os.path.join(dir_path, "profile", "bot")
        options = webdriver.ChromeOptions()
        options.add_argument(r"user-data-dir={}".format(profile))
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        self.driver = webdriver.Chrome("./public/chromeDriver.exe", options=options)

    
    def abrirSite(self, site):
        self.driver.get(site)


    def buscarTwits(self):
        pass