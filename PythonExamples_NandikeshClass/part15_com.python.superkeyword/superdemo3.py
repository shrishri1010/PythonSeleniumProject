#super() constructor can be used in 3 ways
# To invoke parent class methods
# To invoke parent class variables
# To invoke parent class constructor

# To invoke parent class constructor
class A:
    def __init__(self):
        print("constructor from A")

class B(A):
    def __init__(self):
        print("constructor from B")
        super().__init__()    #Calls parent class constructor

obj=B()

