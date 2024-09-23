import PyPDF2 as pyf
from pathlib import Path
import tabula
from pikepdf import Pdf, PdfImage

# Separar um PDF em vários PDF's

nome = r"Python\projeto_analise-MGLU-pdf\MGLU_ER_3T20_POR.pdf"
arquivo_pdf = pyf.PdfReader(nome)

for i, pagina in enumerate(arquivo_pdf.pages):
    num_pagina = i + 1
    novo_pdf = pyf.PdfWriter()
    novo_pdf.add_page(pagina)
    with Path(rf"Python\projeto_analise-MGLU-pdf\paginas\Arquivo Pagina {num_pagina}.pdf").open(mode="wb") as arquivo:
        novo_pdf.write(arquivo)

# Juntar varios PDF's em 1

num_paginas = [1, 14, 16]

novo_arquivo = pyf.PdfWriter()

for num in num_paginas:
    if num in num_paginas:
        pagina_pdf = pyf.PdfReader(rf"Python\projeto_analise-MGLU-pdf\paginas\Arquivo Pagina {num}.pdf")
    novo_arquivo.add_page(pagina_pdf.pages[0])

with Path(r"Python\projeto_analise-MGLU-pdf\paginas\consolidado.pdf").open(mode="wb") as arquivoConsolidado:
    novo_arquivo.write(arquivoConsolidado)

# Juntar 2 PDF's

pdf_3T_4T = pyf.PdfMerger().append(r"Python\projeto_analise-MGLU-pdf\MGLU_ER_3T20_POR.pdf")
pdf_3T_4T.append(r"Python\projeto_analise-MGLU-pdf\MGLU_ER_4T20_POR.pdf")

with Path(r"Python\projeto_analise-MGLU-pdf\paginas\pdf_3T_4T.pdf").open(mode="wb") as arquivo:
    pdf_3T_4T.write(arquivo)

# Outras manipulações de PDF's

pdf_consolidado = pyf.PdfMerger()
pdf_consolidado.append(r"Python\projeto_analise-MGLU-pdf\MGLU_ER_4T20_POR.pdf")
pdf_consolidado.merge(1, r'Python\projeto_analise-MGLU-pdf\paginas\Arquivo Pagina 1.pdf')

with Path(r"Python\projeto_analise-MGLU-pdf\paginas\comparacao.pdf").open(mode="wb") as arquivo:
    pdf_consolidado.write(arquivo)

pdf_original = pyf.PdfReader(r"Python\projeto_analise-MGLU-pdf\MGLU_ER_3T20_POR.pdf")

pdf_rotacionado = pyf.PdfWriter()

for pagina in pdf_original.pages:
    pagina.rotate(90)
    pdf_rotacionado.add_page(pagina)

with Path(r"Python\projeto_analise-MGLU-pdf\paginas\rotacionado.pdf").open(mode='wb') as arquivo:
    pdf_rotacionado.write(arquivo)

arq = pyf.PdfReader(r"Python\projeto_analise-MGLU-pdf\MGLU_ER_3T20_POR.pdf")
referencia = "| Despesas com Vendas"
for i, paginas in enumerate(arq.pages):
    texto_pagina = arq.extract_text()
    if referencia in texto_pagina:
        print("Nº da página: ", i + 1)
        texto_analisar = texto_pagina

posicao_inicial = texto_analisar.find(referencia)
posicao_final = texto_analisar.find("|", posicao_inicial + 1)
texto_final = texto_analisar[posicao_inicial:posicao_final]

print(f'As despesas com vendas da MGLU:\n{texto_pagina}')

tabelas = tabula.read_pdf(r'Python\projeto_analise-MGLU-pdf\MGLU_ER_3T20_POR.pdf', pages=5)
resultado_df = tabelas[0]
resultado_df = resultado_df.dropna(how="all", axis=0) #Exclui as linhas que estão vazias
resultado_df = resultado_df.dropna(how="all", axis=1) #Exclui as colunhas que estão vazias
resultado_df.columns = resultado_df.iloc[0] #Faz com que a primeira linha torne-se as colunas da tabela
resultado_df = resultado_df.iloc[1:]
resultado_df = resultado_df.reset_index(drop=True)


tabelas2 = tabula.read_pdf(r'Python\projeto_analise-MGLU-pdf\MGLU_ER_3T20_POR.pdf', pages=12)

for tabela in tabelas2:
    tabela = tabela.dropna(how="all", axis=0)
    tabela = tabela.reset_index(drop=True)
    # print(tabela)

capital_giro_df = tabelas2[0]
investimentos = tabelas2[1]

tabelas3 = tabula.read_pdf(r'Python\projeto_analise-MGLU-pdf\MGLU_ER_3T20_POR.pdf', pages=12, lattice=True)

capital_giro_df2 = tabelas3[0]
capital_giro_df2 = capital_giro_df2.dropna(how="all", axis=0)
capital_giro_df2 = capital_giro_df2.dropna(how="all", axis=1)
capital_giro_df2 = capital_giro_df2.reset_index(drop=True)
colunas = capital_giro_df2.iloc[0]
colunas.dropna()
capital_giro_df.columns = colunas

print(f'{capital_giro_df}\n{investimentos}')

# Extrair imagens de PDF's

pdf_imagens = Pdf.open(r'Python\projeto_analise-MGLU-pdf\MGLU_ER_3T20_POR.pdf')

for imagem in pdf_imagens.pages:
    for nome, imagem in pdf_imagens.imagens.items():
        imagem_salvar = PdfImage(imagem)
        imagem_salvar.extract_to(fileprefix=rf'Python\projeto_analise-MGLU-pdf\imagens\{nome}')
        # print(f'Nome da imagem: {nome}\nimagem:\n{imagem}')
