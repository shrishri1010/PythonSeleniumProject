class Employee:
    compName = 'cardtronics'

    #syntax of default constructor
    def __init__(self,empId,empName):
        self.empId=empId
        self.empName = empName
        print(f' {self.empName}.{self.empId}@company.com')
        #print(self.empName)

emp1 = Employee(empName='nandikesh',empId='hegde')

