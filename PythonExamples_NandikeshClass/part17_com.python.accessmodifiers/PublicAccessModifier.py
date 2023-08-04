class Test:
    m=15
    def __init__(self):
        self.a=20

    def m1(self):
        print("statement from method")
t=Test()   #object instantiation or Object creation
t.m1()
print(t.a)
print(t.m)