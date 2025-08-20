string = input("Enter string : ")
com = [i for i in string.split() if len(i)<5]
print(com)