'''
Range Function in Python -
range() method returns an immutable sequence of numbers between the given start integer to the stop integer.
'''

#Synatx of Range()
'''
range(stop)
range(start, stop)
range(start, stop, step/increment)
'''

#range(stop)
result = range(10)
print(result)
print(tuple(result))
print(list(result))

#range(start, stop)
print(list(range(1, 10)))
print(list(range(5, 10)))
print(tuple(range(3,10)))

#range(start, stop, step/increment)
start = 2
stop = 16
step = 2

print(list(range(start, stop, step)))
start = 2
stop = 20
step = 3
print(list(range(start, stop, step)))

print("************************** step1 **********************************")
a=[2,7,4,3,8,11]
#print(len(a))
for i in range(0,len(a),2):
    print(a[i])

start = 2
stop = -14
step = -2
print(list(range(start, stop, step)))
print("*************************shrikanth1***********************************")
for m in range(1,10):
    print(m)
print("***********************shrikanth2*************************************")
for m in range(1,10,2):
    print(m)

#a = [10,20,30,40]
#//print(len(a))
result1 = range(3)
print(list(result1))
