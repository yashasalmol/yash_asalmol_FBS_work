# Accept a number from user and check if this element is present in the list or 
# not. Also tell how many times it is present in the list. 

nu = int(input("Enter a nmber of elements : "))
list1 = []
for i in range(nu):
    n = int(input(""))
    list1.append(n)
print(list1)
num = int(input("Enter a number : "))
count = 0
for i in list1:
    if i == num:
        count+=1

if count>0:
    print(f"{num} present in the list {count} times")
else:
    print(f"{num} is not present in the list")