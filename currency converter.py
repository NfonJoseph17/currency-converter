from requests import  get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com"
API_KEY = "562ddaf40c95f5d58108"

printer = PrettyPrinter()

def get_currencies():
    endpoint = f"api/v7/currencies?apikey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['results']

    data = list(data.items())
    data.sort()
    return data

def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get("currencySymbol", "")
        print(f"{_id} - {name} - {symbol}")

def currency_exchange(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apikey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()
    if len(data) == 0:
        print("Invalid currencies!!")
        return

    return list(data.value())[0]

def convert(currency1,currency2, amount):
    rate = currency_exchange(currency1,currency2)
    if rate is None:
        return

    try:
        amount = float(amount)
    except:
        print("Invalid Amount. ")
        return

    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
    return converted_amount

def main():
    currencies = get_currencies()
    print("Welcome to currency converter")
    print("List - lists the different currencies")
    print("Convert - converts from one currency to another")
    print("Rate - get the exchange rate")
    print()

    while True:
        command = input("Enter a command, enter 'q' to quit").lower()

        if command == 'q':
            break
        elif command == 'list':
            print_currencies(currencies)
        elif command == 'convert':
            currency1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter amount in {currency1} ")
            currency2 = input("Enter a currency to convert to: ").upper()
            convert(currency1,currency2,amount)
        elif command == 'rate':
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            currency_exchange(currency1,currency2)
        else:
            print("Unrecognised command!")

main()