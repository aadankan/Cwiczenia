import re, pyperclip

phoneNumRegex1 = re.compile(r'\d\d\d \d\d\d \d\d\d')
phoneNumRegex2 = re.compile(r'\d\d \d\d\d \d\d \d\d')
mo1 = phoneNumRegex1.search(pyperclip.paste())
mo2 = phoneNumRegex2.search(pyperclip.paste())
if mo1 != None:
    print('Znaleziono numer telefonu: ' + mo1.group())
elif mo2 != None:
    print('Znaleziono numer telefonu: ' + mo2.group())
else:
    print('Nie znaleziono numeru')