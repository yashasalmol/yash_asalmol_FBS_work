#  Given two sets of numbers, write a Python program to find the missing 
# numbers in the second set as compared to the first and vice versa. 
# Use the Python set. 
A = {1, 2, 3, 4, 5}
B = {3, 4, 6, 7}

print("In A but not in B:", A - B)
print("In B but not in A:", B - A)
