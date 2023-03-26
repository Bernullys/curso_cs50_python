import requests
import sys
import json

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

while True:
    try:
        n_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
        break
    else:
        break
# De esto no me habia dado cuenta: el problema pide traer la info pero bajo exceptions porque puede traer errores ??? #

while True:
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response = r.json() # este metodo convierte la respuesta en un dictionnary #
        bitcoin_price = response["bpi"]["USD"]["rate_float"]
        break
    except requests.RequestsException:
        sys.exit("RequestException")
        break

ammount = n_bitcoins * bitcoin_price

print(f"${ammount:,.4f}")

