# write a program find reverse of a number 
def reverse(num,rev):
    if(num!=0):
        a = num % 10 
        rev = rev * 10 + a
        return reverse(num // 10,rev)
    else:
        return rev
num = int(input("Enter a number : "))
print(reverse(num,0))