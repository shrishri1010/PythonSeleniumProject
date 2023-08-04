#Creating multiple objects for single class or one class
class Myclass:
    a,b=10,20   #Class variables

    def add(self,x,y):            # x and y are Local variables are belongs to method only
        print(x+y)                # accessing local variables
        print(self.a + self.b)    # accessing class variables using "self" key

#Creaing multiple objects for single class
mc1=Myclass()
mc1.add(15,10)

mc2=Myclass()
mc2.add(15,10)





