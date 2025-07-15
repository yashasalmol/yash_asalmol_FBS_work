# for i in range(1,5):
#     for j in range(1,6-i):
#         print(" ",end=" ")

#     for j in range(1,i+1):
#         if(i==j or j==i-4):
#             print("1 ",end=" ")
#         else:
#             print(j," ",end=" ")
#     print()

for i in range(1,4):
    for j in range(1,5-i):
        print(" ",end=" ")

    for j in range(1,i+1):
        print(j,end=' ')
    j = j+1
    for j in range(1,i):
        print(j,end=" ")
        j+=1
    print()