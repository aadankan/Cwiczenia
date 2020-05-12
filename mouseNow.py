#! python3
# mouseNow.py-Wyswietla biezace polozenie kursora myszy
import pyautogui
print('Nacisnij klawisze Ctrl+C, aby zakonczyc dzialanie programu.')
try:
    while True:
        # Pobranie i wyswietlenie wspolrzednych kursora myszy
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)


except KeyboardInterrupt:
    print('\nGotowe!')

