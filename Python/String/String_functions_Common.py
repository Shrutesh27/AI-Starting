#Common Functions len,max,min,sorted
a="Kolkataz"
print("Length of a",len(a))
#Max,Min,Sorted works based on ACII value 
print("Maximum char from a",max(a))#print which is big as per ACII
print("maximum char from a",min(a))#print which is small as per ACII
print("Sort variable of a in ASC",sorted(a))
#sort based on ACII in asc order will get o/p in list datatype
print("Sort Variable of in desc order",sorted(a,reverse=True))

#below functions only applicable on string functios only
#Capitalized/Title/Upper/Lower/Swapcase

#capitalized: Convert only 1st letter to capital letter b->B
c="banana"
print("Capital the first letter from variable c",c.capitalize())
#Cpaitalized will never change original string
print("it is raining".capitalize())#It will get capital

#title: Convert each 1st letter from capital It Is Letter
b="It is title"
print(b.title())
print("it is string letter".title())  

#upper: convert each letter from string in Upper
b="it is upper case"
print(b.upper())
print("Shrutesh".upper())

#lower: : convert each letter from string in lower
b="It is Lower case"
print(b.lower())
print("Shrutesh".lower())

print("Shrutesh".upper().lower())#convt into lower as last
print("Shrutesh".lower().upper())#convt into upper as last

#swapcase: convt lower->upper upper->lower
b="Shrutesh is Good GUY"
print(b.swapcase())

#Count: count substring like count no. of letter in string occur
c="It is raining"
print("Count")
print(c.count("i"))#as it is case sencitive so first I ignored
print(c.count("ing"))#calculate substring
print(c.count("is"))#calculate substring
print(c.count("abc"))#calculate substring

#Find/Index: Find the index of letter or substring

#Find & Index same but
#if no value found in find o/p -1 in index error
#it is case sensitive I & i diff also give just first appreance 
#it is raining so first i at 0 so ans 0
c="It is raining"
print("Find")
print(c.find("i"))
print(c.find("raining"))#index of r will be o/p
print(c.find("x"))#if not present then -1

print("Index")
print(c.index("i"))
print(c.index("raining"))#index of r will be o/p
#print(c.index("x"))#if not present then error

#endswith/stratwith
c="it is raining"
print("Ends With")
print(c.endswith("ing"))#True
print(c.endswith("is"))#false

print("Starts with")
print(c.startswith("i"))#True
print(c.startswith("it"))#True
print(c.startswith("is"))#false

#Format: get words in btwn string from user input
#mostly used to get values later using functions
#on login Hello Shrutesh where format used
#get user name from username
c="Hello my name is {} and I am {}"
print("format")
print(c.format("Shrutesh",23))
print("Hello my name is {} and I am {}".format("Shru",34))

print("Hello my name is {1} and I am {0}".format("Shru",34))
#first 34 then shru as for above format store values in indexing
#if there is multiple values in format use it like wise in index

print("Hello my name is {name} and I am {age}".format(name="Shru",age=34))
#store using variable & pass in string

print("Hello my name is {name} and I am {age}".format(name="Shru",age=34,Weight=70))
#sometimes even value in format always not needed to use 
#if variables used atleast in each {} variables need to pass 
# no index allowed at that time
#Also can use multiple times

#isalnum / isalpha / isdecimal / isdigit / isidentifier
c="Flat20"
print("isalnum")#check value is alpha/numberic or not
print(c.isalnum())
print("".isalnum())#false as there is no value
print(" ".isalnum())#false as there is no value
print("shrutesh".isalnum())#any one accpeted
print("4".isalnum())
print("Sffh#1".isalnum())#false as used special char

print("isalpha")#check value is alphabetic or not
print("THOMBARE".isalpha())#true as only alphabetic value
print("".isalpha())#false as there is no value
print(" ".isalpha())#false as there is no value
print("Thomb244".isalpha())#false as not only alphabetic value
print("HEO#@@".isalpha())#false as not only alphabetic value special char used

print("isdigit")#check value only in digit or not
print("3422".isdigit())
print("422ghjj".isdigit())
print("321@r3".isdigit())
print("".isdigit())

print("isidentifier")
print("Hello World".isidentifier())#false as space in btwn
print("helloWorld".isidentifier())#true as there is no space
print("Hello_World".isidentifier())#true
print("hello+feke".isidentifier())#false
print("hello3feke".isidentifier())#true
print("hello#feke".isidentifier())#false

#Split: split string bases on condition
#split(),split("h") split based on h remove h
#split("pm") split bases on pm remove pm
c="Who is pm of india"
print(c.split())#Split based on spaces
print(c.split("pm"))#split based on word
print(c.split("i"))#split based on letter
print(c.split("x"))#if letter not present then no split done

#Join: Convert list into string
c=['Who', 'is', 'pm', 'of', 'india']
print(" ".join(c))#join list in string bases on space " "
print("/".join(c))

#Replace: replace letters with expected
c="My name is Shru"
print(c.replace("Shru","Shrutesh"))#replace shru to shrutesh
print(c.replace("43","fhfj"))#if not present the no change

#Strip: remove unused spaces from string
c="    shrutesh   "
print("Hi"+c)#display incorrect
print("Hi"+c.strip())#remove unused space