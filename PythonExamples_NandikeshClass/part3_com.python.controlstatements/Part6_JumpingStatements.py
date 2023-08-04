#Break ---->>break the statement
# Continue  ---->> continue the statement.

#Continue statement
a = [10,30,20,20]
for m in range(len(a)):      #length 3 ---->>> 0,1,2,3
    if a[m]==20:
        print('succeed')
        continue
    else:
        print('Not succeed')
print('end')
print("***************************************************")

#break statement
for i in range(1,10):
    if i==5:
        break
    print(i)









