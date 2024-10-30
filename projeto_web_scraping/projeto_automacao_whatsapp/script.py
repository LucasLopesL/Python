from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pandas as pd
import urllib
import os


service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\lucas\AppData\Local\Google\Chrome\User Data\Profile Selenium')
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://web.whatsapp.com")

tabela = pd.read_excel("projeto_web_scraping\projeto_automacao_whatsapp\Envios.xlsx")

for linha in tabela.index:
    nome = tabela.loc[linha, "nome"]
    mensagem = tabela.loc[linha, "mensagem"]
    arquivo = tabela.loc[linha, "arquivo"]
    telefone = tabela.loc[linha, "telefone"]
    texto = mensagem.replace("fulano", nome) # Substitui o place holder da mensagem pelo nome da pessoa
    texto = urllib.parse.quote(texto) # Codifica a mensagem a ser enviada de por meio da URL, pois não pode haver caracteres como acentos na url
    link = f"https://web.whatsapp.com/send?phone={telefone}&text={texto}" # Personaliza o link do whatsapp para o envio de mensagem automática com nosso parâmentros
    driver.get(link) # Acessa o link, iniciando a conversa e escrevendo a mensagem 
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(((By.ID, 'side')))
    ) # Espera a página do WhatsApp carregar na tela
    # Verificar se existe um arquivo a ser anexado, pegar o caminho e anexá-lo
    if not driver.find_element(By.XPATH, '//*[@id="app]/div/span[2]/div/span/div/div/div/div/div[1]'):
        driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[2]/button/span').click() # Clica no botão enviar e envia a mensagem
        if arquivo != 'N':
            caminho_arquivo = os.path.abspath(f"projeto_web_scraping\projeto_automacao_whatsapp\arquivos\{arquivo}")
            driver.find_element(By.XPATH, '//*[@id=main]/footer/div[1]/div/span[2]/div/div[2]/div/div/span').click() #Clica no botão de anexar
            driver.find_element(By.XPATH, '//*[@id=main]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[4]/button/input').send_keys(caminho_arquivo) # Preenche o input
            sleep(2) # Garante que o arquivo carregou
            driver.find_element(By.XPATH, '//*[@id="app]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div').click() # Envia o arquivo
    else:
        continue
