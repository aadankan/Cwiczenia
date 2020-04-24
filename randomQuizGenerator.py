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
    # TODO Utworzenie plików quizu i odpowiedzi na pytania

    # TODO Zapis nagłówka quizu

    # TODO Losowe ustalenie kolejności stanów

    # TODO Iteracja 50 stanów i utworzenie pytania dotyczącego każdego z nich.
