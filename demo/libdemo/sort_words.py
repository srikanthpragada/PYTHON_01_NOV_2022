import re

with open(r"d:\classroom\nov1p\old_man.txt", "rt") as f:
    contents = f.read()

words = re.findall(r"\w+", contents)

for w in sorted(set(words)):
    print(w)
