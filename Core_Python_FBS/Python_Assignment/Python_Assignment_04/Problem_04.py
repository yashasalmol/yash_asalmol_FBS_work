# WAP to print factorial of a number.

n = int(input("Enter a number : "))
# Initalize a factorial
fact=1
for i in range(1,n+1):
    fact *= i
print("The factorial of number is  : ",fact)