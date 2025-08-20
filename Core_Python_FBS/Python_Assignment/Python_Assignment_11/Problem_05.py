def Bubble(list1,count):
    for p in range(1,len(list1)):
        swap = True
        for i in range(len(list1)-p):
            if list1[i]>list1[i+1]:
                list1[i],list1[i+1]=list1[i+1],list1[i]
                count+=1
                swap = False
        if swap:
            break
    return list1,count
list1 = [10,20,30,23,70,58,92]
count = 0
result = Bubble(list1,count)
print(result)