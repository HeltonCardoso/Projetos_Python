import pyautogui
import time

pyautogui.PAUSE = 2 # inserir um time de executação de cada linha de código.
#abrir a ferremaneta , sistema, ou programa

pyautogui.press("win")
pyautogui.write("Excel")
#pyautogui.press("backspace")
pyautogui.press("enter")

time.sleep(7)
pyautogui.click(x=250, y=194)
time.sleep(5)
#pyautogui.hotkey('ctrl', 'shift','n')
pyautogui.hotkey('alt', 'f4')

#pyautogui.press("win")
#pyautogui.write("Chrome")
#pyautogui.press("backspace")
#pyautogui.press("enter")
#pyautogui.click(x=777, y=294)