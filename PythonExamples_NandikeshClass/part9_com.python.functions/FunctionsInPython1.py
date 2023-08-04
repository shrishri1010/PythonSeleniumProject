#Functions - is nothing but a block of code it performs the operation and this can be called anywhere inside the class.

'''
def greater(a,b):
    if(a>b):
        print('a is greater')
    else:
        print('b is greater')
greater(15,20)
'''

#Return keyword in python
def greater(a,b):
    if(a>b):
        print('a is greater')
        return a
    else:
        print('b is greater')
        return b
test=greater(20,30)
print(test)

def addition(a,b):
    return a+b
test1=addition(20,30)
print(test1)

def addition(a,b,c):
    return a+b+c
print(addition(3,5,7))

def sum(a,b):
    print(a)
    print(b)
    return a*b
print(sum(35,85))




