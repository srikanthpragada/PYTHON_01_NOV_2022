nums = [10, 20, -11, 15, 40, -50]
nums2 = [1, 20, 4, 15, 45]


def compare(a, b):
    return a == b


def add(a, b):
    return a + b


for v in map(compare, nums, nums2):
    print(v)

for v in map(add, nums, nums2):
    print(v)
