'''Write a program of having n number of elements in the list and find out even 
and odd elements in that list and then create two separate lists which will have 
even elements and other will have odd elements.'''

list1 = [1,2,3,4,5,6,7,8,9]
list2 = []
list3 = []
for i in list1:
    if i%2==0:
        list2.append(i)
    else:
        list3.append(i)
print("list2 : ",list2)
print("list3 : ",list3)