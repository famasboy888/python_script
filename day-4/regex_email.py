import re

#Author: Kyle Yap

pat=r'^[\w\-\.]+@([\w-]+\.)+[\w-]{2,}$'
email_list=["valid@gmail.com","invalid*&^@gmmail","yoyoy+8080@hoho.co", "hellowolrd.world@hello.com"]

regex_obj=re.compile(pat)

for email in email_list:
    if regex_obj.match(email):
        print(f'{email} <== is valid')