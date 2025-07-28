def Fact(n):
    # Recursive Factorial 
    if n==0 or n==1:
        return 1
    else:
        return Fact(n - 1) * n

def SumSeries(n):
    # Recursive sum of factorial
    if n==0:
        return 0
    else:
        return Fact(n) + SumSeries(n-1)
n = int(input("Enter a number : "))
result = SumSeries(n)
print("Sum of series : ",result)