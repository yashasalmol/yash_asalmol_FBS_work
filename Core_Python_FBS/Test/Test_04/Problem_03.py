for i in range(1,6):
    for j in range(1,6):
        if i==1 or j==6-i or i==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()