import pyautogui
import time
import subprocess

repeticoes = 2

for i in range(repeticoes):

  navegador =  subprocess.Popen(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
time.sleep(7)
pyautogui.PAUSE = 0.2
pyautogui.press('d')
pyautogui.press('o')
pyautogui.press('l')
pyautogui.press('a')
pyautogui.press('r')
pyautogui.press('space')
pyautogui.press('h')
pyautogui.press('o')
pyautogui.press('j')
pyautogui.press('e')
pyautogui.press("enter")
time.sleep(5)

navegador.terminate()
#pyautogui.hotkey('alt','f4')
