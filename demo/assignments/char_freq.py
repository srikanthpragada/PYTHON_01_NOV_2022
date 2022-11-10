st = "how do you do"

taken = []
for c in st:
    if c not in taken:  # do not use char if it is already taken
        print(c, st.count(c))
        taken.append(c)  # add char to list


