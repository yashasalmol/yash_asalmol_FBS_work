start = int(input("Enter a start number : "))
stop = int(input("Enter a stop number : "))
div =  int(input("Enter a div number : "))
for i in range(start,stop):
    if(i%div==0):
        print(i)