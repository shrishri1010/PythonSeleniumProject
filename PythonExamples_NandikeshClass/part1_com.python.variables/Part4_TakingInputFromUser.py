from builtins import float

num1 = input("Enter first number")    #10 treated as string
num2 = input("Enter second number")   #20 treated as string
print(num1+num2)   #output is 1020  (concatenated)


num1 = int(input("Enter first number"))    #10 convert into integer
num2 = int(input("Enter second number"))   #20 convert into integer
num3 = float(input("Enter third number"))
print(num1+num2+num3)   #output is in decimal