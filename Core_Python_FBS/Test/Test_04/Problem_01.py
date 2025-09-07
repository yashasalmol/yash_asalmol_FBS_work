D = [2000,500,200,100,50,20,10,5]
amt = int(input("Enter amount : "))
num = 0
for i in D:
    num = amt // i
    amt = amt % i
    print(f"Rs.{i} Notes : {num}")