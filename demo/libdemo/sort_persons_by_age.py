from datetime import *
persons = {}
f = open("persons.txt", "rt")
for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 2:
        continue
    name, dobstr = parts
    try:
        dob = datetime.strptime(dobstr, "%d-%m-%Y")
        years = (datetime.now() - dob).days // 365
        persons[name] = years
    except:
        pass

f.close()

for name, age in sorted(persons.items(), key=lambda p: p[1]):
    print(f"{name:30} {age:2}")
