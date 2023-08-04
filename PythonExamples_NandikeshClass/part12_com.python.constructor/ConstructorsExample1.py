class Person:
    compName = 'cardtronics'

    def m1(self):
        print("welocme")

    #syntax of default constructor
    def __init__(self):
        print('constructor1')
        print('constructor2')
        print('constructor3')

per = Person()  # Instantiation. Constructor is invoked at the time o=f object creation.
print(Person.compName)
per.m1()
