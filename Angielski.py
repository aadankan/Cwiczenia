import os
import random

words = "C:/Users/aadan/Desktop/Angielski/1.Rodzina.txt"
Dwords = {}
if not os.path.isfile(words):
    f = open(words, "w")
    f.close()

f = open(words, "r")

listwords = f.readlines()
a = "".join(listwords)
a = a.split('\n')

for i in range(len(a)):
    Dwords[(a[i].split(' - '))[0]] = (a[i].split(' - '))[1]

f.close()


def menu():
    a = input("""
    Co chcesz zrobic?
    1. Dopisac slowka
    2. Sprawdzic sie
    3. Wyjscie
    Wpisz numer: """)
    if a == '1':
        dopisywanie()
    if a == '2':
        sprawdzian()
    if a == '3':
        quit()


def dopisywanie():
    while True:

        print('Napisz swoje slowo: (zostaw to pole puste aby zakonczyc program)')
        polishWord = input()
        if polishWord == '':
            menu()
        if polishWord in Dwords:
            print(Dwords[polishWord])
        else:
            print('Information not found about this word' + polishWord)
            print('What is this word?')
            engWord = input()
            if engWord == "":
                continue
            f = open(words, 'a')
            Dwords[polishWord] = engWord
            f.write('\n'+polishWord + ' - ' + engWord)
            f.close()
            print('Database completed')

def sprawdzian():
    f = open(words, 'r')
    print('Wpisz "quit" aby wyjsc')
    if len(f.readlines()) >= 10:
        e = 0
        f = 0
        g = {}
        while len(g) < 10:
            r = random.randint(0, len(listwords)-1)
            g[str(list(a)[r].split(' - ')[0])] = Dwords[a[r].split(' - ')[0]]

        for i in range(10):
            f += 1
            print(str(list(g)[i].split(' - ')[0]))
            b = input('Podaj slowo po angielsku: ')
            if b.lower() == g[str(list(g)[i].split(' - ')[0])]:
                e += 1
                print('Dobrze!')
            elif b == 'quit':
                menu()
            else:
                print('Zle, poprawna odpowiedz to: '+g[str(list(g)[i].split(' - ')[0])])

        print('Twoj wynik to: ' + str(e) + ' na ' + str(f))

    else:
        print('Za malo slowek')
    menu()


menu()
