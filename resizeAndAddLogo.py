#! python3
# resizeAndAddLogo.py-Zmiana wielkosci wszystkich obrazow w biezacym katalogu roboczym aby miescily sie w
# kwadracie o wymiarach 300 x 300 pikseli. Nastepnie w prawym dolnym rogu bedzie umieszczone logo catlogo.png
import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'logo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)
# Iteracja przez wszystkie pliki w biezacym katalogu roboczym
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')):
        continue

    im = Image.open(filename)
    width, height = im.size

# TODO: Sprawdzanie, czy konieczna jest zmiana wielkosci obrazu

# TODO: Obliczenie nowej szerokosci i wysokosci obrazu

# TODO: Zmiana wielkosci obrazu

# TODO: Dodanie logo

# TODO: Zapis wprowadzonych zmian
