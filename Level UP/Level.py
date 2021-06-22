# coding=utf-8

import pyautogui
import pyperclip
import time
import random

time.sleep(3)
print('What word you want to key in?')
output_words = str(input())
print('time to rest?(seconds)')
restseconds = int(input())
print('add a random number on time, How many seconds?\n(輸入兩個分別為隨機的起始及結束數字並以空格分開)')
randomtimeA, randomtimeB = map (int,input().split( ))
for i in range (3, 0, -1):
    print (f'start in {i}')
    time.sleep(1)
while 1:
    pyperclip.copy(output_words)
    pyautogui.hotkey('Ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')
    for i in range (restseconds - 1 + random.randint(randomtimeA, randomtimeB), 0, -1):
        print (f'\r經過{i}秒再複製一次', end='')
        time.sleep(1)
