# Python Program to Count the Number of Vowels in a String 

string = input("Enter a string: ")
count = 0
for s in string:
    if s in 'aeiouAEIOU':
        count+=1
print("Vowels : ",count)