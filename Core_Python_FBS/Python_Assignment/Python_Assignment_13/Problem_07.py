# Python Program to Remove the Given Key from a Dictionary 

dict1 = {}
n = int(input("Enter a renage : "))
for i in range(1,n+1):
    k = input("Enter a key : ")
    v = input("Enter a value : ")
    dict1[k] = v

new_dict = {}
key_remove = input("Enter key to remove : ")
for s in dict1:
    if s!=key_remove:
        new_dict[s]=dict1[s]
print(new_dict)