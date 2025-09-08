# Python Program to Add a Key-Value Pair to the Dictionary 

dict1 = {}
n = int(input("Enter a dict range : "))
for i in range(n):
    k = input("Enter a key : ")
    v = input("Enter a value : ")
    dict1[k] = v
print(dict1)