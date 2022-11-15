def greet(*names, msg='Hello'):
    for n in names:
        print(msg, n)


greet('Scott', "Larry", "Steve", msg='Hi')
greet('Jack', 'Mark')
