def details(*args, **kwargs):
    print(args)
    for k, v in kwargs.items():
        print(k, v)


details(10, 20, a=10, b=20, c="abc")
details(name='Java', version=19)
