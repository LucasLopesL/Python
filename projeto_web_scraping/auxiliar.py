from selenium import webdriver
from time import sleep
import undetected_chromedriver as uc

driver = webdriver.Chrome() # Aparece o aviso de que o navegador está rodando com um software autmatizado
driver = uc.Chrome() # Retira o aviso do navegador
sleep(5)


# Forma de indicar onde está o Chrome Driver caso dê um erro de Arquivo não Encontrado

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


servico = Service(r'"C:\Python312\chromedriver-win64\chromedriver.exe"')
driver = webdriver.Chrome(service=servico)

# Caso de TypeError atualize o Selenium com: pip install --upgrade selenium

# Forma de automatizar a instalação do Chrome Driver e concomitantemente deixá-lo atualizado e evitar possíveis erros no código

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)
