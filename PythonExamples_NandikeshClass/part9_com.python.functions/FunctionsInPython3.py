#Passing arguments with default values(positional)
def function1(i,j=100):
    print(i,j)
function1(50)
function1(200,30)   #old value is replaced with new value


#Possitional arguments with default values(positional)
def named_args(name,greeting):
    print(greeting +" "+name)
named_args("pavan" , "Hi")

#Returning multiple values from function and it returns a tuple
def bigger(i,j):
    if i>j:
        return i,j
    else:
        return j,i
x=bigger(50,100)
print(x)
print(type(x))