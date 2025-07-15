# a. 1! + 2! + 3! + ... + n!
n = int(input("Enter value of n for factorial series: "))
fact_sum = 0
for i in range(1, n+1):
    fact = 1
    for j in range(1, i+1):
        fact *= j
    fact_sum += fact
print("a. Sum of factorials:", fact_sum)

# b. N + N^2 + N^3 + ... + N^N
N = int(input("\nEnter value of N for exponential series: "))
exp_sum = 0
for i in range(1, N+1):
    exp_sum += N ** i
print("b. Sum of N powers from 1 to N:", exp_sum)

# c. Geometric series sum: 1 + 2 + 4 + 8 + ... up to n terms
n = int(input("\nEnter number of terms for geometric series: "))
geo_sum = 0
term = 1
for i in range(n):
    geo_sum += term
    term *= 2
print("c. Sum of geometric series:", geo_sum)

# d. S = a + a^2/2 + a^3/3 + ... + a^10/10
a = int(input("\nEnter value of a for fractional power series: "))
frac_sum = 0
for i in range(1, 11):
    frac_sum += (a ** i) / i
print("d. Fractional power series sum:", round(frac_sum, 2))

# e. x - x^2/3 + x^3/5 - x^4/7 + ... to n terms
x = int(input("\nEnter value of x for alternating series: "))
n = int(input("Enter number of terms: "))
alt_sum = 0
sign = 1
for i in range(1, n+1):
    power = i
    denom = 2 * i - 1
    term = (x ** power) / denom
    alt_sum += sign * term
    sign *= -1
print("e. Alternating series sum:", round(alt_sum, 2))
