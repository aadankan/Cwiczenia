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

    # Utworzenie archiwum ZIP
    print('Tworzenie archiwum %s...' % zipFilename)
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Przejscie przez cale drzewo katalogu i kompresja plikow we wszystkich podkatalogach
    for foldername, subfolders, filenames in os.walk(folder):
        print('Dodawanie plikow w %s...' % foldername)
        # Dodanie biezacego katalogu do archiwum ZIP
        backupZip.write(foldername)
        # Dodanie wszystkich plikow znajdujacych sie w tym katalogu do archiwom ZIP
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue    # W archiwum nie umieszczamy plikow innych archiwow
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Gotowe!')

backupToZip('')
