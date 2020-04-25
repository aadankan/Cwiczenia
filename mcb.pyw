#! python3
# mcb.pyw - Zapisuje i wczytuje do schowka fragmenty tekstu
# Użycie: py.exe mcb.pyw save <słowo-kluczowe>-Zapis schowka wraz ze słowem kluczowym.
#   py.exe mcb.pyw <słowo-kluczowe>-Wczytywanie słowa kluczowego schowka
#   py.exe mcb.pyw list-Wczytanie wszystkich słów kluczowych do schowka.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Zapis zawartości schowka.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif sys.argv[1].lower() == 'del':
    del mcbShelf[sys.argv[2]]

elif len(sys.argv) == 2:
    # Wyświetlanie listy słów kluczowych i wczytywanie treści.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'clear':
        mcbShelf.clear()


mcbShelf.close()
