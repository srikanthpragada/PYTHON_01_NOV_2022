import requests

response = requests.get("https://restcountries.com/v3.1/all")
if response.status_code != 200:
    print("Sorry! Could not get details!")
    exit()

countries = response.json()

for c in sorted(countries, key = lambda c : c['population'], reverse=True):
    print(f"{c['name']['common']:40}  {c['region']:20}  {c['area']:10} {c['population']:10}")

