#! python3
# pw.py - Dangerous password manager program


import sys, pyperclip

PASSWORDS = {'email': 'password1',
             'blog': 'password2',
             'luggage': 'password3',
             'gmail': 'password4'}
if len(sys.argv) < 2:
    print('Using: python pw.py [account] - copying the password of the specified account')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password to account is ' + account + 'copied to the clipboard.')
else:
    print('Does not exist account with name ' + account + '.')
