for i in range(1,6):
    for j in range(1,7-i):
        print(" ",end=" ")
    
    for j in range(1,i+1):
        print(j,end=" ")

    k=i-1
    for j in range(1,i):
        print(k,end=" ")
        k-=1
    print()

#           1
#         1 2 1
#       1 2 3 2 1
#     1 2 3 4 3 2 1
#   1 2 3 4 5 4 3 2 1