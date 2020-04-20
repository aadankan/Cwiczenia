words = {}

while True:
    print('Write yours word: (leave this field to end this program)')
    polishWord = input()
    if polishWord == '':
        break

    if polishWord in words:
        print(words[polishWord])
    else:
        print('Information not found about this word' + polishWord)
        print('What is this word?')
        engWord = input()
        words[polishWord] = engWord
        print('Database completed')