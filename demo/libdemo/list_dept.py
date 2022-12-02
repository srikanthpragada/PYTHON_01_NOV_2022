dept = {}

with open("departments.txt", "rt") as f:
    for line in f:
        parts = line.strip().split(",")
        # if we don't have 2 parts (dname, ename) then ignore line
        if len(parts) < 2:
            continue
        dname, ename = parts[:2]  # unpack only first two elements
        employees = dept.setdefault(dname, [])
        employees.append(ename)

for dname, employees in dept.items():
    print(dname, ",".join(sorted(employees)))
