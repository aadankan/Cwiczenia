#! python3
# mcb.pyw - Zapisuje i wczytuje do schowka fragmenty tekstu
# Użycie: py.exe mcb.pyw save <słowo-kluczowe>-Zapis schowka wraz ze słowem kluczowym.
#   py.exe mcb.pyw <słowo-kluczowe>-Wczytywanie słowa kluczowego schowka
#   py.exe mcb.pyw list-Wczytanie wszystkich słów kluczowych do schowka.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# TODO: Zapis zawartości schowka.

# TODO: Wyświetlanie listy słów kluczowych i wczytywanie tresci.

mcbShelf.close()
