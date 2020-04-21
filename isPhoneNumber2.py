import re

phoneNumRegex = re.compile(r'\d\d\d \d\d\d \d\d\d')
mo = phoneNumRegex.search('Moj numer telefonu to 413 334 345')
print('Znaleziono numer telefonu: ' + mo.group())
