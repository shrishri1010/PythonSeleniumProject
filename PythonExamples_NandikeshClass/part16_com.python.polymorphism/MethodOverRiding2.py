#Polymorphism
#1.Method over riding
#a.Over riding a variable
#b.Over riding a method

# b.Over riding a method
class A:
    a=10
    def methodA(self):
        print('A class')

class B(A):
    def methodA(self):
        print('B class')
obj1=A()
obj1.methodA()

obj2=B()
obj2.methodA()





