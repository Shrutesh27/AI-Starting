#Strings are immutable datatype we cannot change
#once string created we cannot change 
#we can reassign but cannot change 
# we can delete also but cannot change
a="Hello"
#a[0]="x"#this is not possible
a="World"#this is possible
print(a)

#Deletion
del a
#print(a) #delete string but not complete

a="Hello"
#Delete 1st char of a it is not possible coz we cannot change string
del a[0]
print(a)

del a[:3:2]#this also wont work