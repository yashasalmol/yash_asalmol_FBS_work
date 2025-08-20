def Palindrome():
    num = 0
    while True:
        if str(num) == str(num)[::-1]:
            yield num
        num+=1
gen = Palindrome()
for i in range(15):
    print(next(gen))