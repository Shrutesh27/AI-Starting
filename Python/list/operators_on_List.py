l=[1,2,3,4]
l1=[5,6,7,8]
print(l+l1)#new list will get formed no change in existing list
print(l*3)#each value print 3 times from list

for i in l:
    print(i)

l3=[1,2,4,[5,6]]
for i in l3:
    print(i)#exeuctes 4 times as last list is only 1 list

print(4 in l3)#it is true as inside direct l3 list
print(6 in l3)#it is false as 6 not direct inside current list 
#it is inside list where another list present there is value 6
print(6 in l3[3])#it will be true as 6 is inside 3rd index of l3