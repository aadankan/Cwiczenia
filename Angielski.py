import os
import random

words = "C:/Users/adik/Desktop/words.txt"
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
    1. dopisac slowka
    2. sprawdzic sie
    Wpisz numer: """)
    if a == '1':
        dopisywanie()
    if a == '2':
        sprawdzian()


def dopisywanie():
    while True:

        print('Write yours word: (leave this field to end this program)')
        polishWord = input()
        if polishWord == '':
            break
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
    pass



menu()
