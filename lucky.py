#! python3
# lucky.py-Otwieramy kilka wynikow wyszukiwania Google

import requests, sys, webbrowser, bs4, pyperclip

print('Wyszukiwanie...')    # Komunikat wyswietlany podczas pobierania strony Google
res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Pobranie laczy z kilkoma pierwszymi wynikami wyszukiwania
soup = bs4.BeautifulSoup(res.text)

# Otworzenie karty przegladarki WWW dla kazdego wyniku wyszukiwania
linkElems = soup.select('.kCrYT a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.pl' + linkElems[i].get('href'))

print('cos')
print(linkElems)



