# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 10:09:15 2024

@author: leonardo

"""
import pyautogui as py
import pyperclip # usar texto com caracteres especiais
import time #para conseguir dar pausa em uma etapa específica
import pandas as pd


df = pd.read_excel("test1.xlsx")
py.hotkey('alt','tab')

for i in range(len(df.loc[0])):
    if (str(df.loc[0][i])) != 'nan':
        if i == 0:
            py.click(x=54,y=53)
            pyperclip.copy(str(df.loc[1][i]))
            time.sleep(.9)
            py.hotkey('ctrl', 'v')
  
        elif i == 1:
            py.click(x=58,y=69)
            pyperclip.copy(str(df.loc[1][i]))
            time.sleep(.9)
            py.hotkey('ctrl', 'v')
        
        elif i == 2:
            py.click(x=59,y=91)
            pyperclip.copy(str(df.loc[1][i]))
            time.sleep(.9)
            py.hotkey('ctrl', 'v')