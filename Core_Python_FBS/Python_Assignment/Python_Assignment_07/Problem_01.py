for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end=' ')
    for j in range(1,i+1):
        if(j==1 or i==j):
            print(" * ",end=" ")
        else:
            print("   ",end=" ")
    print()
#decreasing
for i in range(1,6):
    for j in range(1,i):
        print(" ",end=" ")
    for j in range(1,7-i):
        if(j==1 or j==6-i):
            print(" * ",end=" ")
        else:
            print("   ",end=" ")
    print()

#            *  
#          *   *  
#        *       *  
#      *           *  
#    *               *  
#    *               *  
#      *           *
#        *       *
#          *   *
#            *