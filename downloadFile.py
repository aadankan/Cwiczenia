import requests
res = requests.get('http://www.gutenberg.org/files/27062/27062-0.txt')
res.raise_for_status()
playFile = open('Romeo-i-Julia.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
