#Dictionary ------>> stores the data in Key and value pair in flower bracket

#Syntax -  DictName = {'key':'Value'}
'''
Notes --
1.We can Change/modify the dictionary. so we are calling dictioanry is Mutable(Alter/Modify).
2.We can add the data in dictioanry.
3.We can delete the key-value using dictionary.
4.Dictioanry contains the values in key-value pair and it should be inside the flower bracket.
'''

#Declaring single values
a={'Name':'Nandikesh'}
print(a)

#declaring multiple values
x={'Name':'Nandikesh', 'email':'test@gmail.com'}
print(len(x))
print(x)
print(type(a))

print("*********************cppppp*****")
#Retrieving the elements from the dictionary
print(x['Name'])

#Modify/Change the elements into the dictionary
x['Name']='Hegde'
print(x)

#Adding the elements into the dictionary
x['Address']='mangalore'
print(x)

#Deleting the elements from the dictionary
del x['Address']
print(x)

dict1 = {}
print(len(dict1))

#prints the value of the key
p={'Name':'Nandikesh', 'email':'test@gmail.com'}
print(p['Name'])
print(p['email'])
print(f"display name and email {p['Name']},{p['email']}")

#Built in Functions Dictionary
#keys(), values(), items()
dict2={'Name':'Nandikesh', 'email':'test@gmail.com', 'mobileNo':'9655856289'}

print(dict2.keys())
print(dict2.values())
print(dict2.items())
print(len(dict2))   #length of the dictionary

print('********************************')
dt='qwe'
for x in dt:
    print(x)





