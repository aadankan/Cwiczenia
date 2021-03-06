#! python3
# randomQuizGenerator.py - tworzy quiz wraz z pytaniami i odpowiedziami
# ułożonymi w losowej kolejości wraz z odpowiedziami.

import random

# To są dane quizu. Klucze to nazwy stanow, natomiast wartosci to ich stolice.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Joneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
            'Kalifornia': 'Sacramento', 'Kolorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
            'Floryda': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaje': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
            'Kentucky': 'Frankfort', 'Luizjana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
            'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'Nowy Meksyk': 'Santa Fe', 'Nowy Jork': 'Albany',
            'Karolina Północna': 'Releigh', 'Dakota Północna': 'Bismarck', 'Ohio': 'Columbus',
            'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pensylwania': 'Harrisburg', 'Rhode Island': 'Providence',
            'Karolina Południowa': 'Columbia', 'Dakota Południowa': 'Pierre', 'Tennessee': 'Nashville',
            'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Wirginia': 'Richmond',
            'Waszyngton': 'Olympia', 'Wirginia Zachodnia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Wygenerowanie 35 plików quizu
for quizNUm in range(35):
    # Utworzenie plików quizu i odpowiedzi na pytania
    quizFile = open('capitalsquiz%s.txt' % (quizNUm + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNUm + 1), 'w')

    # Zapis nagłówka quizu
    quizFile.write('Imię i nazwisko: \n\nData:\n\nKlasa:\n\n')
    quizFile.write((' ' * 20)+ 'Quiz stolic stanów (Quiz %s)' % (quizNUm + 1))
    quizFile.write('\n\n')

    # Losowe ustalenie kolejności stanów
    states = list(capitals.keys())
    random.shuffle(states)

    # Iteracja 50 stanów i utworzenie pytania dotyczącego każdego z nich.
    for questionNum in range(50):
        # Przygotowanie prawidłowych i nieprawidłowych odpowiedzi.
        correctAnswers = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswers)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswers]
        random.shuffle(answerOptions)

        # Zapis pytania i odpowiedzi w pliku quizu
        quizFile.write('%s. Co jest stolicą stanu %s?\n' % (questionNum + 1, states[questionNum]))

        for i in range(4):
            quizFile.write('   %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # Zapis odpowiedzi w pliku
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswers)]))
quizFile.close()
answerKeyFile.close()
