# Sum of three digits number

num = int(input("Enter a Three digit number : "))

a = num % 10
num = num // 10
b = num % 10
c = num // 10

sum = a + b + c
print("Sum of digits is : ",sum)