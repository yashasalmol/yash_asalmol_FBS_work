sum=0
n = int(input("Enter a number : "))
for i in range(0,n+1):
    if(i<=n):
        print(i)
        sum += i
    i+=1
print("Sum of all series : ",sum)

    