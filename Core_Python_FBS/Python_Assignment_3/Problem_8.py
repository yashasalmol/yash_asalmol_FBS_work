import random

userid = input("Enter a userid : ")
password = input("Enter a password : ")
if(userid == "yash" and password == "yash1234"):
    captcha = random.randint(1000,9999)
    print("The captcha is : ",captcha)

    cap = int(input("Enter the same captcha : "))
    if(captcha == cap):
        print("Userid and password is correct ")
    else:
        print("wrong captcha!")
else:
    print("The user enter invalid userid and password.")