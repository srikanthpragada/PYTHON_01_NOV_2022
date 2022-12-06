import re

players = {}

f = open("players.txt", "rt")
for line in f.readlines():
    # Look for name
    m = re.search("[a-zA-Z ]+", line)
    if m is None:  # name not found
        continue

    name = m.group()

    # Look for age
    m = re.search(r"\d+", line)
    if m is None:  # age not found
        continue

    age = m.group()

    players[name] = age

f.close()

for name, age in sorted(players.items()):
    print(f"{name:30} {age:2}")
