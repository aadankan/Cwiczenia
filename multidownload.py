#! python3
# multidownload.py-Pobiera wszystkie komiksy opublikowane w witrynie XKCD, uzywajac do tego wielu watkow

import requests, os, bs4, threading
os.makedirs('xkcd,', exist_ok=True)

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Pobranie strony
        print('Pobieranie strony http://xkcd.com/%s...' % urlNumber)
        res = requests.get('http://xkcd.com/%s' % urlNumber)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)

        # Ustalenie adresu URL pliku obrazu komiksu
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Nie udalo sie odnalezc pliku obrazu komiksu')
        else:
            comicUrl = comicElem[0].get('src')
            # Pobranie obrazu
            print('Pobieranie obrazu %s...' % comicUrl)
            res.raise_for_status()

            # Zapis obrazu w katalogu ./xkcd
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

# TODO: Utworzenie i uruchomienie obiektow Thread
# TODO: Zaczekanie na zakonczenie dzialania wszystkich watkow
