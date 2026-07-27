first_num=input("Enter first no")
second_num=input("Enter Second no")
#user input will be treated in string format
print(type(first_num))
print(first_num+second_num)
print("hello")

#type conversion convert string to number if it is possible
#types implicit:-python auto convert it
print(4+5)#9 auto convert
a=5+6+7j
print(a)#11+7j auto convert
print(4.2+2+5j)#6.2+5j auto convert
#types explicit:- user need to say python need to convert
int('4')#convert to integer 4
print(int(first_num)+float(second_num))
str(4)#convert to string
bool(1)#conv to boolean
complex(4)#o/p 4+0j
list('hello')#convert to list [h,e,l,l,o]
#int("kolkata")#not possible

a=4.4
print(int(a))
#o/p will be 4 this will never convert original value still 4.5
b="45"
print(int(a)+int(b))#output will be 49
#print(a+b)#o/p will be 4.545

#this is not type casting it is type conversion for temporary basics
first_num=int(input("Enter first no"))
second_num=int(input("Enter Second no"))
print(first_num+second_num)