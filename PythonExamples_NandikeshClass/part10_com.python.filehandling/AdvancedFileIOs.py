#a=open("D:\\python\\test.txt",'r')
#print(a.mode())
#print(a.readlines())  # It will return the output in list format
#print(a.readlines()[1])
#print(len(a.readlines()))

#Reading the data from the file
'''
a=open("D:\\python\\test.txt",'r')
print(a.readlines())
a=open("D:\\python\\test.txt",'r')
for m in a.readlines():
    if "test" in m:
        print("present")
    else:
        print("not present")
'''

#Overwrite method  ----- Open file  for writting
'''
a=open("D:\\python\\test.txt",'w')
a.write('shrikanth testing hellowrold i m in mangalore\n')
a.write('shrikanth testing hellowrold i m in mangalore\n')
a.close()
a=open("D:\\python\\test.txt",'r')
print(a.read())
'''

#replace function
fileinput = open("D:\\python\\test.txt", "r")
#read file contents to string
data = fileinput.read()
print(data)
#replace all occurrences of the required string
data = data.replace('delhi', 'python')
#close the input file
fileinput.close()
print(data)





