
#abc is Abstract baseclass. From this baseclass importing ABC module and abstractmethod
from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass

class B(A):
    def m1(self):
        print('this is display method1')

class C(B):
    def m2(self):
        print('this is display method2')
cobj=C()
cobj.m1()
cobj.m2()















