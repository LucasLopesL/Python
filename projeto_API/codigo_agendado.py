import requests
from datetime import datetime

requisicao = requests.get("https://economia.awesome.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

requisicao_dict = requisicao.json()
cotacao_dolar = requisicao_dict["USDBRL"]['bid']
cotacao_euro = requisicao_dict["EURBRL"]['bid']
cotacao_bitcoin = requisicao_dict["BTCBRL"]['bid']

print(f'A cotação atualizada ({datetime.now()}) do Bitcoin, Euro e Dólar:\nDólar: R${cotacao_dolar}\nEuro: R${cotacao_euro}\nBitcoin: R${cotacao_bitcoin}')
