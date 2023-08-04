#While loop :
'''
Syntax - initialization, i=10
         condition check in while loop and returns True or false,
         iteration --->> increment
'''
i=1
while(i<=10):
    print(i)
    i=i+1

print('************** while loop ******************')
i=1
while(i<=10):
    if(i%2==0):
        print('even',i)
    else:
        print('odd',i)
    i=i+1
print('************** End of while loop ******************')