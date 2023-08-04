#Example 1
def my_three(a,b,c):
    print(a,b,c)

a={'a':"one",'b':"two", 'c':"three"}   #key and values are defined

my_three(**a)

#Example 2
def my_func(**kargs):
    for i,j in kargs.items():
        print(i,j)

my_func(name='shri',sports='tennis',roll=10)
