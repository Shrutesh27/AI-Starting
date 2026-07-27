print("Build in function Print")

a=input("Enter input build function ")
print("Type function",type(a))

a=int(5.6)
#float, str, List,tuple
print("Type converted build in Int",type(a))

#abs: jsut like modules
print(abs(4),abs(-4))
#show real number only

#pow if we pass 2 int then 
# it give power of 1st number to the 2nd number
print(pow(2,3))#2 to the power 3 :-8
print(pow(2,-3))#2 to the power 3 :0.125

#min/max: need to pass iterable string,tuble,list such kind
print("print min value",min([2,3,4,6,7,1,0.4,0.1]))
print("print max value",max([2,3,4,6,7,1,0.4,0.1]))
print("print min value from string",min("Kolkata"))
print("print max value from string",max("KolkatAT"))

#round if there is multiple decimal vlaues and want to print min use this
c=22/7
print("round",round(c,3))#print 3 values after decimal
print("round",round(c))#print only value before decimal

#divmod it return tuple divmod(x//y,x%y)
print(divmod(5,2))
#print x intdiv y, x mod y 2 results we will get

#bin/oct/hex
#get binary,octa,hexadecimal value if any value
print("Print Binary value",bin(10))
print("Print Octal value",oct(4))
print("Print hexadecimal value",hex(4))

#id to get address of any variable use this
a=3
print("Print address of given value",id(a))

#ord:- if we want ascii code of any char use this
print("get Acii code of given value",ord("c"))
print("get Acii code of given value",ord("C"))

#length: get length of iterable String,tuple,set,list,disc
#it starts from 1
print("print length of String",len("Kolkata"))
print("Print length of list",len([1,2,3,1,2]))

#sum:- get sum of iterable values must be numebric
print("print sum of numbers",sum({1,2,4,5}))
print("print sum of numbers",sum({}))

#help: to read documentation of build in function
print(help(divmod))