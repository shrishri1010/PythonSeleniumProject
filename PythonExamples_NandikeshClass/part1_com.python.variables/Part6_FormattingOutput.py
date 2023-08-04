name="shri"
age=40
sal=12000.45

#Approach1
print(name,age,sal)

#Approach2
print("Name is:", name)
print("Age is:", age)
print("Sal is:", sal)

#Approach3 : Using % operator. Here datatype is important
print("Name:%s Age:%d Salary:%g"%(name,age,sal))

#Approach4 : Using {} Here value is important
print("Name:{} Age:{} Salary:{}".format(name,age,sal))

#Approach5 : Using {} and index wise. index starts from zero
print("Name:{0} Age:{1} Salary:{2}".format(name,age,sal))