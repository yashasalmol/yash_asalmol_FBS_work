# Python Program to Sum All the Items in a Dictionary 

dict1 = {}
n = int(input("Enter a range : "))
for i in range(n):
    k = input("Enter a key : ")
    v = int(input("Enter a value : "))
    dict1[k] = v
# dict1 = {'a': 12, 'b': 13}
total = 0
for x in dict1.values():
    total += x
print("Mydict : ",dict1)
print("The total : ",total)