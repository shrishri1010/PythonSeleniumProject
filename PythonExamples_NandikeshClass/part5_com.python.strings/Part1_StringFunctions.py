#length,index,concatenation,Repetation,index, uppercase, lowercase,isUpper,isLower,comparission
#delete, strip method, split.
#length --->>  lengthe of the string ---->>> returns the value in integer.

#Declaring or Creating Strings
#Approach 1
name="john"
print(name)

#Approach 2
name1=str("welcome")
print(name1)

a = "helloworld"
print(len(a))
print(max(a))   #Based on the ASCII value
print(min(a))   #Based on the ASCII value

b = "helloworld5435435"
print(len(b))

#concatenation
print(a+b)

#Repetation
print("hello"*3)

#index
a="learnpython"
print(a.index('t'))
print(a.upper())

x="TESTWORLD"
print(a.lower())

#isUpper,isLower   ------>>>>  returns boolean value
a="learnpython"
print(a.isupper())
print(a.islower())

##comparission ------>>>  Using ==  ---->> returns boolean value
a="learnpython"
b="learnpython"
print('if it is correct', a==b)

#Delete
'''
m="tesingtesting"
print(m)
del m
print('check delete condition', m)
'''
#Strip method   ---->>> removes the space.
s="   nandikesh    "
print(s.strip())

#Split method ----->>>  Once you split the string it converts into List.
k= "testhello"
print(k.split("he"))

k1= "test,hello"
print(k1.split(","))






