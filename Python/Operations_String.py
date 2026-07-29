#Arethmatic +:- concatination *:- multiplication
#this only used on string
print("Hello"+"World")#String concatination combine 2 strings
print("*"*5)#multiply string with numbers

#Relational
print("Hello"=="World")#comparison operator
print("Hello"!="World")
print("Mumbai">"Pune")
#Lexiographically comparison
#Like in dictionary mumbai first then pune due to M first from P
#So in Lexiograpic comparison 2nd letter is big i.e. Pune greather than Mumbai
print("Pune"<"Satara")
#satara starts from S after P so it is big i.e this will be true
print("goa">"Goa")#true coz small letter come later Capital letter

#Logical
print("Hello" and "World")
#""(empty string)->in python false
#any non empty string->in pythin true
print(""and "hello")
print(" " and "hello")#this is not empty string
print("" or "world")
print("hello" or "Wolrd")
#as first it self is 1 so it will print Hello
print("Hello" and "World")
#used and op so 1st is 1 so check for 2nd 
# if it is also 1 then pass 2nd string
print("Hello" and "")#here 2nd is blank then it is false no print

#anything written then it is 1 empty then it is 0
print(not "Hello")#this is false as getting 0 
print(not "")#this is True as getting 1

#nonempty string is 1 & empty string 0

c="Hello World"
for i in c:
    print(i)#print each char seprate
print("------")
for i in c[2:7:2]:#print from 2 to 6 chars skip alternate
    print(i)#print each char seprate
print("------")
for i in c[::-1]:#print reverse sperately
    print(i)#print each char seprate

#Membership Operator in, not in
print("H" in c)#True as H has in Hello world
print("h" in c)#false as h not in Hello world
#Python is case sensitive
print("h" not in c)#here True as h not in Hello world