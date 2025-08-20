# Python Program to Take in a String and Replace Every Blank Space with Hyphen 

string = input("Enetr a string: ")
new_string = ""
for ch in string:
    if ch == ' ':
        new_string += '-'
    else:
        new_string += ch
print(new_string)