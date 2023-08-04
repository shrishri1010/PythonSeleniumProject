'''
#private variables can be access only within method
Private - The members of a class that are declared private are accessible within the class only,
          private access modifier is the most secure access modifier. Data members of a class are declared private
          by adding a double underscore ‘__’ symbol before the data member of that class.
'''
class Employee:
    __age=50
    def __init__(self, name, sal):
        self.__name = name    # private attribute
        self.__sal = sal       # private attribute
        print(self.__name)
        print(self.__sal)

    def displayAge(self):
        print(self.__age)
emp = Employee("Bill", 10000)
emp.displayAge()
