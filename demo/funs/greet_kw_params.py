def greet(user, msg):
    print(msg, user)


greet('Rossum', 'Hi')  # positional args
greet(msg='Hello', user='Larry')  # keyword args
greet('Scott', msg='Good Morning')
