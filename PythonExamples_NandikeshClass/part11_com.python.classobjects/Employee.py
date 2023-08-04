class Employee :
    compName = 'test' #class variable

emp1 = Employee()   #Craetion of object nothing but "Instantiation"  --->> one object
emp1.empId=100
emp1.name='suresh'
emp1.age=35
emp1.salary=15000
print(emp1.salary)

emp2 = Employee() #Craetion of object nothing but "Instantiation"  --->> one object
emp2.empId=200
emp2.name='sathish'
emp2.age=30
emp2.salary=20000
print(emp2.salary)
print(Employee.compName)








