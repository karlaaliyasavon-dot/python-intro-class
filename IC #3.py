import requests

# A Census API URL always has this shape
# https://api.census.gov/data/{year}/{dataset}?get={variables}&for={geography}

YEAR = 2020
DATASET = "dec/pl"
URL = f"https://api.census.gov/data/{YEAR}/{DATASET}"
API_KEY = "d4ed7255c38ce7cce82b7f2bc52856d08388a5d1"

params = {
    "get":"NAME,P1_001N",
    "for":"state:*",
    "key":API_KEY
}

response = requests.get(URL, params=params)
response.raise_for_status()
print(response.url)
if response.status_code != 200:
    print(f"request failed ({response.status_code})")
    print(response.text)
    raise SystemExit(1)

data = response.json()

# The API returns a list of lists. The first row is the column
header= data[0]
rows= data[1:]

print(f"Got {len(rows)} rows back.")

print(header)
for row in rows:
    print(row)
