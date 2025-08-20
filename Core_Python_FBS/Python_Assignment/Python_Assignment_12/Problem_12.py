# Python Program to count number of lowercase characters in a string.
string = input("Enter a string : ")
c_alpha = 0
for s in string:
    if s.isalpha():
        c_alpha+=1
print(c_alpha)
error