
numbers = [1, 2, 3]
file = open("numbers.txt", "a")
for i in numbers:
     file.write(str(i) + "\n")
file.close()


file=open("test.txt",'w')
file.write("Line 1\n")
file.write("Line 2\n")
file.write("Line 3\n")
file.write("Line 4\n")
file.close()
