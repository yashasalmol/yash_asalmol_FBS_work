amount = int(input("Enter the amount : "))

print("Minimum notes needed : ")

for i in range(1):

    count = 0
    while amount >= 500:
        amount -= 500
        count += 1
    if count > 0:
        print("500 x", count)

    count = 0
    while amount >= 200:
        amount -= 200
        count += 1
    if count > 0:
        print("200 x", count)

    count = 0
    while amount >= 100:
        amount -= 100
        count += 1
    if count > 0:
        print("100 x", count)

    count = 0
    while amount >= 50:
        amount -= 50
        count += 1
    if count > 0:
        print("50 x", count)

    count = 0
    while amount >= 20:
        amount -= 20
        count += 1
    if count > 0:
        print("20 x", count)

    count = 0
    while amount >= 10:
        amount -= 10
        count += 1
    if count > 0:
        print("10 x", count)

