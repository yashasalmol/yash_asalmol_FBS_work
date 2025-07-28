# Write a program to find sum of digits of a number. 
def SumDigit(num,sum):
    if(num!=0):
        a = num % 10
        sum = sum + a
        return SumDigit(num // 10,sum)
    else:
        return sum
n = int(input("Enter a number : "))
result = SumDigit(n,0)
print(result)