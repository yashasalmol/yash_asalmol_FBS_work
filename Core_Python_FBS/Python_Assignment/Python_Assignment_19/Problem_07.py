nums = [i for i in range(1, 1001) for j in range(2, 10) if i % j == 0]
nums = sorted(set(nums))
print(nums)