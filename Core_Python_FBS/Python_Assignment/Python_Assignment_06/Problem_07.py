for i in range(1,6):
    for j in range(1,7-i):
        print(" ",end=" ")
    k=65
    for j in range(1,i+1):
        print(chr(k),end=' ')
        k+=1

    for j in range(1,i):
        print(chr(k),end=" ")
        k+=1
    print()

#           A 
#         A B C 
#       A B C D E
#     A B C D E F G
#   A B C D E F G H I