a=input("Enter Email id: ")
print(a)
print(len(a))
a_len=a.split("@")
print(a_len)
a_len=len(a_len[0])
print(a_len)

b=input("Enter Password: ")
len_pwd=len(b)
print(b)

if 7<=len(a)<20 and "@" in a and ".com" in a and " " not in a:
    print("correct email format")
    if 8<= len_pwd <=10:
        print("Correct password format")
    else:
        print("Incorrct Passowrd length")
elif "@" not in a or ".com" not in a or " " in a:
    print("incorrect email format use")
elif a_len<7 or a_len>20:
    print("email length must be btwn 7 to 20")
else:
    print("format totally wrong")