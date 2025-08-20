# Python Program to Detect if Two Strings are Anagrams 
s1 = input("Enter a first String : ")
s2 = input("Enter a second string : ")
if sorted(s1)==sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")