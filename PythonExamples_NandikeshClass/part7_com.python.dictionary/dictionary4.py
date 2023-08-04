from builtins import dict, print

friends={'Name':'Nandikesh', 'email':'test@gmail.com'}

#popitem() Returns randomly select item from dictionary and also remove
print(friends.popitem())
print(friends)

#clear() Delete everything from dictionary
print(friends.clear())


dictset={'Name':'Nandikesh', 'email':'test@gmail.com'}
print(dictset.keys())     #keys method returns all the keys
print(dictset.values())   #values method returns all the values
#print(dict2.items())


#get(key) function will Return a value of key, If key is not found it returns None,
print(dictset.get('email'))

#pop(key) Remove the items from dictionary
print(dictset.pop('Name'))

print(dictset)