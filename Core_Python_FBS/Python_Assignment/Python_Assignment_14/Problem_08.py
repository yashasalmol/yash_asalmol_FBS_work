# Write a Python program to find all the anagrams and group them 
# together from a given list of strings. 
# from collections import defaultdict

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams = defaultdict(set)

for word in words:
    anagrams[''.join(sorted(word))].add(word)

print("Grouped Anagrams:", list(anagrams.values()))
