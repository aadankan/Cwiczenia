import pyperclip

a = pyperclip.paste()
a = str(a)
a = a.replace("\r\n", "&")
c = []
d = ""
a = a.split("&")
for i in range(len(a)):
    c.append(a[i].split(" - ")[1] + " - " + a[i].split(" - ")[0])

for i in range(len(a)):
    d = d.__add__(c[i] + "\r\n")

pyperclip.copy(d)
