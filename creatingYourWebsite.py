# Program do dokonczenia, dopracowania
# Jest to program do tworzenia stron internetowych za pomoca prostych polecen


def structurewebsite(nazwastrony):
    website = open('Website.html', 'w')
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
    website.close()


print('Podaj nazwe swojej strony')
nazwa = input(':')
structurewebsite(nazwa)

# TODO: Zrobic dodawanie tekstu

# TODO: Zrobic dodawanie naglowkow

# TODO: Zrobic usuwanie

# TODO: Zrobic dodawanie zdjec

# TODO: Zrobic zmiane kolejnosci tekstu

# TODO: Zrobic dodawanie pogrubiania tekstu

# TODO: Zrobic dodawanie linkow

# TODO: Zrobic dodawanie list

# TODO: Dodac opcje CSS - opcjonalne
