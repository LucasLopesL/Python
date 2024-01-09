import pyautogui
import time

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
