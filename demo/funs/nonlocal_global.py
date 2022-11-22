n = 100
def fun1():
    a = 10
    global n
    n = 1

    def fun2():
        nonlocal a
        a = 20
        b = 40

    fun2()
    print(a)


fun1()
