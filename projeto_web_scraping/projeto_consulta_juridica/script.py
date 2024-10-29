from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pandas as pd
import os


# Criar o navegador
servico  = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)

# Caminho da página
caminho = os.getcwd()
arquivo = caminho + r'\index.html'

# Coletar as informações da planilha
lista_processos = pd.read_excel(r'projeto_web_scraping\projeto_consulta_juridica\Processos.xlsx')

for processo in lista_processos.index():

    # Acessar a página para cada processo
    driver.get(arquivo)
    # Mover o mouse
    menu = driver.find_element(By.XPATH, "/html/body/div[2]/div/button")
    ActionChains(driver).move_to_element(menu).perform()
    # Saber o estado e clicar
    estado = lista_processos.loc[processo, "Cidade"]
    # if estado == 'São Paulo':
    #     driver.find_element(By.XPATH, "/html/body/div[2]/div/div/a[1]").click()
    # elif estado == "Distrito Federal":
    #     driver.find_element(By.XPATH, "/html/body/div[2]/div/div/a[2]").click()
    # else:
    #     driver.find_element(By.XPATH, "/html/body/div[2]/div/div/a[3]").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, estado).click()
    # Listar as abas
    abas = driver.window_handles()
    # Índice das abas
    indice = 1 + processo
    # Mudar para a aba aberta
    nova_aba = driver.switch_to.window(abas[indice])
    # Preencher o nome da parte
    driver.find_element(By.ID, "nome").send_keys(lista_processos.loc[processo, "Nome"])
    # Preencher o nome do advogado
    driver.find_element(By.ID, "advogado").send_keys(lista_processos.loc[processo, "Advogado"])
    # Preencher o número do processo
    driver.find_element(By.ID, "numero").send_keys(lista_processos.loc[processo, "Processo"])
    # Clicar em pesquisar processo
    driver.find_element(By.CLASS_NAME, "registerbtn").click()
    # Trocar para o alerta
    alerta = Alert(driver)
    # Garatir que o alerta apareceu
    sleep(1)
    # Verificar se o processo existe
    texto_alerta = alerta.text
    if "Processo encontrado com sucesso" in texto_alerta:
        lista_processos.loc[processo, "Status"] = "Processo encontrado com sucesso!"
        # Aceitar alerta
        alerta.accept()
    else:
        lista_processos.loc[processo, "Status"] = "Processo NÃO encontrado!"
        # Fechar o alerta
        alerta.accept()
    # Esperar o segundo alerta aparecer para acessar o processo
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    # Trocar para o alerta
    alerta2 = driver.switch_to.alert
    # Aceitar o alerta
    alerta2.accept()
    # Fechar o navegador
    driver.quit()

