import os


def hasString(filename, searchstring):
    with open(filename, "rt") as f:
        contents = f.read()
        return searchstring in contents


search = input("Enter search string :")

result = os.walk(r"d:\classroom\nov1p\demo")
for dirname, dirs, files in result:
    for f in files:
        filename = dirname + "\\" + f
        if filename.endswith(".py"):
            if hasString(filename, search):
                print(filename)
