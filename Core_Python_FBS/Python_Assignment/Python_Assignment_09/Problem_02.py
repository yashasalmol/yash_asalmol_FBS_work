def count(n):
    if n==0:
        return 0
    else:
        return 1 + count(n // 10)

def Armstrong(n,power):
    if n == 0:
        return 0
    else:
        a = n % 10
        return (a ** power) + Armstrong(n // 10,power)

num = int(input("Enter a number : "))
digit = count(num)
result = Armstrong(num,digit)

if num == result:
    print("The number is Armstrong")
else:
    print("The number is Not Armstrong")