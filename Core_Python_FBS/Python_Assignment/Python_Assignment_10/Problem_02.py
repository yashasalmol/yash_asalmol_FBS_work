num = int(input("Enter a list: "))
list1 = []
for i in range(num):
    n = int(input(""))
    list1.append(n)
print(list1)

min = list1[0]
for i in range(len(list1)):
    if(min>list1[i]):
        min = list1[i]
print(min)

max = list1[0]
for i in range(len(list1)):
    if(max<list1[i]):
        max = list1[i]
print(max)

# m1 = min(list)
# m2 = max(list)
# print(f"Min element : {m1}\nMax element : {m2}")