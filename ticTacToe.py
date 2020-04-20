theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
theBoard2 = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

# Tworzenie planszy


def printboard(board):
    print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
    print('-+-+-')
    print(board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R'])
    print('-+-+-')
    print(board['low-L']+'|'+board['low-M']+'|'+board['low-R'])

# Warunki wygranej krzyzyka


def xwin():
    f = 'X'
    if theBoard['top-L'] == f and theBoard['top-M'] == f and theBoard['top-R'] == f:
        return "koniec"
    elif theBoard['mid-L'] == f and theBoard['mid-M'] == f and theBoard['mid-R'] == f:
        return "koniec"
    elif theBoard['low-L'] == f and theBoard['low-M'] == f and theBoard['low-R'] == f:
        return "koniec"
    elif theBoard['top-L'] == f and theBoard['mid-L'] == f and theBoard['low-L'] == f:
        return "koniec"
    elif theBoard['low-M'] == f and theBoard['mid-M'] == f and theBoard['top-M'] == f:
        return "koniec"
    elif theBoard['low-R'] == f and theBoard['mid-R'] == f and theBoard['top-R'] == f:
        return "koniec"
    elif theBoard['low-R'] == f and theBoard['mid-M'] == f and theBoard['top-L'] == f:
        return "koniec"
    elif theBoard['low-L'] == f and theBoard['mid-M'] == f and theBoard['top-R'] == f:
        return "koniec"
    else:
        pass

# Warunki wygranej kolka


def kwin():
    f = '0'
    if theBoard['top-L'] == f and theBoard['top-M'] == f and theBoard['top-R'] == f:
        return "koniec"
    elif theBoard['mid-L'] == f and theBoard['mid-M'] == f and theBoard['mid-R'] == f:
        return "koniec"
    elif theBoard['low-L'] == f and theBoard['low-M'] == f and theBoard['low-R'] == f:
        return "koniec"
    elif theBoard['top-L'] == f and theBoard['mid-L'] == f and theBoard['low-L'] == f:
        return "koniec"
    elif theBoard['low-M'] == f and theBoard['mid-M'] == f and theBoard['top-M'] == f:
        return "koniec"
    elif theBoard['low-R'] == f and theBoard['mid-R'] == f and theBoard['top-R'] == f:
        return "koniec"
    elif theBoard['low-R'] == f and theBoard['mid-M'] == f and theBoard['top-L'] == f:
        return "koniec"
    elif theBoard['low-L'] == f and theBoard['mid-M'] == f and theBoard['top-R'] == f:
        return "koniec"
    else:
        pass

# Zmiana tury


turn = 'X'
while True:
    a = 0
    for i in theBoard:
        if a == 8:
            printboard(theBoard)
            print("Remis!")
            print("-"*100)
            theBoard = theBoard2.copy()
            a = 0
        elif theBoard[i] != " ":
            a += 1
    printboard(theBoard)
    print('Ruch gracza ' + turn + '. W którym polu stawiasz znak?')
    move = input()
    if theBoard[move] == " ":
        theBoard[move] = turn
    else:
        print('To pole jest zajete wybierz inne')
        continue
    if turn == 'X':
        if xwin() == "koniec":
            print("Gracz X wygrywa!")
            printboard(theBoard)
            print("-" * 100)
            theBoard = theBoard2.copy()
        turn = '0'
    else:
        if kwin() == "koniec":
            print("Gracz 0 wygrywa!")
            printboard(theBoard)
            print("-"*100)
            theBoard = theBoard2.copy()
        turn = 'X'

printboard(theBoard)
