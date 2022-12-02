data = {1: "Larry Page", 2: "Jason Hunter",
        3: "Stephen Walther", 4: "Ben King"}

with open("employees.txt", "wt") as f:
    for id, name in data.items():
        f.write(f"{id},{name}\n")
