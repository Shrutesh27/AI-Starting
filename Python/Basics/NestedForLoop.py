rows=int(input("Enter No. of Rows "))
for i in range(1,rows+1):
#if rows 5 required then rows+1 6 so 5 rows occur
    for j in range(0,i):
        print("*",end=" ")#want to print in same line use end=""
    print("")
print(list(range(rows+1,0,-1)))
print("---------------")
for i in range(rows+1,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print("")
