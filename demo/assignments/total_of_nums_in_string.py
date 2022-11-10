st = "100,34,45,56"

parts = st.split(",")
total = 0
for p in parts:
    total += int(p)

print(total)
