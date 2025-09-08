# Python Program to Multiply All the Items in a Dictionary 
dict1 = {}
n = int(input("Enter a range : "))
for i in range(n):
    k = input("Enter a key : ")
    v = int(input("Enter a value : "))
    dict1[k] = v
# dict1 = {'y': 2, 'g': 3}
total = 1
for v in dict1.values():
    total *= v
print(dict1)
print(total)