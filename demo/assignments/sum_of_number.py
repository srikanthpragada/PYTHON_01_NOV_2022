
st = "90,33,44,55,ab,92"
parts = filter(str.isdigit, st.split(","))
print(sum(map(int, parts)))