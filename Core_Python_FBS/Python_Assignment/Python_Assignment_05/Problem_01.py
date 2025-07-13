attempt = 0
while(attempt<3):
    userid = (input("Enter userid : "))
    password = (input("Enter password : "))
    if(userid == "yash" and password == "yash123"):
        print("Login Successful!")
        break
    print("Incorrect userid and password Attempts remaining : ",2-attempt)
    attempt+=1
    
else:
    print("Too many attempts.")