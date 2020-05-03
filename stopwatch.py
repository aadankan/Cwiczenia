#! python3
# stopwatch.py-prosty program stopera

import time

# Wyswietlanie inforamcji o sposobie dzialania programu
print('Nacisnij Enter, aby rozpoczac. Kolejne nacisniecie Enter oznacza nowe okrazenie. Nacisniecie Ctrl+C '
      'konczy dzialanie programu')
input()  # Nacisnij Enter, aby rozpoczac
print('Rozpoczeto dzialanie.')
startime = time.time()  # Pobranie godziny rozpoczecia pierwszego okrazenia
lastTime = startime
lapNum = 1

# Rozpoczecie pomiaru czasu okrazenia
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startime, 2)
        print('Okrazenie #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()  # Wyzerowanie czasu ostatniego okrazenia
except KeyboardInterrupt:
    # Obsluga wyjatku zglaszanego po nacisnieciu klawiszy Ctrl+C. Dzieki temu nie bedzie wyswietlony komunikat bledu
    print('\nGotowe')
