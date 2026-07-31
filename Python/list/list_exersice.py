
l4="hello how are you"
#convert each 1st letter from each word in capitalized 
# without using title 
print(l4)
l5=l4.split(" ")
l6=[]
for i in l5:
    l6.append(i.capitalize())
print(l6) #get string where each char is in string

print(" ".join(l6))

sample="abc@gmail.com"
#get first letter before @ from email
print(sample[:sample.find("@")])
#or
s1=sample[0:3]
print(s1)

l=[1,3,4,2,1,5,4]
#remove duplicate from list
l3=[]
for i in l:
    if i not in l3:
        l3.append(i)
print(l3)