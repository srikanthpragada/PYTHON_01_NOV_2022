st = "This is To Counter UpperCase"

count = 0
for c in st:
    if c.isupper():
        count += 1

print("Count = ", count)
