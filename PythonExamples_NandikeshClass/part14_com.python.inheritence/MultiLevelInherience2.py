class Parent:
    a=10
    def m1(self):
        print('parent class')

class child(Parent):
    def m2(self):
        print('child class')

class subchild(child):
    def m3(self):
        print('subchild class')

print('parent class properties')
p=Parent()
p.m1()

print('child class properties')
c=child()
c.m1()
c.m2()

print('subchild class properties')
sc=subchild()
sc.m1()
sc.m2()
sc.m3()

