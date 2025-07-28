def Fabonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return Fabonacci(n-1) + Fabonacci(n-2)
num = int(input("Enter a number : "))
for i in range(num):
    print(Fabonacci(i))