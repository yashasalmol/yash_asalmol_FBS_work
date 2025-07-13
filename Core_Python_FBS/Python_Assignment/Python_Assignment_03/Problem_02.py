# Write a program to input any alphabet and check whether it is vowel or consonant.

alpha = input("Enter alphabets : ")

if(alpha in 'aeiouAEIOU'):
    print("The vowels.")
else:
    print("The consonent.")