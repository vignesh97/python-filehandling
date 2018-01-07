file= open("example.txt",'r')
'''value=file.readline()
while len(value)!=0:
    print(len(value)-1)
    value=file.readline()'''

content  = file.readlines()
file.close()
for i in content:
    print(len(i)-1)

#print(content)
