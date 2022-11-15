# positional-only args
def process(len, num, /):
    pass


process(10, 20)
# process(len=10, num=30)
