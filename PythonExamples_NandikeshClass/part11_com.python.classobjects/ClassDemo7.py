#Checking memory locations of objects
class Myclass:
    def display(self):
        pass

c1=Myclass()
c2=Myclass()
c3=c1

print(id(c1))   #2698419740624  memory locations of objects
print(id(c2))   #2698409255312  memory locations of objects
print(id(c3))   #2698419740624  memory locations of objects






