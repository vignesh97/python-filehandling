file= open("example.txt",'r')
value=file.readline()
while len(value)!=0:
    print(len(value))
    value=file.readline()
file.close()
#print(content)
