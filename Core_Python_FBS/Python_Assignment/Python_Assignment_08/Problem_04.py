def SumOdd(n):
    total = 0
    for i in range(1,n+1):
        if(i%2!=0):
            print(i)
            total+=i
    return total
num = int(input("Enter a number : "))
result = SumOdd(num)
print(f"sum of all odd numbers : {result}")