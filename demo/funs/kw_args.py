def details(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


details(a=10, b=20, c="abc")
details(name='Java', version=19)
