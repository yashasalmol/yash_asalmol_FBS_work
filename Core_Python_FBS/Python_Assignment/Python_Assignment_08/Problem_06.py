def Fibo():
    a = -1
    b = 1
    for i in range(1,n+1):
        c = a + b
        print(c)
        a = b
        b = c
n = int(input("Enter a number : "))
Fibo()