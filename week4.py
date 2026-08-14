import sys
import requests
try:
    if len(sys.argv) < 2:
        sys.exit("Missing command line argument")
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
result = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=841a8d832d18985c4d09359d3c1f534aadafa162cfddfa1c5aabab2a6fdfc7ae")
content = result.json()
price = content["data"]["priceUsd"]
price = float(price)
amount = n*price
print(f"${amount:,.4f}")

