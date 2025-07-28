def SumNatural(n):
    total = 0
    for i in range(1,n+1):
        total+=i
    return total
n = int(input("Enter a number : "))
print("sum of series 1 + 2 + 3 + 4 + ... + ",n,'=',SumNatural(n))

def Fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return Fact(n-1) * n
n = int(input("Enter a numebr : "))
print(f"1!+ 2! + 3! + 4! + ... + {n}! = {Fact(n)}")

def SumPower(n):
    total = 0
    for i in range(1,n+1):
        total+=i**i
    return total
n = int(input("Enter a number : ")) 
print(f"1^1 + 2^2 + 3^3+ …… {n}^n = {SumPower(n)}")