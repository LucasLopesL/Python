import requests
import json

cotacao = requests.get("https://economia.awesomeapi.com.br/json/all")
cotacao_dict = cotacao.json()
# print(cotacao_dict)

# Cotação dólar, bitcoin e Euro

cotacao_usd = cotacao_dict["USD"]["bid"]
cotacao_btc = cotacao_dict["BTC"]["bid"]
cotacao_euro = cotacao_dict["EUR"]["bid"]

print(f'Dólar: {cotacao_usd}\nBitcoin: {cotacao_btc}\nEuro: {cotacao_euro}')


# Cotação dólar últimos 30 dias

cotacao_usd_30d = requests.get("https://economia.awesomeapi.com.br/json/daily/USD-BRL/30")
cotacao_usd_30d_dict = cotacao_usd_30d.json()
print(f'Cotação Dólar últimos 30 dias {[cotacao["bid"] for cotacao in cotacao_usd_30d_dict]}')

