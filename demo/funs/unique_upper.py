def unique_upper(*names):
    upper = set()
    for n in names:
        for c in n:
            if c.isupper():
                upper.add(c)

    print(upper)


def unique_upper2(*names):
    upper = set()
    for n in names:
        upper = upper | {c for c in n if c.isupper()}

    print(upper)


unique_upper2("Java", "C#", "PYthon", "SQL", "C++")
