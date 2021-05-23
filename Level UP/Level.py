# coding=utf-8

import pyautogui
import pyperclip
import time

while 1:
    pyperclip.copy('.')
    pyautogui.hotkey('Ctrl', 'v')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(57)