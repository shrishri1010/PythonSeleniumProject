 #Using for loop
'''
for(variable name) in <string/list>:
		statement;
'''

a='hello'  #a[0]=h,a[1]=e,a[2]=l,a[3]=l,a[4]=0
for x in a:
    print(x)
print('********************************')

a=[10,20,30,40,50]
for x in a:
    print(x)
print('********************************')

a=(2,7,4,3,8,'test')
for x in a:
    print(x)

print('********************************')
a=(2,7,4,3,8,15)
for m in a:
    if(m%2==0):
        print('even number',m)
    else:
        print('odd number',m)
print('********************************')

a=[2,7,4,3]
b=[2,5,6,10]

for m in a:
    for n in b:
        print(m+n)
















