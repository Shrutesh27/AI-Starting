import random
random_No=random.randint(1,100)
a=int(input("Enter No."))
b=1
while a!= random_No:
    if a<random_No:
        print("No. is smaller than actual")
    else:
        print("No is greater than No.")
    a=int(input(f"Re-enter No. {b+1} time"))
    b+=1
print("Correct No is {} guessed at {}".format(a,b))