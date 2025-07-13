start = int(input("Enter a start: "))
stop = int(input("Enter a stop: "))

for i in range(start, stop + 1):
    num = i
    count = 0
    temp = num
    while num != 0:
        num = num // 10
        count += 1
    num = temp
    sum = 0
    while num != 0:
        a = num % 10
        num = num // 10
        sum += (a ** count)
    if sum == temp:
        print(temp, "is an Armstrong number")
    # else:
    #     print(temp, "is Not an Armstrong number")