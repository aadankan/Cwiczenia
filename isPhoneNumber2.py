import re, pyperclip

phoneNumRegex1 = re.compile(r'\d\d\d \d\d\d \d\d\d')
phoneNumRegex2 = re.compile(r'\d\d \d\d\d \d\d \d\d')
mo1 = phoneNumRegex1.findall(pyperclip.paste())
mo2 = phoneNumRegex2.findall(pyperclip.paste())
if mo1 != None:
    for i in range(len(mo1)):
        print('Znaleziono numer telefonu: ' + mo1[i])

if mo2 != None:
    for i in range(len(mo2)):
        print('Znaleziono numer telefonu: ' + mo2[i])

else:
    print('Nie znaleziono numeru')