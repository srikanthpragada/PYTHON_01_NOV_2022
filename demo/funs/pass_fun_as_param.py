def printvalue(value):
    print("Value = ", value)


def printVertical(value):
    for c in value:
        print(c)


def process(value, func):
    func(value)


def add(a, b):
    return a + b


process('Hello', printvalue)
process('Hello', printVertical)
#process(10, add)
