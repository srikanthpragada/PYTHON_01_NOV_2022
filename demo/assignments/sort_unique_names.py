data = "java,c,c,javascript,c#,java,python"
names = data.split(",")
unames = set(names)
print(sorted(unames))