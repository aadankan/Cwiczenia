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

# TODO: Iteracja przez pliki znajdujace sie w katalogu roboczym

# TODO: Pominiecie plikow bez daty

# TODO: Pobranie poszczegolnych fragmentow nazwy plikou

# TODO: Przygotowanie nazwy pliku zawierajacej date w formacie europejskim

# TODO: Pobranie pelnych bezwzglednych sciezek dostepu do pliku

# TODO: Zmiana nazwy plikow
