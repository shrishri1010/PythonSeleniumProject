#Using __del__ method
class MyClass:
    #syntax of parameterised constructor
    def __del__(self):
        print("Destroyed")
c1 = MyClass();
c2 = MyClass();

del c1


