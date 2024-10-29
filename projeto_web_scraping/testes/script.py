from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from PIL import Image
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

# Actions Chains -> Bom para alguns dropdowns especiais
menu = driver.find_element(By.XPATH, 'xpath')
item = driver.find_element(By.XPATH, "xpath")
ActionChains(driver).move_to_element(menu).perform()
sleep(0.5)
item.click()


# Alertas

caminho = os.getcwd()
arquivo = caminho + r"/alertas.html"
driver.get(arquivo)

# Alertas básicos
driver.find_element(By.XPATH, "/html/body/div[2]/input").click()
alerta = Alert(driver) # ou alerta = driver.switch_to.alerta
alerta.accept()

# Alerta com confirmação
driver.find_element(By.XPATH, "/html/body/div[3]/input").click()
alerta = Alert(driver)
# Pegar o texto do alerta
print(alerta.text)
# Aceitar
alerta.accept()
# Cancelar
alerta.dismiss()

# Alerta com Input
driver.find_element(By.XPATH, "/html/body/div[4]/button").click()
alerta = Alert(driver)
# Envia informações para o input do alerta
alerta.send_keys("123.456.789-07")
alerta.accept()


# Abas e diferentes Janelas

caminho = os.getcwd()
arquivo = caminho + r"/Pagina Hashtag.html"
driver.get(arquivo)

# Funciona da mesma forma para janelas e abas
driver.find_element(By.XPATH, "/html/body/section[2]/div/div[6]/figure/a/img").click() # Muda pra nova ABA
lista_abas = driver.window_handles()
aba_original = lista_abas[0]
aba_bi = lista_abas[1]
driver.switch_to.window(aba_bi) # Muda para a nova aba
driver.find_element(By.ID, "firstname").send_keys("Lucas")
driver.find_element(By.ID, "email").send_keys("lucasreidopython@gmail.com")
driver.find_element(By.ID, "phone").send_keys('11 99999-9999')
driver.find_element(By.ID, "_form_1155_submit").click()
driver.switch_to.window(aba_original) # Volta pra aba orinal
driver.close() # Fecha a aba ativa/atual
driver.quit() # Fecha o navegador

# Pop-ups

driver.get("https://www.hashtagtreinamentos.com/")
# Loop
while len(driver.find_element(By.ID, "botaoPopupFechar")) < 1: # Esperar o Pop-up aparecer na tela
    sleep(1)
sleep(1)

driver.find_element(By.ID, "botaoPopupFechar").click()

# Expected Conditions (EC) -> Loop padrão do Selenium
driver.get("https://www.hashtagtreinamentos.com/")
element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "botaoPopupFechar"))
)
sleep(1) # Garantia de que o item apareceu na tela
element.click()


# PrintScreen - Tela Inteira e parte da tela

caminho = os.getcwd()
arquivo = caminho + r"/Pagina Hashtag.html"
driver.get(arquivo)

# Tela Inteira
driver.save_screenshot("projeto_web_scraping\testes\prints\print.png")

# Parte da tela
imagem = Image.open("projeto_web_scraping\testes\prints\print.png")
# No crop() devemos passar a posição das quatro pontas em formato de TUPLA de ontem tiraremos o print (Base de eixo x e eixo y) -> Usar a ferramenta do desenvolvedor. Se não funcionar olhe a escala da tela do seu computador (Multiplique pela escala)
xy_imagem = driver.find_element(By.ID, "header")

posicao = xy_imagem.location
tamanho = xy_imagem.size

x_inicial = posicao["x"]
y_inicial = posicao["y"]
x_final = x_inicial + tamanho["width"]
y_final = y_inicial + tamanho["height"]

imagem = imagem.crop((x_inicial, y_inicial, x_final, y_final))
imagem.save("projeto_web_scraping\testes\prints\pedaco_print.png")

# Gereciamento da tela do navegador
driver.maximize_window()
driver.minimize_window()

options = webdriver.ChromeOptions()
options.add_argument('--headless') # Modo para rodar a automação de forma secreta (Sem aparecer)
options.add_argument(r'user-data-dir=C:\Users\lucas\AppData\Local\Google\Chrome\User Data\Profile Selenium') # Modo de abri o navegador com cookies e logins (para saber o perfil -> chrome://version)
options.add_argument('--start-maximaze')
options.add_argument('--disable-extensions')
novo_driver = driver = webdriver.Chrome(service=servico, options=options)
