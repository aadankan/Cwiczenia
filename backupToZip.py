#! python3
# backupToZip.py-Katalog wraz z cala zawartoscia zostaje umieszczony
# w archiwum ZIP, ktorego nazwa jest inkrementowana za kazdym razem

import zipfile, os

def backupToZip(folder):
    # Umieszczenie w archiwum ZIP calej zawartosci katalogu

    folder = os.path.abspath(folder)    # Upewniamy sie, ze otrzymalismy bezwgledna sciezke dostepu do folderu

    # Ustalanie nazwy pliku jaka powinna zostac uzyta przez kod na podstawie istniejacych plikow
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    # TODO: Utworzenie archiwum ZIP

    # TODO: Przejscie przez cale drzewo katalogu i kompresja plikow we wszystkich podkatalogach
    print('Gotowe!')

backupToZip('')
