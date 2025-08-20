# Python Program to Put Even and Odd elements of a List into two Different Lists

list1 = [1,2,3,4,5,6,7,8,9]
even_list = []
odd_list = []
for num in list1:
    if num%2==0:
        even_list.append(num)
    else:
        odd_list.append(num)
print(even_list)
print(odd_list)