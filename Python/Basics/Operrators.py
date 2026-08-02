#operations is used to perfrom operation on variables & values
#Arethmatic
x=5
y=2.4
print(x+y)
print(x-y)
print(x/y)
print(x*y)
print(x%y)
print("Power of operator",x**y)
print(x//y)#integer division even in float it convert to int

#comparision 
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)
print(x==y)
print(x!=y)

#Logical and or not
x=True
y=False
print(x or y)#even 1 value true true
print(x and y)#even one value false false
print(not y)

#Bitwise works on binary values
x=2
y=3
print(x & y)#bitwise and
print(x|y)
print(x>>2)#right shift
print(y<<3)#left shift
print(~x)

#Assignment
a=3
print(a)
a+=3
print(a)
a/=3
print("divide",a)

#identity
a=3
b=3
print(a is b)#compare values & memory location
a="hello"
b="hello"
print("hello",a is b)
a="Hello-World"
b="Hello-World"
print("Hello World",a is b)

a="Hello-World"
b="Hello-World"
print("Hello World",a is not b)
a=[1,2,3]
b=[1,2,3]
print(a is b)#false as store in new memory
a="3"
b=3
print(int(a) is b) 

a="Delhi"
print("D" in a)
print("D" not in a)

x=[1,2,3]
print(5 in x)