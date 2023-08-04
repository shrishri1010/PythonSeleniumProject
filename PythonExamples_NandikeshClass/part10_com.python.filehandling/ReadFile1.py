#Reading the data from the file
file=open("D:\\python\\test.txt",'r')
print(file.read())    #read entire content of file at once
#print(file.read(2))  # reads the two letters from file
file.close()

#Reading the data from the file
file=open("D:\\python\\test.txt",'r')
print(file.readlines())    #read entire content of file at once and prints it in array format
file.close()

#Reading the data of the first line
file=open("D:\\python\\test.txt",'r')
print(file.readline())    #read the first line
file.close()
