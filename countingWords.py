import pyperclip

a = pyperclip.paste()
b = a
a = a.split(' ')
c = b.split('.' or '!' or '?')
print("Tekst ten ma: " + str(len(c)-1) + " zdan " + str(len(a)) + " slow i " + str(len(b)) + ' znakow')
