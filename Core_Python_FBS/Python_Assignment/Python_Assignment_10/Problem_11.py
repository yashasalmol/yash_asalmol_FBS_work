# Write a program to print all numbers 
# which are divisible by m and n in the list

list1 = [1,2,3,4,5,6,7,8,9,100]
list2 = []
m = int(input("Enter number : "))
n = int(input("Enter a numebr : "))
for i in range(len(list1)):
    if list1[i]%m==0 and list1[i]%n==0:
        list2.append(list1[i])
print(list2)