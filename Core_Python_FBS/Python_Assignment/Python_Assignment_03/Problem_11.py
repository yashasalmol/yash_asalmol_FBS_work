p1 = int(input("Enter age of p1: "))
p2 = int(input("Enter age of p2: "))
p3 = int(input("Enter age of p3: "))
p4 = int(input("Enter age of p4: "))
p5 = int(input("Enter age of p5: "))
amount = int(input("Enter amount: "))
total = 0
if(p1 <= 12):
    total += amount - (amount * 0.3)
elif(p1 >= 59):
    total += amount - (amount * 0.5)
else:
    total += amount

if(p2 <= 12):
    total += amount - (amount * 0.3)
elif(p2 >= 59):
    total += amount - (amount * 0.5)
else:
    total += amount

if(p3 <= 12):
    total += amount - (amount * 0.3)
elif(p3 >= 59):
    total += amount - (amount * 0.5)
else:
    total += amount

if(p4 <= 12):
    total += amount - (amount * 0.3)
elif(p4 >= 59):
    total += amount - (amount * 0.5)
else:
    total += amount
if(p5 <= 12):
    total += amount - (amount * 0.3)
elif(p5 >= 59):
    total += amount - (amount * 0.5)
else:
    total += amount
print("Total amount: ",total)