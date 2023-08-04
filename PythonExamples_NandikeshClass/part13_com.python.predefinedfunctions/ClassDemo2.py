#using __str__ method
class Emp:
    #syntax of parameterised constructor
    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal = sal
    def __str__(self):
        return("EmpId:{} EmpName:{} EmpSal:{}".format(self.eid,self.ename,self.sal))

e1 = Emp(101,'smith',12000)  # Instantiation. Constructor is invoked at the time o=f object creation.
print(e1)