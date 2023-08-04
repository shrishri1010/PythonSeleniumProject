#How to call current class method in another method
class MyClass:

    def m1(self):
        print("this is m1 method")
        self.m2(25)

    def m2(self,a):
        print("this is m2 method", a)
c1=MyClass()
c1.m1()
c1.m2(45)