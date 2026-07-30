#----------------------------------
#Create
l=[]#empty list
print(l)
l=[1,3,2,4]#homogenious list store same datatype values
print("Homogenious List",l)
l2=["hello",3,4.5,True,5.6j]#hetrogenious list
print("Hetrogenious list",l2)

#Multidimentional list
#2d List:- list inside list 
# it is also hetrogenious store int and list
l3=[1,2,3,[4,5]]
print("2D list",l3)
#3D list: list -> list -> list
l3=[1,2,[3,5.4,[6,"hello",99],432],235]
l4=[[[1,2],[3,4]],[[5,6],[7,9.6]]]
print("3D list",l3," 3D list 2",l4)

#List Type conversion convert values inside list method to list
l5=list("Shrutesh")#[s,h,r,t,e,s,h]
print("List Type conversion",l5)
l6=list()
print(l6)
