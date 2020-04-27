# Program do dokonczenia, dopracowania
# Jest to program do tworzenia stron internetowych za pomoca prostych polecen


def structurewebsite(nazwastrony):
    website = open('D:\Python\Ksiazka\Website.html', 'w')
    website.write("""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>
""" + str(nazwastrony) + """
</title>
</head>
<body>
</body>
</html>""")


print('Podaj nazwe swojej strony')
nazwa = input(':')
structurewebsite(nazwa)




