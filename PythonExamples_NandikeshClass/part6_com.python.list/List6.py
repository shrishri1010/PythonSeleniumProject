list1 = [2,4,6,8,9,10,4]
list1.append(90)        #append function
print(list1)

#count function
print(list1.count(4))

#extend function
list2 = [99,100]
list1.extend(list2)
print(list1)

#index function
print(list1.index(99))

#insert function
print(list1.insert(1,100))  # index 1 position it adds 100 value.
print(list1)

#pop function
print(list1.pop(3))  # returns the value based on the index
print(list1)

#remove function
list1.remove(99)  # removes the value 99
print(list1)

#reverse function
list1.reverse()  # reverse
print(list1)

#sort function
list1.sort()  # sorting the list in sequence
print(list1)




