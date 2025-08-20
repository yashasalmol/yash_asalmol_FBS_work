# Python Program to Take in a String and 
# Replace Every Blank Space with Hyphen 

string = input("Enter a string : ")
new_alpha = ""
for s in string:
    if s==" ":
        new_alpha+="-"
    else:
        new_alpha+=s
print(new_alpha)