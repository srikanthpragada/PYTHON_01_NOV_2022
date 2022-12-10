from bs4 import BeautifulSoup
import requests
from datetime import *

WEBSITE = "http://www.srikanthtechnologies.com"
response = requests.get(WEBSITE)
bs = BeautifulSoup(response.text, 'html.parser')

table = bs.find(id="ctl00_ContentPlaceHolder1_GridView2")
rows = table.find_all("tr")
for row in rows[1:]:
    cols = row.find_all("td")
    title = cols[0].text
    stdate = cols[2].text   # dd-mon
    cd = datetime.now()
    std = datetime.strptime(f"{stdate}-{cd.year}", "%d-%b-%Y")
    days = (std - cd).days     # timedelta.days
    if days >= 0:
        msg = "days to go"
    else:
        msg = "days old"

    print(f"{title:30} {std.strftime('%d-%m-%Y')}  {days} {msg}")
