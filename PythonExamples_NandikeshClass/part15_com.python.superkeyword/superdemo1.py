#super() constructor can be used in 3 ways
# To invoke parent class methods
# To invoke parent class variables
# To invoke parent class constructor

# To invoke parent class methods
class A:
    def m1(self):
        print("This is method from A")

class B(A):
    def m2(self):
        print("This is method from B")
        super().m1()   #calling parent class method using super()
b=B()
b.m2()
