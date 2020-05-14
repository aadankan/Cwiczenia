import time
import pyautogui
from math import *


class Drawing:
    def __init__(self):
        pass

    def prostokat(self=2, x=100, y=100, wtime=0):
        time.sleep(self)
        pyautogui.dragRel(x, 0, duration=wtime)
        pyautogui.dragRel(0, y, duration=wtime)
        pyautogui.dragRel(-x, 0, duration=wtime)
        pyautogui.dragRel(0, -y, duration=wtime)

    def trojkat(self=2, x=100, h=50, wtime=0):
        time.sleep(self)
        pyautogui.dragRel(x * 2, 0, duration=wtime)
        pyautogui.dragRel(-x, -h, duration=wtime)
        pyautogui.dragRel(-x, h, duration=wtime)

    def kolo(self=2, r=100, d=1, wtime=0):
        time.sleep(self)
        i = 0
        a, b = pyautogui.position()
        while i <= 2 * pi:
            x = round(sin(i) * r)
            y = round(cos(i) * r)
            i += 1 / r * d
            pyautogui.click(a+x, b-y, duration=wtime)

    def dom(self=2, x=100, y=100, h=50, wtime=0):
        time.sleep(self)
        Drawing.prostokat(0, x, y, wtime)
        pyautogui.moveRel(-1 / 2 * x, 0)
        Drawing.trojkat(0, x, h, wtime)
        pyautogui.moveRel(3/5*x, 1/5*x)
        Drawing.prostokat(0, x/5, x/5)
        pyautogui.moveRel(3/5*x, 0)
        Drawing.prostokat(0, x / 5, x / 5)
        pyautogui.moveRel(-7/10*x, -1/5*x)
        pyautogui.moveRel(2/5*x,3/5*y)
        Drawing.prostokat(0, x/5, 12/30*y)


Drawing.dom()

