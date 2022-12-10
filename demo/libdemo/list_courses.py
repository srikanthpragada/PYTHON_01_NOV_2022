from bs4 import BeautifulSoup

with open("courses.xml", "rt") as f:
    contents = f.read()

bs = BeautifulSoup(contents, "lxml-xml")
courses = bs.find_all("course")
for course in courses:
    title = course["name"]
    fee = course["fee"]
    duration = course["duration"]

    print(f"{title:30} {fee:5}  {duration:3}")
