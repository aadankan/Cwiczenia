#! python3
# stopwatch.py-prosty program stopera

import time

# Wyswietlanie inforamcji o sposobie dzialania programu
print('Nacisnij Enter, aby rozpoczac. Kolejne nacisniecie Enter oznacza nowe okrazenie. Nacisniecie Ctrl+C '
      'konczy dzialanie programu')
input()                     # Nacisnij Enter, aby rozpoczac
print('Rozpoczeto dzialanie.')
startime = time.time()      # Pobranie godziny rozpoczecia pierwszego okrazenia
lastTime = startime
lapNum = 1

# TODO: Rozpoczecie pomiaru czasu okrazenia
