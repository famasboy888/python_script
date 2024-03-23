import json

#Author: Kyle Yap

file=open('data.json','r')
data=json.load(file)
print(data.get('result')[1].get('name').get('first'))


file.close()

