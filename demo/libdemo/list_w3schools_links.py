from bs4 import BeautifulSoup
import requests

WEBSITE = "https://www.w3schools.com"
response = requests.get(WEBSITE)
bs = BeautifulSoup(response.text,'html.parser')
count = 0
for a in bs.find_all("a"):
    href = a['href']
    if href.startswith("http"):
        print(href)
        count += 1
    elif not href.startswith("javascript"):
        print(WEBSITE + href)
        count += 1

print("Count = ", count)


