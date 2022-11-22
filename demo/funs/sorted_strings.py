l = ["ab123", "dd322", "ab999", "de111"]

for n in sorted(l, key=lambda s: s[2:]):
    print(n)
