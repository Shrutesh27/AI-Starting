#Concept of Indexing
a="Hello"#H=0,e=1,l=2,l=3,o=4
print(a)
print("Value of 0",a[0])

#Types of indexing
#above is Positive left to right in string H to o
print("Value of 1",a[1])

#negative indexing right to left o to H
print("Print index of -1",a[-1])
count=0
c=""
for i in a:
    c=i+c
    count+=1
print(c,"Total",count)

#Slicing extract multiple char from String
c="Hello World"
print(c[0:4])#c[strat:end] and get numbers till 3
print(c[2:])#want to print 2 on word all letters
print(c[:4])#want to print till 3 on word all letters
print(c[:])#no start no end so it will print all letters
print(c[0:8:2])
#get chars from 0 to 8 whihc includes space
# but skip by 1 char btwn if 1 was written then no skip

print(c[0:6:-1])
#if using positive indexing then we cant take negative indexing
print("negative indexing",c[-1:-8:3])
#if using Negative indexing then we cant take Positive indexing
print(c[-1::-2])
print(c[-1::-1])#reverse String
print(c[::-1])#reverse String