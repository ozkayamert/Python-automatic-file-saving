import requests

API_Key = "fca_live_U3RkCzO9qKmTg5bbUQjWxFqSkkcwmr5rfSsO6iyx"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_Key}"

CURRENCIES = ["USD","CAD","EUR","AUD","CNY"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("invalid currency.")
        return None

while True:    
    base = input("Enter the base currency (q for quit): ").upper()

    if base == "Q":
        break
        
    data = convert_currency(base)
    if not data:
        continue

    for ticker, value in data.items():
        print(f"{ticker}: {value}")