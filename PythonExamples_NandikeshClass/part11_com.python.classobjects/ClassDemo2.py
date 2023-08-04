#Instance method and static method

class MyClass:
    def testmethod1(self):    #instance method
       print("instance method")

    @staticmethod
    def testmethod2():      #static method   ----->> By default,it does not take parameters.
       print("static method")

mc=MyClass()
mc.testmethod1()  #instance method can be accessed by creating the object.

MyClass.testmethod2()