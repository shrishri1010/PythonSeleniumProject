'''
List
1. We can modify the list. so we are calling list is Mutable(Alter/Modify).
2. List is having sequence of mutable of values: ex - ['test', 'hello']
3.List contains the values and it should be inside the square bracket.
'''

# Append the value in List
list = [10,20,30,59,70,45]
list1 = [10,20,30]
print('Before append', list)
print(list[-1])
list.append(40)
print('After append',list)

x=list[2]
print('x is',x)
print(list[-1])
print(type(list))
print('list is', list[-1])
print(30 in list)
print(33 not in list)
print('slicing', list[1:2])

#sum
print(sum(list+list1))
print(min(list))
print(max(list))
print(len(list))

#Slicing list
print(list[0:5])
print(list[2:4])
print(list[:4])   #[10, 20, 30, 59]
print(list[2:])   #[30, 59, 70, 45, 40]

'''
+ and * operations in list
'''
list1 = [11,22]
list2 = [10,20]
list3 = list1+list2
print(list3)

list4= [1,2,3,4]
list5 = list4 * 3
print(list5)










