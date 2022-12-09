import requests

code = input("Enter country code : ")
response = requests.get(f"https://restcountries.com/v3.1/alpha/{code}")
if response.status_code != 200:
    print("Sorry! Could not get details!")
    exit()

country = response.json()[0]

print(f"Name          : {country['name']['common']}")
print(f"Capital       : {country['capital'][0]}")
print(f"Population    : {country['population']}")
print(f"Area          : {country['area']}")

print("Languages : ")
for code, name in country['languages'].items():
   print(' ' * 5, name)

print("Currencies : ")
for code, details in country['currencies'].items():
    print(' ' * 5, details['name'])

print("Borders : ")
for code in country['borders']:
    print(' ' * 5,code)




