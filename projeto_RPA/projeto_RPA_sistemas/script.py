import pyautogui
from time import time

# Vamos coletar informações de um sistema e enviá-las por e-mail
# pyautogui.write() -> Escreve
# pyautogui.click() -> clica
# pyautogui.locateOnScreen() -> Localiza um elemento na tela
# pyautogui.hotkey() -> Atalhos do teclado
# pyautogui.press() -> aperta um botão do teclado

# Abrir o Chrome

pyautogui.PAUSE = 0.5 # Pause entre cada comando
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")

# Pesquisa por gmail
pyautogui.write("gmail")
pyautogui.press("enter")

# Localizar o gmail e clicar nele
x, y, largura, altura = pyautogui.locateOnScreen(r"projeto_RPA\projeto_RPA_sistemas\imagens\gmail.png")
pyautogui.click(x + largura/2, y + altura/2)

# Esperar o gmail carregar 


