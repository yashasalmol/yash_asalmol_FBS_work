def Sum(n):
    if n==0:
        return 0
    else:
        return n + Sum(n-1)
num = int(input("Enter a number : "))
result = Sum(num)
print("Sum =",result)