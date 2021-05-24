# coding=utf-8

import discord
from discord.ext import commands

import pyautogui
import pyperclip
import time

while 1:
    pyperclip.copy('不要把我丟掉')
    pyautogui.hotkey('Ctrl', 'v')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(57)