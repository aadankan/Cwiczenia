#! python3
# resizeAndAddLogo.py-Zmiana wielkosci wszystkich obrazow w biezacym katalogu roboczym aby miescily sie w
# kwadracie o wymiarach 300 x 300 pikseli. Nastepnie w prawym dolnym rogu bedzie umieszczone logo catlogo.png

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'Logo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)
# Iteracja przez wszystkie pliki w biezącym katalogu roboczym.
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
       or filename == LOGO_FILENAME:
        continue     # Pominiecie plikow innych niz obrazy oraz obrazu o nazwie pliku takiej samej jak logo.

    im = Image.open(filename)
    width, height = im.size

    # Sprawdzenie, czy konieczna jest zmiana wielkosci obrazu.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Obliczenie nowej szerokosci i wysokosci obrazu.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Zmiana wielkosci obrazu.
        print('Zmiana wielkosci obrazu %s...' % (filename))
        im = im.resize((width, height))

    # Dodanie logo.
    print('Dodanie logo do obrazu %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    # Zapis wprowadzonych zmian.
    im.save(os.path.join('withLogo', filename))
