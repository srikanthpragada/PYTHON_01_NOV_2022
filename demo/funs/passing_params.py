def fun(v):
    print(id(v))
    v = 0


def prepend(lst, value):
    lst.insert(0, value)


a = 100
print(id(a))
fun(a)
print(a)

l = [1, 2]
prepend(l, 10)
print(l)
