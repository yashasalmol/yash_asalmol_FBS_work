SP = int(input("Enter a selling price : "))
CP = int(input("Enter a cost price : "))

if(SP > CP):
    print("Profit.")
elif(SP < CP):
    print("Loss.")
else:
    print("no profit no loss.")