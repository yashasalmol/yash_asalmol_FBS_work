n = int(input("Enetr a number : "))
for num in range(2,n):
    count = 0
    for i in range(1,num+1):
        if(num%i==0):
            count+=1
    if(count==2):
        print(num,end=' ')