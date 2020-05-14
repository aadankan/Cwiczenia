import time
import pyautogui
from math import *


class Drawing:
    def __init__(self):
        pass

    def prostokat(self, x, y, wtime):
        time.sleep(self)
        pyautogui.dragRel(x, 0, duration=wtime)
        pyautogui.dragRel(0, x, duration=wtime)
        pyautogui.dragRel(-y, 0, duration=wtime)
        pyautogui.dragRel(0, -y, duration=wtime)

    def trojkat(self, x, h, wtime):
        time.sleep(self)
        pyautogui.dragRel(x*2, 0, duration=wtime)
        pyautogui.dragRel(-x, -h, duration=wtime)
        pyautogui.dragRel(-x, h, duration=wtime)

    def kolo(self, r, wtime):
        time.sleep(self)
        l = 2 * pi * r
        y = 0



    def dom(self, x, y, h, wtime):
        time.sleep(self)
        Drawing.prostokat(0, x, y, wtime)
        pyautogui.moveRel(-1/2*x, 0)
        Drawing.trojkat(0, x, h, wtime)

Drawing.kolo(4, 100, 0.5)



