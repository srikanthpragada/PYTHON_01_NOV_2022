# Find unique chars in 5 strings

names = ['Java', 'JavaScript', 'Python', 'C#','C++']

chars = set()
for name in names:
    chars = chars | set(name)

print(sorted(chars))

