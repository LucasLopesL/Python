from bs4 import BeautifulSoup # -> O BeautifulSoup4 interage, apenas, com páginas estáticas
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


