##Multiple try - Except block

try:
    #a = int(input('Enter value'))
    #print(a/0)
    a=[3,5,7]
    print(a[3])
except ZeroDivisionError as e:
    print(type(e).__name__)
except IndexError as e:
    print(type(e).__name__)
except Exception as e:
    print(type(e).__name__)

'''
try:
    #a = int(input('Enter value'))
    #print(a/0)
    a=[3,5,7]
    print(a[7]);
except Exception as e:
    print(type(e).__name__)
'''

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