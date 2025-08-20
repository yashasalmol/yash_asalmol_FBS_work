# Python Program to Remove the nth Index Character from a Non-Empty String 
string = input("Enter a string : ")
n = int(input("Enter a index : "))
result = ""
for s in range(len(string)):
    if s!=n:
        result+=string[s]
print(result)