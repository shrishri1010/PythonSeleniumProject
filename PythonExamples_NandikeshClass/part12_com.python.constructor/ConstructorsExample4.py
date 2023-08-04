#constructor with arguments
class MyClass:
    name="shrikanth"
    #create constructor
    def __init__(self,name):
        print(name)           #constructor argument is local variables
        print(self.name)      #represents class variables
c1=MyClass("pavan")
