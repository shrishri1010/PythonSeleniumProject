print(list(range(10)))  ### Output ----[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(5,10)))  ### Output ----[5, 6, 7, 8, 9]
print(list(range(1,10,2)))  ### Output ----[1, 3, 5, 7, 9]   #By default starting value is 1 (initial value, max-range value is 10, increment/decrement)
print(list(range(0,10,2)))  ### Output ----[0, 2, 4, 6, 8]
print(list(range(10,1,-1)))  ### Output ----[10, 9, 8, 7, 6, 5, 4, 3, 2]
print(list(range(-10,-5)))  ### Output ----[-10, -9, -8, -7, -6]
print(list(range(-10,-5,2)))  ### Output ----[-10, -8, -6]