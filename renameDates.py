#! python3
# reneameDates.py-Zmienia nazwe pliku wraz z data w formacie amerykanskim(MM-DD-RRRR)
# na date w formacie europejskim

import shutil, os, re

# Utworzenie wyrazenia regularnego dopasowujacego pliki zawieracjace w nazwie date w formacie amerykanskim.
datePattern = re.compile(r"""^(.*?) #Caly tekst przed data
    ((0|1)?\d)-                     #Jedna lub dwie cyfry okreslajace miesiac
    ((0|1|2|3)?\d)-                 #Jadna lub dwie cyfry okreslajace dzien
    ((19|20)\d\d)                   #Cztery cyfry okreslajace rok
    (.*?)$                          #Caly tekst po dacie
    """, re.VERBOSE)

# Iteracja przez pliki znajdujace sie w katalogu roboczym
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Pominiecie plikow bez daty
    if mo == None:
        continue

    # Pobranie poszczegolnych fragmentow nazwy plikou
    befortPart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

# TODO: Przygotowanie nazwy pliku zawierajacej date w formacie europejskim

# TODO: Pobranie pelnych bezwzglednych sciezek dostepu do pliku

# TODO: Zmiana nazwy plikow
