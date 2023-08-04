class Person:
    compName = 'cardtronics'

    #syntax of default constructor
    def __init__(self):
        print('constructor1')
        print('constructor2')
        print('constructor3')

per1 = Person()  # Instantiation
per2 = Person()  # Instantiation

print(Person.compName)