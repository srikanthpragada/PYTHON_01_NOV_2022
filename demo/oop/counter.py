class Counter:
    def __init__(self):
        self.value = 0

    def inc(self):
        self.value += 1

    def dec(self):
        self.value -= 1

    def reset(self):
        self.value = 0

    def getvalue(self):
        return self.value

c = Counter()
c.inc()
c.inc()
c.inc()
print(c.getvalue())
c.reset()
print(c.getvalue())
