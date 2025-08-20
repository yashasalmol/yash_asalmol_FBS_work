# Python Program to Calculate the Number of Words and 
# the Number of Characters Present in a String 

string = input("Enter a string: ")
c_alpha = 0
c_digit = 0
for s in string:
    if s.isalpha():
        c_alpha+=1
    elif s.isdigit():
        c_digit+=1

print(f"Characters: {c_alpha} Digits: {c_digit}")