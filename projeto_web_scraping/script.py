from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os


# * Com acessar uma página com o Selenium e interagir com ela

servico  = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)
caminho = os.getcwd()
arquivo = caminho + r'\projeto_web_scraping\index.html'
driver.get('https://google.com/')
driver.get(arquivo)
driver.find_element(By.ID, 'fullname').send_keys("Lira")
driver.find_element(By.ID, 'botao').click()

# * Class Name e XPATH

driver.find_element(By.XPATH, '//*[@id="botao"]').click() # O própio navegador pela ferramenta do desenvolvedor (F12) traz a informação do XPath
titulo = driver.find_element(By.CLASS_NAME, 'h1').text
whatsapp = driver.find_element(By.PARTIAL_LINK_TEXT, 'WhatsApp').text
driver.find_element(By.NAME, 'email').text
driver.find_element(By.XPATH, "/html/body/a").get_attribute("href")

# * Interação com diversos Formulários

caminho = os.getcwd()
arquivo = caminho + r"projeto_web_scraping\formulario.html"
driver.find_element(By.XPATH, "/html/body/form/imput[1]").click()
alerta = driver.switch_to.alert
alerta.accept()

# Checkbox
driver.find_element(By.XPATH, "/html/body/form/input[3]").click()
# Verificação de qual o estado do botão
driver.find_element(By.XPATH, "/html/body/form/input[3]").is_selected()

# Campo de texto padrão
driver.find_element(By.XPATH, "/html/body/form/input[16]").send_keys("Corinthans")
# Verificar o que está escrito
driver.find_element(By.XPATH, "/html/body/form/input[16]").get_attribute('value')

# Campo de cores RGB
driver.find_element(By.XPATH, "/html/body/form/input[4]").send_keys("#894d4d")
driver.find_element(By.XPATH, "/html/body/form/input[5]").send_keys("#2143e8")

# Campo de data
driver.find_element(By.XPATH, "/html/body/form/input[6]").send_keys("21/11/2002")
# Verificar o que está preenchido
driver.find_element(By.XPATH, "/html/body/form/input[6]").get_attribute("value")

# Campo de data com minutos
driver.find_element(By.XPATH, "/html/body/form/input[7]").send_keys("21/11/2002", Keys.TAB, "21:30")
# Verificando o que está preenchido
driver.find_element(By.XPATH, "/html/body/form/input[7]").get_attribute("value")

# Campo de anexar arquivo
driver.find_element(By.XPATH, "/html/body/form/input[8]").send_keys(r"C:\Users\lucas\OneDrive\Área Pessoal\MeusProjetos\Python\Python\projeto_web_scraping\formulario.html")
driver.find_element(By.XPATH, "/html/body/form/input[8]").get_attribute("value")

# Campo mês por extenso e ano
driver.find_element(By.XPATH, "/html/body/form/input[9]").send_keys("Outubro", Keys.TAB, "2024")
# verificar o que está escrito
driver.find_element(By.XPATH, "/html/body/form/input[9]").get_attribute("value")

# Campo Numérico
driver.find_element(By.XPATH, "/html/body/form/input[10]").send_keys("10")
# Verificar o que está preenchido
driver.find_element(By.XPATH, "/html/body/form/input[10]").get_attribute("value")

# Campo de senhas
driver.find_element(By.XPATH, "/html/body/form/input[11]").send_keys("LucasReidoPython")

# Campo de Radio Buttons
driver.find_element(By.XPATH, "/html/body/form/input[13]").click()

# Campo de arrastar
driver.find_element(By.XPATH, "/html/body/form/input[15]").send_keys(Keys.ARROW_RIGHT * 50)

# Campo de Horário
driver.find_element(By.XPATH, "/html/body/form/input[17]").send_keys("12:00")

# Campo de Semana e Horário
driver.find_element(By.XPATH, "/html/body/form/input[18]").send_keys("42","2022")

# Campo de texto longo
driver.find_element(By.ID, "story").send_keys('''
    Olá, como está?
    tudo bem?
    que ótimo
    Top
    é nois.
''')
# Limpar o campo
driver.find_element(By.ID, "story").clear()

# Listas Dropdown
driver.find_element(By.XPATH, "/html/body/form/select[1]").send_keys("C")
# Opção 2
driver.find_element(By.XPATH, "/html/body/form/select[1]").click()
sleep(0.5)
driver.find_element(By.XPATH, "/html/body/form/select[1]/option[1]").click()
# Opção 3 -> Select - from selenium.webdriver.support.ui import Select
elemento = driver.find_element(By.TAG_NAME, "select").click()
elemento_select = Select(elemento)
# Index
elemento_select.select_by_index(2)
# Text visível
elemento_select.select_by_visible_text("C")
# Valor
elemento_select.select_by_value("b")
# Descelecionar elemento
# elemento_select.deselect_all()
# elemento_select.deselect_by_index()
# elemento_select.deselect_by_value()
# elemento_select.deselect_by_visible_text()
# Ler os itens selecionados
elemento_select.first_selected_option()
# Ler todos os itens selecionados
# elemento_select.all_selected_options()
