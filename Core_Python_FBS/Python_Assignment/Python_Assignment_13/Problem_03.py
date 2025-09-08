#  Python Program to Check if a Given Key Exists in a Dictionary or Not     
dict1 = {}
n = int(input("Enter a range : "))
for i in range(n):
    k = input("Enter a key : ")
    v = input("Enter a value : ")
    dict1[k] = v
print(dict1)

check = input("Enter a key you want to check : ")
if check in dict1:
    print("Yes, already present in dict")
else:    
    print("Not present in dict")
print(check)