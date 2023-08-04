'''
#private methods can be access only within method
Private - The members of a class that are declared private are accessible within the class only,
          private access modifier is the most secure access modifier. Data members of a class are declared private
          by adding a double underscore ‘__’ symbol before the data member of that class.
'''
class Employee:
    def __displ(self):      #private method
        print("This is display1 method")

    def displ(self):
        print("This is display2 method")
        self.__displ()
emp = Employee()
emp.displ()
