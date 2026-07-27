#to get random no use below line
import random
randomNo=random.randint(1,100)#to pick random no with range
guess=int(input("Guess Number: "))
a=1
while guess !=randomNo:
    if guess<randomNo:
        print("Guess is less than og no")
    else:
        print("Guess is higher than og no")
    guess=int(input("Guess Number: "))
    a+=1
print("correct ans you took",a,"attempt to guess correct")