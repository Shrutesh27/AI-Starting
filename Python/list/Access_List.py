#How to access items from List
l=[1,3,2,4]
print("get values from list using index",l[0])
print("get last values from list using index",l[-1])
print("get set of values from list",l[1:4])
print("reverse values from list",l[::-1])

#get values from Multidimentional list
#use multi [] to get list from list
l3=[1, 2, [3, 5.4, [6, 'hello', 99], 432], 235]
print(l3[2][1])#get 5.4
print(l3[2][2])#get [6, 'hello', 99]
print("get values from multidimentional list",l3)
print("get values from multidimentional list",l3[-2])
print(l3[2])
x=l3[2]
print("get values from 2D list",x[1])
print("get values from 2d arrays",l3[2][1])

#get values from 3D list
l4=l4=[[[1,2],[3,4]],[[5,6],[7,9.6]]]
print("get values from 3D list",l4[0][0][1])
print("get values from 3D list",l4[1][1][0])
print("get values from last from 3D list",l4[-1][-1][-2])