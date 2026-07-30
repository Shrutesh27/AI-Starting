#Delete values from List
#del, remove, pop, clear
l=[1,2,3,"hello",4,5,'g','o',"a"]
l2=[1, 2, [3, 5.4, [6, 'hello', 99], 432], 235]

#del: delete values from list using index or delete entire list
del l2#Delete entire list
#print(l2)

del l[0]#Delete values from list using index
print("Delete values from list using index",l)
del l[-2]
print("Delete values from list using negative index",l)
print(l)
del l[-3:]
print("Delete multiple values from list using negative index",l)

#remove: remove values from list using values not index
l.remove("hello")
print("remove values from list using values",l)

#POP:remove last value from list
print(l)
l.pop()
print("Remove last value using pop",l)

#Clear: this will never delete list it will remove all values from list
l.clear()
print("Empty list using clear",l)