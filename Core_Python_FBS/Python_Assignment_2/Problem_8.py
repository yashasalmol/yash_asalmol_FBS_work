#Write a program to swap two numbers using third variable.

num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))

temp = num1
num1 = num2
num2 = temp

print("num1 is : ",num1)
print("num2 is : ",num2)