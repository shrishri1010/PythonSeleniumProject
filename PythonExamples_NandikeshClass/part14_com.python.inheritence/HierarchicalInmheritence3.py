class Parent:
    a=10
    def m1(self):
        print('parent class')
class childA(Parent):
    def m2(self):
        print('childA class')
class childB(Parent):
    def m3(self):
        print('childB class')
print('parent class properties')
p=Parent()
p.m1()

print('child A class properties')
c=childA()
c.m1()
c.m2()

print('child B class properties')
sc=childB()
sc.m1()
sc.m3()

