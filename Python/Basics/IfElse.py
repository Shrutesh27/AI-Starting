email=input("Enter Email ")
#if else & nested if else used below

if "@" in email:
    password=input("Enter Password ")
    
    if email=="shru@" and password=="1234":
        print("Welcome")
    elif email=="shru@" and password!="1234":
        print("Incorrect Pass")
        password=input("Enter Password again ")
        if password=="1234":
            print("welcome")
        else:
            print("Still Incorrect Pass")
    elif email!="shru@" and password=="1234":
        print("Incorrect Email")
        email=input("Enter Email again ")
        if email=="shru@":
            print("welcome")
        else:
            print("Still Incorrect Pass Email")
    else:
        print("Incorrect Credentials")
else:
    print("Incorrect Email format")
