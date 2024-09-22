import PyPDF2 as pyf
from pathlib import Path

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
    pdf_rotacionado.addPage(pagina)

with Path(r"Python\projeto_analise-MGLU-pdf\paginas\rotacionado.pdf").open(mode='wb') as arquivo:
    pdf_rotacionado.write(arquivo)
