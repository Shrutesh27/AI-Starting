l=[1,2,4,8,9]

print("length of lsit L",len(l))

#min,max will only works if there is only int preset in list
print("Min number from list",min(l))
print("Max number from list",max(l))

l=[1,2,4,8,[4,3],9]#for this min max will get failed due to list->list
l2=[5,6,7,2,1]
l=[1,2,4,8,9]

print(min(l+l2))#Print min number from both list same for max

print("Sort l2 list",sorted(l2))

l3=[4,2,3,7,5,5,5.6,0.1]
print("create new list using sorted")
print(sorted(l3))#this will only support similar datatype
#sorted will create new list never change existing list

l3.sort()#this will permanantly change list
print("sort list permenantly using sort",l3)

print("Sort list in reverse order permenantly using sort")
l3.sort(reverse=True)
print(l3)
l3.sort()#permantly change in ASC order
print(l3)

print("get Value from list using index",l3.index(3))
