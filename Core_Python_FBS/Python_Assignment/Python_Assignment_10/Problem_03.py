# Write a program to find the second largest element in the list. 

# list1 = [20,30,40,50,60,70,80,90,110,100,10,20]
# m = list1.sort(reverse=True)
# print(list1[1])

n = int(input("Enter a numebr of elements : "))
list1 = []
for i in range(n):
    num = int(input(""))
    list1.append(num)
print(list1)

max = list1[0]
sec_max = 0
for i in range(1,len(list1)):
    if(max<list1[i]):
        sec_max = max
        max = list1[i]
    elif(sec_max < list1[i]):
        sec_max = list1[i]
print(sec_max)