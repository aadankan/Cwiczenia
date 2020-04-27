#! python3
# mapIt.py-Wyswietla w przegladarce WWW mape na podstawie adresu
# podanego w wierszu polecen lub w schowku

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Pobranie adresu z wiersza polecen
    address = ' '.join(sys.argv[1:])
else:
    # Pobranie adresu ze schowka
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

