#Creating basic class and object which include methods
class MyClass:
    def myfunction(self):
        pass
    def display(self,name):  #parameterised method
        print("Name is :", name)

mc=MyClass()  # creating object of the class ------->>> Instantiation  ---->>> mc is reference variable
mc.myfunction()
mc.display("shrikanth")

#out put is ---->> Name is : shrikanth