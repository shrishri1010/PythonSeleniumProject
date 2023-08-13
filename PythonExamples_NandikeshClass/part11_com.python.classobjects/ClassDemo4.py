#Local variables, Class variables and Global Variables
i,j=15,25  #Global Variables

class Myclass:
    a,b=10,20   #Class variables

    def add(self,x,y):            # x and y are Local variables are belongs to method only
        print(x+y)                # accessing local variables
        print(self.a + self.b)    # accessing class variables using "self" key
        print(i+j)                # accessing global variables directly

mc=Myclass()
mc.add(15,10)



