st = "This is To Counter UpperCase"

count = 0
for c in st:
    code = ord(c)
    if 65 <= code <= 90:
        count += 1

print("Count = ", count)
