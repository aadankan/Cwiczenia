#! python3
# quickWeather.py-Wyswietla prognoze pogody dla lokalizacji podanej w wierszu polecen

import json, requests, sys

# Ustalenie lokalizacji na podstawie argumentow wiersza polecen
if len(sys.argv) < 2:
    print('Uzycie: quickWeather.py lokalizacja')
    sys.exit()
location = ' '.join(sys.argv[1:])

# TODO: Pobranie danych w formacie JSON z API witryny OpenWeatheMap.org

# TODO: Umieszczenie danych JSON w zmiennej Pythona
