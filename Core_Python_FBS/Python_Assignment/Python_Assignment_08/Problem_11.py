def count(num):
    count=0
    while(num!=0):
        num = num // 10
        count+=1
    return count

def Armstrong(num):
    n = num
    dc = count(num)
    sum = 0
    while(num!=0):
        a = num % 10
        num = num // 10
        sum = sum + (a**dc)
    return sum
num = int(input("Enter a number : "))
ans = Armstrong(num)
if(ans==num):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")