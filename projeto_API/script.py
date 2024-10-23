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
print(f'Cotação Dólar últimos 30 dias\n{[float(cotacao["bid"]) for cotacao in cotacao_usd_30d_dict]}')

# Cotação Bitcoin de Jan/2020 a Out/2020
cotacao_btc_ = requests.get("https://economia.awesomeapi.com.br/json/daily/BTC-BRL/600?start_date=20200101&end_date=20201031")
cotacao_btc_dict = cotacao_btc_.json()
lista = [float(cotacao["bid"]) for cotacao in cotacao_btc_dict]

print(f'Cotações BTC de Janeiro a Outubro de 2020:\n{lista}')

# Gráfico com as cotações de Bitcoin

import matplotlib.pyplot as plt

plt.figure(figsize=(15, 5))
plt.plot(lista)
plt.show()
