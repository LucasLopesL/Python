from bs4 import BeautifulSoup # -> O BeautifulSoup4 interage, apenas, com páginas estáticas
import requests
import re # -> Regular Expressions


with open("projeto_web_scraping\projeto_web_scraping_bs4\Pagina Hashtag.html", "r", encoding="UTF-8") as arquivo:
    site = BeautifulSoup(arquivo, "html.parser")
    site.prettify() # -> Organiza o código HTML do site para ficar mais fácil de ler

barra_nav = site.find("nav")
links = barra_nav.find_all("a")
url_link = links[0].attrs # -> Pega todos os atributos da Tag
url_link = links[0]["href"] # Pega o atributo "href". Importante lembrar que o BS4 trata os atributos como dicionários (Chave: Valor). No caso estamos buscando o valor da chave 'href'

for link in links:
    print(link['href']) # Pegamos o atributo "href" de todos os links.


textos = site.find_all(string=re.compile("alunos"))
print(textos)


# Parent e Contents -> Parent: Pega os conteúdos acima da tag selecionada. Content: Pega os conteúdos abaixo da tag selecionada

# BS4 em sites - Site de Criptomoedas.
# A desvantagem do BS4 é que não existe um navegador controlando, portanto não tem como esperar os elementos da página corregar. Portanto, ocorrerão "AttributeError". Com isso devemos tratar esse erro expercífico com o "try" e o "except".

link = "https://coinmarketcap.com/"
requisicao = requests.get(link)
site = BeautifulSoup(requisicao.text, "html.parser")
print(site.prettify())
tbody = site.find("tbody")
linhas = tbody.find_all("tr")
for linha in linhas: # Código que pega o nome e o preço atual da moeda.
    try:
        nome = linha.find(class_="ePTNty").text
        preco = linhas.find(string=re.compile("/$"))
        print(f'{nome}: {preco}')
    except AttributeError:
        break

# Outra forma de raspagem de dados

for linha in linhas:
    try:
        info_moeda = linha.get_text(separator=";").split(";")
        print(info_moeda)
    except AttributeError:
        break

# Raspagem em forma de API

tabela = site.find("tbody")
linhas = tabela.find_all("tr")
dic_moedas = {}
for linha in linhas:
    try:
        nome = linha.find(class_ = "ePTNty").text
        codigo = linha.find(class_ = "coin-item-symbol").text
        valores = linha.find_all(string = re.compile(r"\$"))
        preco = valores[0]
        market_cap = valores[2]
        volume = valores[3]
        variacoes = linha.find_all(string = re.compile(r"\%"))
        for i, variacao in enumerate(variacoes):
            if "bQjSqS" in variacao.parent["class"]:
                variacoes[i] = "-" + str(variacao)
            else:
                continue
        var_1h = variacoes[0]
        var_24h = variacoes[1]
        var_7d = variacoes[2]
        dic = {"nome": nome, "codigo": codigo, "preco": preco, "market_cap": market_cap, "volume": volume, "var_1h": var_1h, "var_24h": var_24h, "var_7d": var_7d}
        dic_moedas[nome] = dic
    except AttributeError:
        break
