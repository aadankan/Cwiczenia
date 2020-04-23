#! python3
# phoneAndEmail.py-Wyszukuje numery telefonow i dresy e-mail w schowku.

import pyperclip, re

phoneRegex = re.compile(r"""(
    (\+48|(\+48))?                  # Numer kierunkowy
    (\s|-|\.)?                      # Separator
    (\d{3})                         # Pierwsze trzy cyfry
    (\s|-|\.)                       # Separator
    (\d{3})                         # Trzy cyfy
    (\s|-|\.)                       # Separator
    (\d{3})                         # Ostatnie trzy cyfry
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # Numer wewnetrzny
    )""", re.VERBOSE)


# Utworzenie wyrazenia regularnego dopasowujacego adres e-mail
emailRegex = re.compile(r"""(
    [a-zA-Z0-9._%+-]+               # Nazwa uzytkownika
    @                               # Znak @
    [a-zA-Z0-9.-]+                  # Nazwa domeny
    (\.[a-zA-Z]{2,4})               # Kropka i pozniej cokolwiek
    )""", re.VERBOSE)

# TODO: Wyszukanie dopasowan w schowku

# TODO: Skopiowanie wynikow do schowka
