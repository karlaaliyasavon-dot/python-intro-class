import requests


YEAR = 2023
DATASET = "acs/acs5"
URL = f"https://api.census.gov/data/{YEAR}/{DATASET}"
API_KEY = "4fd3ba416db903a3b38441fb781e516d1023a624"

# FIPS code
print("Census Population Lookup")
print("------------------------")
print("Examples: 06 = California, 12 = Florida, 36 = New York")

state_code = input("Enter a state FIPS code: ").strip()

# API request
params = {
    "get": "NAME,B01003_001E",
    "for": f"state:{state_code}",
    "key": API_KEY,
}

# Send request
response = requests.get(url=URL, params=params)

if response.status_code != 200:
    print(f"request failed ({response.status_code})")
    print(response.text)
    raise SystemExit(1)

data = response.json()
print(response.url)
print(response)

headers = data[0]
row = data[1]

# Results
print()
print("Results")
print("---------")
print(f"{headers[0]}: {row[0]}")
print(f"{headers[1]}: {row[1]}")
print(f"{headers[2]}: {row[2]}")

