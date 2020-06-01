import pyautogui
import time

while True:
    time.sleep(3)
    pyautogui.click(800, 663)
    time.sleep(0.1)
    pyautogui.click(900, 663)
    time.sleep(0.1)
    pyautogui.click(1000, 663)
    time.sleep(0.1)
    pyautogui.click(1100, 663)
    time.sleep(0.1)
    pyautogui.click(1200, 663)
    time.sleep(0.1)
    pyautogui.click(1300, 663)
    time.sleep(1.5)
    pyautogui.click(1148, 750)
    pyautogui.click(1148, 750)

    time.sleep(5)
    x, y = pyautogui.position(1186, 938)
    pixelColor = pyautogui.screenshot().getpixel((x, y))
    while pixelColor[0] != 207 and pixelColor[1] != 71 and pixelColor[2] != 0:
        x, y = pyautogui.position(1361, 945)
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        if pixelColor[0] != 87 and pixelColor[1] != 195 and pixelColor[2] != 192:
            print('git')
            pyautogui.click(1186, 938)
            pyautogui.click(1186, 958)
            time.sleep(3)
            pyautogui.click(1186, 958)
            break
