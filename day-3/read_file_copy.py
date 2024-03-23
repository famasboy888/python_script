file=open('file.txt','r')
file_contents=file.read()
file.close()

print(file_contents)

file=open('new_file.txt', 'w')
file.write(file_contents)
file.close()