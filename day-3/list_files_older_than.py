import os
import datetime

user_input=input('Enter path or file: ')
if os.path.exists(user_input):
    today=datetime.datetime.now()
    for file in os.listdir(user_input):
        full_file_path=os.path.join(user_input,file)
        if(os.path.isfile(full_file_path)):
            file_create_date=datetime.datetime.fromtimestamp(os.path.getctime(full_file_path))
            if (today-file_create_date).days > 3:
                print(file, (today-file_create_date).days)
else:
    print('Path does not exists!')