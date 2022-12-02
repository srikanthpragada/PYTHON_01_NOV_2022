f = open("names.txt", "rt")

for n in f.readlines():
    print(n, end='')

f.close()
