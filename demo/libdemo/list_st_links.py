from bs4 import BeautifulSoup
import requests

WEBSITE = "http://www.srikanthtechnologies.com"
response = requests.get(WEBSITE)
bs = BeautifulSoup(response.text,'html.parser')
count = 0
for a in bs.find_all("a"):
    href = a['href']
    if href == "#" or href.startswith("javascript"):
        continue

    if href.startswith("http"): # absolute url
        print(href)
        count += 1
    else:
        if not href.startswith("/"):
             href = "/" + href   # add / when not present at the start
        print(WEBSITE + href)
        count += 1

print("Count = ", count)


