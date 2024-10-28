from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from time import sleep
import os


# Configuração Básica
opcoes = webdriver.ChromeOptions()
opcoes.add_experimental_option("prefs", {
    "download.default_directory": r'C:\Users\lucas\OneDrive\Área Pessoal\MeusProjetos\Python\Python\projeto_web_scraping\projeto_emissao_NF\notas',
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})
servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico, options=opcoes)
caminho = os.getcwd()
arquivo = caminho + r'/login.html'
driver.get(arquivo)

# Login

usuario = driver.find_element(By.XPATH, "/html/body/div[2]/form/input[1]").send_keys("Lucas Lopes")
sleep(0.5)
senha = driver.find_element(By.XPATH, "/html/body/div[2]/form/input[2]").send_keys("123456")
sleep(0.5)
login = driver.find_element(By.XPATH, "/html/body/div[2]/form/button").click()
sleep(1)

# Ler dados das NF a serem emitidas

tabela = pd.read_excel(r"projeto_web_scraping\projeto_emissao_NF\NotasEmitir.xlsx")
for linha in tabela:
    # Preenchimento dos dados nos respectivos campos para cada cliente
    nome = driver.find_element(By.NAME, "nome").send_keys(tabela.loc[linha, "Cliente"])
    endereco = driver.find_element(By.NAME, "endereco").send_keys(tabela.loc[linha, "Endereço"])
    bairro = driver.find_element(By.NAME, "bairro").send_keys(tabela.loc[linha, "Bairro"])
    municipio = driver.find_element(By.NAME, "municipio").send_keys(tabela.loc[linha, "MunicIpio"])
    cep = driver.find_element(By.NAME, "cep").send_keys(str(tabela.loc[linha, "CEP"]))
    uf = driver.find_element(By.NAME, "uf").send_keys(Keys.SPACE, tabela.loc[linha, "UF"])
    cnpj_cpf = driver.find_element(By.NAME, "cnpj").send_keys(str(tabela.loc[linha, "CPF/CNPJ"]))
    ie = driver.find_element(By.NAME, "inscricao").send_keys(str(tabela.loc[linha, "Incricao Estadual"]))
    descricao = driver.find_element(By.NAME, "descricao").send_keys(tabela.loc[linha, "Descrição"])
    quantidade = driver.find_element(By.NAME, "quantidade").send_keys(str(tabela.loc[linha, "Quantidade"]))
    valor_unitario = driver.find_element(By.NAME, "valor_unitario").send_keys(str(tabela.loc[linha, "Valor Unitario"]))
    total = driver.find_element(By.NAME, "total").send_keys(str(tabela.loc[linha, "Valor Total"]))
    emitir_nota = driver.find_element(By.CLASS_NAME, "registerbtn").click()
    # Recarregar a página para limpar o formulário
    driver.refresh()
    sleep(1)

