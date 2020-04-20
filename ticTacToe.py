theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
theBoard2 = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

# Tworzenie planszy
def printBoard(board):
    print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
    print('-+-+-')
    print(board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R'])
    print('-+-+-')
    print(board['low-L']+'|'+board['low-M']+'|'+board['low-R'])

# Warunki wygranej krzyzyka
def xWin():
    f = 'X'
    if theBoard['top-L'] == f and theBoard['top-M'] == f and theBoard['top-R'] == f:
        return  True
    elif theBoard['mid-L'] == f and theBoard['mid-M'] == f and theBoard['mid-R'] == f:
        return  True
    elif theBoard['low-L'] == f and theBoard['low-M'] == f and theBoard['low-R'] == f:
        return  True
    elif theBoard['top-L'] == f and theBoard['mid-L'] == f and theBoard['low-L'] == f:
        return  True
    elif theBoard['low-M'] == f and theBoard['mid-M'] == f and theBoard['top-M'] == f:
        return  True
    elif theBoard['low-R'] == f and theBoard['mid-R'] == f and theBoard['top-R'] == f:
        return True
    elif theBoard['low-R'] == f and theBoard['mid-M'] == f and theBoard['top-L'] == f:
        return True
    elif theBoard['low-L'] == f and theBoard['mid-M'] == f and theBoard['top-R'] == f:
        return True
    else:
        return False

# Warunki wygranej kolka
def kWin():
    f = '0'
    if theBoard['top-L'] == f and theBoard['top-M'] == f and theBoard['top-R'] == f:
        return  True
    elif theBoard['mid-L'] == f and theBoard['mid-M'] == f and theBoard['mid-R'] == f:
        return  True
    elif theBoard['low-L'] == f and theBoard['low-M'] == f and theBoard['low-R'] == f:
        return  True
    elif theBoard['top-L'] == f and theBoard['mid-L'] == f and theBoard['low-L'] == f:
        return  True
    elif theBoard['low-M'] == f and theBoard['mid-M'] == f and theBoard['top-M'] == f:
        return  True
    elif theBoard['low-R'] == f and theBoard['mid-R'] == f and theBoard['top-R'] == f:
        return True
    elif theBoard['low-R'] == f and theBoard['mid-M'] == f and theBoard['top-L'] == f:
        return True
    elif theBoard['low-L'] == f and theBoard['mid-M'] == f and theBoard['top-R'] == f:
        return True
    else:
        return False

# Zmiana tury
turn = 'X'
while True:
    printBoard(theBoard)
    print('Ruch gracza ' + turn + '. W którym polu stawiasz znak?')
    move = input()
    if theBoard[move] == " ":
        theBoard[move] = turn
    else:
        print('To pole jest zajete wybierz inne')
        continue
    if turn == 'X':
        if xWin() == True:
            print("Gracz X wygrywa!")
            printBoard(theBoard)
            print("-" * 100)
            theBoard = theBoard2.copy()
        turn = '0'
    else:
        if kWin() == True:
            print("Gracz 0 wygrywa!")
            printBoard(theBoard)
            print("-"*100)
            theBoard = theBoard2.copy()
        turn = 'X'


printBoard(theBoard)


