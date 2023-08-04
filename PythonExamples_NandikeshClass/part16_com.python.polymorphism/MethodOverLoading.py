#Overoading methods

class Bird:
    def fly(self,name=None):
        if name=="parrot":
            print("can fly")
        if name=="penguine":
            print("cannot fly")
        if name is None:
            print("No input")

obj=Bird()
obj.fly("parrot")

