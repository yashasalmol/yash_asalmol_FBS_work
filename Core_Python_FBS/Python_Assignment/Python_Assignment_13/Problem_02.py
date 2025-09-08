#  Python Program to Concatenate Two Dictionaries Into One
dict1 = {}
n = int(input("Enter a range : "))
for i in range(n):
    k = input("Enter a key : ")
    v = int(input("Enter a value : "))
    dict1[k] = v

dict2 = {}
n = int(input("Enter a range : "))
for i in range(n):
    k = input("Enter a key : ")
    v = int(input("Enter a value : "))
    dict2[k] = v

combined = {}

for key  in dict1:
    combined[key] = dict1[key]

for key in dict2:
    combined[key] = dict2[key]

print(combined)