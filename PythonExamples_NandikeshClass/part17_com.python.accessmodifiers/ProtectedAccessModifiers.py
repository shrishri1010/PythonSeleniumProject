'''
Protected --- The members of a class that are declared protected are only accessible to a class derived from it.
            #Data members of a class are declared protected by adding a single underscore ‘_’ symbol before the
            data member of that class.
'''
class Test:
    __test=100
    _weare='own world'
    def __init__(self, name, sal):
        self._name = name   # protected attribute
        self._sal = sal     # protected attribute
    def method2(self):
        print('testing automation')
        print(hrEmp.__test)
t=Test("captain",1000)
print(t._name)
print(t._sal)
class Nandikesh(Test):  #Derived class
    # member function task
    def task(self):
        print("We manage Employees")
hrEmp = Nandikesh("manish", 5000)
print(hrEmp._name)
print(hrEmp._sal)
hrEmp.task()
hrEmp.method2()
print(hrEmp._weare)




