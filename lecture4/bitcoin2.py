import sys
import requests

if len(sys.argv) != 2:
    sys.exit("wrong command-line arguments")

try:
    bitcoins_to_buy = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = r.json()
    btcoin_rate = data["bpi"]["USD"]["rate"].replace(",", "")
    new_btcoin_rate = float(btcoin_rate)

except requests.RequestException:
    sys.exit("It has happend an error requesting")

cost_in_usd = bitcoins_to_buy * new_btcoin_rate
print(f"${cost_in_usd:,.4f}")
