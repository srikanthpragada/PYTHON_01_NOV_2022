import requests

response = requests.get("https://api.github.com/users/srikanthpragada")
if response.status_code != 200:
    print("Sorry! Could not get details!")
    exit()

details = response.json()   # JSON to dict
print(f"Name       :{details['name']}")
print(f"Company    :{details['company']}")
print(f"Location   :{details['location']}")