def numbers():
    for i in range(1, 6):
        yield i


g = numbers()
print(g)
print(next(g))
print(next(g))
