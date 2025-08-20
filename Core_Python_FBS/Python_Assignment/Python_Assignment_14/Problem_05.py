# Write a Python program to find the longest common prefix of all 
# strings. Use the Python set. 
def longest_common_prefix(strings):
    prefix = ""
    for i in range(len(min(strings, key=len))):
        chars = {s[i] for s in strings}
        if len(chars) == 1:
            prefix += chars.pop()
        else:
            break
    return prefix

strings = ["flower", "flow", "flight"]
print("Longest Common Prefix:", longest_common_prefix(strings))
