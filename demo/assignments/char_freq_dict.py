st = "how do you do"

chars = {}
for c in set(st):
    chars[c] = st.count(c)

print(chars)