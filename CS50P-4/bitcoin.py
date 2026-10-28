import requests
import sys

if len(sys.argv) > 2:
    sys.exit("Too Many command line arguments")
elif len(sys.argv) == 1:
    sys.exit("Missing command line arguments")
try:
    bitcoin = float(sys.argv[1])
except ValueError:
    sys.exit("error")

try:
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd", headers=headers)
    response.raise_for_status()
    data = response.json()
    prix = data["bpi"]["USD"]["rate_float"]
except requests.RequestException:
    sys.exit("Error fetching data")

cout_total = bitcoin * prix
print(f"Cout total : ${cout_total:,.4f}")