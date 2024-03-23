import csv

#Author: Kyle Yap

csv_file=open('test.csv','r')
data=csv.reader(csv_file,delimiter=',')

header=next(data)
print(header)
new_list=[]

for i in data:
   print(i)
   if i[5] == 'worker':
      new_list.append(i)

print('=================NEW LIST==================')
for t in new_list:
   print(t)

csv_file.close()