# ount the number of spaces in a string (take input from user) 

string = input("Enter the string : ")
count = [i for i in string if ' ' in str(i)]
print(len(count))