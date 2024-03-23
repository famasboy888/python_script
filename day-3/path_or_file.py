import os

user_input=input('Enter path or file: ')

if os.path.exists(user_input):
    if os.path.isdir(user_input):
        print(f'{user_input} is a directory.')
    elif os.path.isfile(user_input):
        print(f'{user_input} is a file.')
    else:
        print('Invalid input')
else:
    print('Directory or file does not exists!')