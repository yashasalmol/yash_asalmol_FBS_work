passengers = int(input("Enter number of passengers : "))
ticket_cost = int(input("Enter a per ticket cost : "))
total = 0

for i in range(passengers):
    age = int(input("Enter a age : "))
    if(age<=12):
        total += ticket_cost - (ticket_cost * 0.3)
    elif(age>=59):
        total += ticket_cost - (ticket_cost * 0.5)
    else:
        total += ticket_cost

print("Total ticket amount : ",total)