global_var=15    #global variable can be accessed inside the function as well as outside the function.

def printfunction():
    local_var=10     #local variables - can be accessed inside the function.
    print(global_var)

printfunction()
#print(local_var)