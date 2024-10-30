from webdriver_manager.chrome import ChromeDriverManager
from anticaptchaofficial.recaptchav2proxyless import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from chave import chave_api # -> Crie um arquivo chave e armazene a chave de sua API. Para isso é necessário criar uma conta no anti-captcha.com
import time

navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
link = "https://google.com/recaptcha/api2/demo"
navegador.get(link)

chave_captcha = navegador.find_element(By.ID, 'recaptcha-demo').get_attribute('data-sitekey') # -> Encontramos isso dentro da ferramenta do desenvolvedor (F12). Normalmente encontra-se dentro de uma tag iFrame.

solver = recaptchaV2Proxyless()
solver.set_verbose(1)
solver.set_key(chave_api)
solver.set_website_url(link)
solver.set_website_key(chave_captcha)

resposta = solver.solve_and_return_solution()

if resposta != 0: # Se o resultado for diferente de zero, resolvemos o reCAPTCHA
    print(resposta) # A resposta é o token necessário para quebrar o CAPTCHA
    navegador.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{resposta}'") # Preencher o token gerado pela API no campo campo do token do captcha (g-recaptcha-response) que é secreto (display: None). É necessário executar um código em JS (Método -> "execute_script()", pois para interagir com um elemento com o Selenium, ele precisa estar visível na página e no JS não é preciso estar visível. Por ser um campo secreto, utilizamos o JS para realizar essa task.
    navegador.find_element(By.ID, 'recaptcha-demo-submit').click() # Clicar no botão e enviar a resposta (token) para o reCAPTCHA
else:
    print(solver.err_string) # -> Caso não seja resolvido, exibimos qual o texto presente no erro (err_string)

time.sleep(100) # Para manter o navegador aberto
