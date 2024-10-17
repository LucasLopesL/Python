from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os


# Com acessar uma página com o Selenium e interagir com ela

servico  = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)
caminho = os.getcwd()
arquivo = caminho + r'\projeto_web_scraping\index.html'
driver.get('https://google.com/')
driver.get(arquivo)
driver.find_element(By.ID, 'fullname').send_keys("Lira")
driver.find_element(By.ID, 'botao').click()

# Class Name e XPATH

driver.find_element(By.XPATH, '//*[@id="botao"]').click() # O própio navegador pela ferramenta do desenvolvedor (F12) traz a informação do XPath
titulo = driver.find_element(By.CLASS_NAME, 'h1').text
whatsapp = driver.find_element(By.PARTIAL_LINK_TEXT, 'WhatsApp').text
driver.find_element(By.NAME, 'email').text

