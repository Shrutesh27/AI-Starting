a=int(input("Enter number "))
i=1
while i<=a:
    print(i)
    i+=1

#For loop
a=list(range(1,11))#print from 1 to 10
print(a)
b=list(range(7))#print from 0 to 6
print(b)
c=list(range(1,11,2))#print odd number from1 to 10
print(c)
c=list(range(10,-1,-2))#print even no from 10 to 0 in reverse
print(c)
print(c[0:4])

for i in range(1,11,2):
    print(i)#print odd num from 1 to 10 using for loop
for i in "Kolkata":
    print(i)
for i in [1,2,4,5,3,2]:
    print(i) 