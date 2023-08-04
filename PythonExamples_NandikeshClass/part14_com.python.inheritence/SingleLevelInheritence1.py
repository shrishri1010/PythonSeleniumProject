#Single Level Inheritence
class Parent:
    a=10
    def m1(self):
        print('inside parent class method')
class child(Parent):         #Inheritence
    def m2(self):
        print('inside child class method')
p=Parent()    #parent clas  instantiation
p.m1()
#p.m2()

c=child()    #child classs instantiation
c.m1()
c.m2()
