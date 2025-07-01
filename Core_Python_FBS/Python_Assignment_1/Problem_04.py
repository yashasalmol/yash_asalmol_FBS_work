# A program to enter p,t,r and calculate simple interest

p = float(input("Enter a principal : "))
t = float(input("Enter a Time : "))
r = float(input("Enter a Rate : "))

interest = (p * t * r)/100
# principal, Time, Rate
print("Simple interest is : ",interest)
