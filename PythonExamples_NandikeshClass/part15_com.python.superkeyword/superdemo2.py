#super() constructor can be used in 3 ways
# To invoke parent class methods
# To invoke parent class variables
# To invoke parent class constructor

# To invoke parent class variables

a,b=10,15  #Global variables
class A:
    a,b=10,20  #Class variables

class B(A):
    a,b=100,200   #Child Class variables
    def m1(self,a,b):
        print(a+b)  #local variables
        print(self.a+self.b)  #Child class variables --- self is pointing to current class
        print(super().a+super().b) #parent class variables
        print(globals()['a']+globals()['b'])

obj=B()
obj.m1(5,10)
