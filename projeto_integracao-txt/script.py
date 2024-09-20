with open(r"C:\Users\lucas\OneDrive\Área Pessoal\MeusProjetos\Python\Python\projeto_integracao-txt\Alunos.txt", 'r') as arquivo:
    org = 0
    anu = 0
    st = 0
    yt = 0
    igfb = 0
    linhas = arquivo.readlines()
    del linhas[:4]
    for linha in linhas:
        email, origem = linha.split(',')
        if "_org" in origem:
            org += 1
            if "hashtag_site_org" in origem:
                st += 1
            if "hashtag_yt_org" in origem:
                yt += 1
            if "hashtag_igfb_org" in origem or "hashtag_ig_org" in origem:
                igfb += 1
        else:
            anu += 1


with open("analise.txt", "w", encoding="UTF-8") as analise:
    analise.write(f'{org} alunos vieram pelo tráfego orgânico e {anu} vieram por meio de anúncios.\nDos que vieram do tráfego orgânico {st} vieram pelo site, {yt} pelo YouTube, {igfb} pelo Instagram ou pelo Facebook.')