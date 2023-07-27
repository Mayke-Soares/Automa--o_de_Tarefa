
import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 2

# abrir ubuntu
pyautogui.press("win")
pyautogui.write("Ubuntu")
pyautogui.press("enter")

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(.5)

# Abrir whatsapp
pyautogui.click(x=47, y=88) # clicar no ícone

# Abrir youtube
pyautogui.click(x=265, y=18) # Abrir aba 2
pyautogui.click(x=116, y=91) # clicar no ícone

# Google tradutor
pyautogui.click(x=503, y=23) # Abrir aba 3
pyautogui.click(x=273, y=91) # clicar no ícone

# Curso em vídeo
pyautogui.click(x=749, y=17) # Abrir aba 4
pyautogui.click(x=339, y=89) # clicar no ícone

pyautogui.click(x=986, y=11) #Abrir aba 5
pyautogui.click(x=536, y=86) # clicar no ícone

pyautogui.click(x=1122, y=17) # Abrir aba 6
pyautogui.click(x=873, y=85) # clicar no ícone"""
