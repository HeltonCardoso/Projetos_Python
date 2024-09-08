import pyautogui
import time

pyautogui.PAUSE = 2 # inserir um time de executação de cada linha de código.
#abrir a ferremaneta , sistema, ou programa

pyautogui.press("win")
pyautogui.write("Excel")
#pyautogui.press("backspace")
pyautogui.press("enter")

time.sleep(10)
pyautogui.hotkey('alt', 'f4')

#pyautogui.press("win")
#pyautogui.write("Chrome")
#pyautogui.press("backspace")
#pyautogui.press("enter")
#pyautogui.click(x=777, y=294)