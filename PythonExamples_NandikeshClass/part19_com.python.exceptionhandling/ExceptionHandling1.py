#a=10/0
#print(a)
'''
Exception is an abnormal condition
Exception is an event that disrupts the normal flow of the program
'''
try:
    a = 10 / 0
    print(a)
except ArithmeticError:
    print('exception has been caught')

try:
    b=10
    print(a)
except NameError:
    print('a is not declared')

try:
    a=[1,3,5]
    print(a[3])
except IndexError:
    print('index error has been caught')

'''
try:
    a = int(input('Enter value'))
    print(a/0)
except ZeroDivisionError:
    print('ZeroDivisionError error has been caught')
'''















