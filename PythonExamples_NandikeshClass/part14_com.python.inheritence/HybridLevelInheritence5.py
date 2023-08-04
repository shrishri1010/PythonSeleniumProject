class A:
    __a=10   #protected
    def m1(self):
        print('A class')
class B(A):
    def m2(self):
        print('B class')
class C(A):
    def m3(self):
        print('C class')
class D(C):
    def m4(self):
        print('D class')
c=C()
#print(c.__a)
c.m1()
c.m3()
d=D()
d.m1()
d.m3()
d.m4()