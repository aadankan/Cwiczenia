#! python3
# bulletPointAdder.py-at the beginning of each line of text found
# Adds asterisks to the list in the clipboard

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):     # Iteracja przez wszystkie indeksy listy "lines"
    lines[i] = '* ' + lines[i]  # Dodanie gwiazdki do każdego ciągu tekstowego na liście "lines"

text = '\n'.join(lines)
pyperclip.copy(text)
