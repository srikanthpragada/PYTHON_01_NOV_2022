def upper_reverse(st):
    for c in st[::-1]:
        if c.isupper():
            print(c, end='')


upper_reverse("HeLLO")
