# Write a program to check whether a number is prime or not using recursion. 

def Prime(num,i=2):
    if num<=1:
        return False
    if i * i > num:
        return True
    if n%i==0:
        return False
    else:
        return Prime(num,i+1)
num = int(input("Enter a number : "))
if Prime(num):
    print("Prime Number ")
else:
    print("Not Prime Number ")