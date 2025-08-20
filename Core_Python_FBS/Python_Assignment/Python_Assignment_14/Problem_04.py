# Write a Python program that finds all pairs of elements
# in a list whose sum is equal to a given value. 

# Taking number of elements
n = int(input("Enter number of elements: "))
num = []
for i in range(n):
    num.append(int(input("Enter element : ")))
target = int(input("Enter target sum : "))
print("Pairs with sum : ",target)
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i] + num[j] == target:
            print(num[i],num[j])