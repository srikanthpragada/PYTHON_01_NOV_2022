import os

result = os.walk(r"d:\classroom\nov1p\demo")
count = 0
for dirname, dirs, files in result:
    for f in files:
        if f.endswith(".py"):
            count += 1
            print(dirname + "\\" + f)

print("Count = ", count)
