import requests
# request module allows us to request the data from a domain or root in domain
API_KEY = "fca_live_3OHokINBN6t1fbevviNtmxFXF5FLawl9a4Fu41Uo"
# API key is provided the website we are accessing data from 
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
# Base url consists of 
# domain (https://api.freecurrencyapi.com)
# root (/v1/latest)
# API key
CURRENCIES = ["USD","JPY","BGN","CZK","GBP","EUR","PLN","RON","CNY","INR","KRW","PHP","CAD","RUB","GBP"]

def convert_currency(base):
    # function created to convert the prompted currnecy (base) to required currency
    currencies = ",".join(CURRENCIES)
    # to concatenate the strings or items in the list using the seperator ","
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    # &base_currency={base}&currencies={currencies} is the data we are requesting from the site
    try:
        response = requests.get(url)
        # returns json format file which cant be read without converting it to python dictionary
        data = response.json()
        # data is converted into dictonary format(json -----> javaScript object notation)
        return data["data"]
    except :
        print("Invalid currency")
        return None

while True:
    country = input("Enter the currency you want to check the value for!( press q to quit ): ").upper()
    if country not in CURRENCIES:
        print("Country doesn't exist in our database.")
        continue
    if country == "Q":
        break
    amount = float(input(f"Enter the amount of {country}: "))
    required = input(f"Enter the currency you want {country} to be converted into: ").upper()
    if required not in CURRENCIES:
        print("Country doesn't exist in our database.")
        continue
    data = convert_currency(country)
    for country, value in data.items():
        if required == country:
            print(f"{country} : {value*amount}")