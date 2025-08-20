# Write a Python program to find the two numbers whose product is 
# maximum among all the pairs in a given list of numbers. Use the 
# Python set. 
nums = [2, 3, 5, 7, 1, 9]
nums = list(set(nums))  # remove duplicates
max_product = float('-inf')
pair = ()

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        product = nums[i] * nums[j]
        if product > max_product:
            max_product = product
            pair = (nums[i], nums[j])

print("Pair with max product:", pair, "Product:", max_product)
