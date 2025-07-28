# Write a program to find sum of digits using recursion. 

def Sum(num):
    if num==0:
        return 0
    else:
        return num % 10 + Sum(num // 10)
num = int(input("Enter a nummber : "))
result = Sum(num)
print(result)