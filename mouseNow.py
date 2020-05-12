#! python3
# mouseNow.py-Wyswietla biezace polozenie kursora myszy
import pyautogui
print('Nacisnij klawisze Ctrl+C, aby zakonczyc dzialanie programu.')
try:
    while True:
        # Pobranie i wyswietlenie wspolrzednych kursora myszy
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        pixelColor = pyautogui.screenshot().getpixel((x,y))
        positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
        positionStr += ', ' + str(pixelColor[1]).rjust(3)
        positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)


except KeyboardInterrupt:
    print('\nGotowe!')

