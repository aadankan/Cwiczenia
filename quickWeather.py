#! python3
# quickWeather.py-Wyswietla prognoze pogody dla lokalizacji podanej w wierszu polecen

import json, requests, sys

# Ustalenie lokalizacji na podstawie argumentow wiersza polecen
if len(sys.argv) < 2:
    print('Uzycie: quickWeather.py lokalizacja')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Pobranie danych w formacie JSON z API witryny OpenWeatheMap.org
url = 'htt://api.openweathermap.org/data/2.5/forecast/daile?q=%s&cnt=3' % location
response = requests.get(url)
response.raise_for_status()

# Umieszczenie danych JSON w zmiennej Pythona
weatherData = json.loads(response.text)
# Wyswietlenie opisu pogody
w = weatherData['list']
print('Aktualna pogoda w %s:' % location)
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Jutro:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Pojutrze:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])

