nums = [10, 11, 15, 20, 25]

for n in map(lambda v: v + 2 if v % 2 == 0 else v + 1, nums):
    print(n)
