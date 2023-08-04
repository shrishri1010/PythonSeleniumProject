#Append method  ---- we need to open the file in 'a' mode
a=open("D:\\python\\test.txt",'a')
a.write("\n i am in delhi")
a.close()
a=open("D:\\python\\test.txt",'r')
print(a.read())
print("*******************************************************************")

#Looping through the data using for loop
file=open("D:\\python\\test.txt",'r')
for line in file:
    print(line)
file.close()