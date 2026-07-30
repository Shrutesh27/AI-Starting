l=[1,2,3,4,5]
#Replace 1 with 100
l[0]=100# It will work as list in python are mutable
#Not like string it will change
print("change from 1 to 100 in list",l)
l[-1]=500
print("change 5 to 500 in list",l)

#we can change multiple vlaues using slicing
l[1:4]=[200,300,400]#change 2,3,4 to respective 200,300,400
print("Change list values using slicing",l) 

l=["Shrutesh",232,4.32,True]
l[0]="Win"
print(l)
#Using list we cange also change 
# String,Int,boolean,float and values from list
l[0:3]=[2,"Win",5] 
print(l)
#We can also add more values using this formula
l[0:3]=[1,"ddgd",4,6.4]#List got extended
print(l)

#Add items in list
#Append, extend, insert

#Append always append 1 item even it is list 
# it will only add 1 item combine list  add at end

#Extend always add multiple item in list even it single string 
#it will break string into chars

#Append: add values at end of list
l=[1,2,3,4,5]
l.append(1000)
print("Add values in string using Append",l)
l.append("hello")
print("Add values in string using Append",l)
l.append([5,3])#Add list inside list using Append
print("Add list inside list using Append",l)

#Extend: if want to add multiple values at end of list
l.extend([500,6432,True,"Shrutesh"])
print("Add multiple values in List using Extend",l)
l.extend("goa")
#in extedn if single String then 
# extend convert it into chrs and add seprately
print("extend Single string using list",l)

#Insert: if want to insert values in btwn list values
# like [1,2,"Shrutesh","gfhsddh",4545] 
#want to add world btwn 2 & shrutesh use :- insert
l.insert(2,"World")#Just pass index where to add
print(l)