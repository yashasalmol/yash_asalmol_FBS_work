 # Write a program to reverse a number using recursion.

def reverse(num,rev):
    if num == 0:
        return rev
    else:
        return reverse(num // 10, rev * 10 + num % 10)
num = int(input("Enter a number : "))
result = reverse(num,0)
print(result)