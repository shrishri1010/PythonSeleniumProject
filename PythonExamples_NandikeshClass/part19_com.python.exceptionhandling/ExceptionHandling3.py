##Multiple try - Except block
from typing import TypeVar

try:
    #a = int(input('Enter value'))
    #print(a/0)
    a=[3,5,7]
    print(a[2])
except ZeroDivisionError as e:
    print(type(e).__name__)
except TypeError as e:
    print(type(e).__name__)
except NameError as e:
    print(type(e).__name__)
else:
    print("Entered into else block")

try:
    a = int(input('Enter value'))
    print(a/0)
    a=[3,5,7]
    print(a[7]);
except Exception as e:
    print(type(e).__name__)
finally:
    print("Entered into finally block")


'''
x = int(input('Enter a number: '))
try:
    while(x>10):
    print('You have entered an even number.')
    else:
    print ('You have entered an odd number.')
except Exception as e:
    print(type(e).__name__)
'''