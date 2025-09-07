n = int(input("Enter total number of coins (before losing): "))
coins = list(map(int, input("Enter the coin numbers: ").split()))

missing = 0
for c in coins:
    missing ^= c
print("Missing coin is:", missing)