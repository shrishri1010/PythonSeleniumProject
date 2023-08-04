class Parent1:
    father=10
    def m1(self):
        print('parent1 class')

class Parent2:
    mother=50
    def m2(self):
        print('parent2 class')

class child(Parent1,Parent2):
    def m3(self):
        print('child class')
c=child()
c.m1()
print(c.father)
c.m2()
print(c.mother)
c.m3()
