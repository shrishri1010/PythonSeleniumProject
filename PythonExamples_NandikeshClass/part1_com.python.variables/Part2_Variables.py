'''
1.	Local variables   -->> Scope of the variables within the function.
2.	Global variables  -->> Scope of the variables within the function and also outside the function.
'''
#local variables a and b
def addition(self):
    a=10          #int type
    b=20.5        #float type
    print(a+b)

def multiplication():
    m=30
    n=20
    print(m*n)

def substraction():
    x=10
    y=5
    print(x-y)
    print(x)

addition(10)
substraction()
multiplication()


#Global Variables -
sum=0
def summation(a,b):
    sum=a+b
    print('inside the function  ------ ', sum)

summation(120,100)
print('outside the function',sum)
print('************************')


