#Declaring variables inside the class
class MyClass:
    a,b=100,200    #class variables

    def add(self):    #instance method
       print(self.a+self.b)

    def multiplication(self):
       print(self.a*self.b)

mc=MyClass()
mc.add()
mc.multiplication()