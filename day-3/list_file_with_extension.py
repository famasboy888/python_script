import os

user_input_dir=input('List files with in directory: ').strip()
user_input_ext=input('What extention (.py, .exe, .png): ').strip()

if os.path.exists(user_input_dir):
    list_files=os.listdir(user_input_dir)
    cnt=0
    for file in list_files:
        if file.endswith(user_input_ext):
            print(file)
            cnt += 1
    print(f'{cnt} file(s) found.')
else:
    print('Path does not exists!')