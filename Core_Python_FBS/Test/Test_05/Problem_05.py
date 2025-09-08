list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

union = list1[:] 
for x in list2:
    if x not in union:
        union.append(x)
print("Union of lists:",union)