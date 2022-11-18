def trim(s):
    return s.strip().upper()


names = ['  abc  ', 'xyz', '  pqr', 'def  ', ' Abc', ' DEF']

for n in sorted(names, key=trim):
    print(n)
