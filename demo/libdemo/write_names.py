names = ["Larry", "Jackson", "David", "Mike", "Joe"]

f = open("names.txt", "wt")

for n in names:
    f.write(n + "\n")

f.close()
