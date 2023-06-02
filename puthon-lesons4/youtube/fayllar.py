import requests

response = requests.get(" https://v6.exchangerate-api.com/v6/0746ad590a7d31a60e036b9a/latest/USD")
print(response.json()['conversion_rates']['UZS'])


response = requests.get(" https://v6.exchangerate-api.com/v6/0746ad590a7d31a60e036b9a/pair/USD/UZS")
print(response.json()['conversion_rate'])