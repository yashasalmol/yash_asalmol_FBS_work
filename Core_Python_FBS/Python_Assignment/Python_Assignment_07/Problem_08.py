k=7
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    
    for j in range(1,k+1):
        print(" ",end=" ")
    k-=2
    for j in range(i,0,-1):
        if(j%5==0):
            print("",end="")
        else:
            print(j,end=" ")
    print()

#   1               1 
#   1 2           2 1 
#   1 2 3       3 2 1
#   1 2 3 4   4 3 2 1
#   1 2 3 4 5 4 3 2 1