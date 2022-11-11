st = "how do you do how did you do yesterday"

words = st.split(" ")
taken = []
for w in words:
    if w not in taken:
        print(w, words.count(w))
        taken.append(w)

