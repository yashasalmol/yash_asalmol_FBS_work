def Range(start,stop,step=1):
    current = start
    while current<stop:
        yield current
        current+=step
for i in Range(2,10,2):
    print(i)