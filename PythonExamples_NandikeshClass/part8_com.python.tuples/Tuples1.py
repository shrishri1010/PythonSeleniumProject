'''
Tuples
1. Having sequence of Immutable(Cannot modify) values
2.Holds values with different data types and decalring within parenthesis ()
'''

'''
Tuple -
1.we can't add the values.
2.We can't change the values.
3.We can't delete the values.
'''

a=(10,20,30,40,"test",20.12)
print(type(a))
print(a[:])
#print(a.append(25))
#a[2]=50
#print(a)
#del a[2]

#Functions in Tuple

m=(10,20,30,40,"test",20.12)
print(len(m))
n=(10,10,20,30,40,20.12)
print(sum(n))
print(max(n))
print(min(n))
print(n.count(10))
print(n.count(40))

#Lets learn comparision operators  ----->>>  ==,>,< ,!=  (Returns boolean values)
p=(10,20,30)
q=(10,30,30)

print(p[1]==q[1])
print(p[1]<q[1])
print(p[1]>q[1])
print(p[1]!=q[1])


blogName = ["how","to","do","in","java"]
print(id(blogName[1]))
print(id(blogName[2]))

blogName1 = ["ab","zb","b","d","e"]
print(id(blogName1[0]))
print(id(blogName1[1]))
print(max(blogName1))
print(min(blogName1))

#Slicing in Tuples
t1 = (1,15,90,30,45,80)
print(t1[0:4])
print(t1[:4])
print(t1[0:])
print(t1[2:])

#in and not in operator in tuples
tuple = (1,15,90,30,45,80)
print(100 in tuple)
print(100 not in tuple)







