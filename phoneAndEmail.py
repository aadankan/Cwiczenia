#! python3
# phoneAndEmail.py-Wyszukuje numery telefonow i dresy e-mail w schowku.

import pyperclip, re

phoneRegex = re.compile(r"""(
    (\d{2}|(\d{2}))?                # Numer kierunkowy
    (\s|-|\.)?                      # Separator
    (\d{3})                         # Pierwsze trzy cyfry
    (\s|-|\.)                       # Separator
    (\d{2})                         # Dwie cyfy
    (\s|-|\.)                       # Separator
    (\d{2})                         # Ostatnie dwie cyfry
    )""", re.VERBOSE)


# Utworzenie wyrazenia regularnego dopasowujacego adres e-mail
emailRegex = re.compile(r"""(
    [a-zA-Z0-9._%+-]+               # Nazwa uzytkownika
    @                               # Znak @
    [a-zA-Z0-9.-]+                  # Nazwa domeny
    (\.[a-zA-Z]{2,4})               # Kropka i pozniej cokolwiek
    )""", re.VERBOSE)

# Wyszukanie dopasowan w schowku
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[4], groups[6], groups[8]])

    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Skopiowanie wynikow do schowka
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Skopiowano do schowka:')
    print('\n'.join(matches))
else:
    print('Nie znalezniono zadnego numeru telefonu lub adresu e-mail.')
