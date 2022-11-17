def isodd(n: int) -> bool:
    return n % 2 == 1


l = [10, 20, 11, 15, 40, 50]
for n in filter(isodd, l):
    print(n)

for c in filter(str.isupper, "AbcDef"):
    print(c)
