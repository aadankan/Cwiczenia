#! python3
# downloadXkcd.py-Pobiera wszystkie komiksy opublikowane w witrynie XKCD

import requests, os, bs4

url = 'gttp://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    # TODO: Poranie strony

    # TODO: Ustalenie adresu URL pliku obrazu komiksu

    # TODO: Pobranie obrazu

    # TODO: Zapis obrazu w katalogu ./xkcd.

    # TODO: Pobranie adresu URL w przycisku Prev

print('Gotowe!')