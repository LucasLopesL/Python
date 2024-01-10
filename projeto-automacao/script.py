import pyautogui
import time
import pandas

pyautogui.PAUSE = 1

#Passo 01 - Acessar o chrome e entrar no site

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(5)

#Passo 02 - Fazer Login

pyautogui.click(x=751, y=470)
pyautogui.white("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("minha senha")
pyautogui.press("tab")
pyautogui.click(x=946, y=676, button= "left")

tabela = pandas.read_csv("produtos.csv")

#Passo 03 - Cadastrar Produto
for linha in tabela.index:
    pyautogui.click(x=725, y=323)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco = tabela.loc[linha, "preco"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
        
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(5000)
