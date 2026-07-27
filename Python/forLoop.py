#range function
range_multiple=list(range(1,11))#generate direct range of given integer
print(range_multiple)

#if single no so it starts from 0
range_Single=list(range(5))#print till 4
print(range_Single)

#range(start,stop,step)
range_Step=list(range(1,11,2))
#last will provide gap of 2 no btwn numbers 1 to 10
#like print even or odd no.
print(range_Step)

print(list(range(10,0,-2)))#reverse even no

#sequence any thing in order
#String: "Kolkata", list: ["Kolkata","Goa","Mumbai"]
#tuple("kolkata","goa","Mumbai")
#sets{"kolkata","goa","Mumbai"}

#in python for loop iterate on range or sequence
for i in range (1,11,2):
    print(i)#print odd 1 to 10

for i in "kolkata":
    print(i)#print value in sequence seperate

for i in [1,2,3,4,5]:
    print(i)#print 1 to 5 seperate

for i in (1,2,3,4,5):
    print(i)#print 1 to 5 seperate
for i in {1,2,3,4,5}:
    print(i)#print 1 to 5 seperate