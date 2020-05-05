#! python3
# countdown.py-Prosty skrypt odliczajacy czas

import time
import subprocess

timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft -= 1

# Po odliczeniu okreslonego czasu bedzie odtworzony plik dzwiekowy
subprocess.Popen(['start', 'alarm.wav'], shell=True)

