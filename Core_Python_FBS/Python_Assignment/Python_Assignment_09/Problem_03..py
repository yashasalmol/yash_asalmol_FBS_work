def reverse(num,rev=0):
    if num==0:
        return rev
    else:
        a = num % 10
        return reverse(num // 10,rev * 10 + a)
num = int(input("Enter a number : "))
result = reverse(num)
print(result)