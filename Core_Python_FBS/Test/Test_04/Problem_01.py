def print_factors(n):
    print(f"Factors of {n}: ", end="")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")

num = int(input("Enter a number: "))
print_factors(num)
