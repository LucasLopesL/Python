import xmltodict
import pandas as pd
import os

def ler_xml_danfe():
    with open(rf'C:\Users\lucas\OneDrive\Área Pessoal\MeusProjetos\Python\Python\projeto_leitura-xml-nf\DANFEBrota.xml', 'rb') as arquivoBrotas:
        documento = xmltodict.parse(arquivoBrotas)

    # Valor Total, Produtos/Serviços(valores), CNPJ do vendedor, Nome do vendedor, CPJ/CNPJ do comprador, Nome do comprador

    with open(r"C:\Users\lucas\OneDrive\Área Pessoal\MeusProjetos\Python\Python\projeto_leitura-xml-nf\info-DANFEBrota.txt", 'w', encoding="UTF-8") as arquivoInfo:
        dictNF = documento['nfeProc']["NFe"]["infNFe"]
        cnpj_vendeu = dictNF["emit"]["CNPJ"]
        nome_vendeu = dictNF["emit"]["xNome"]
        cpf_comprou = dictNF["dest"]["CPF"]
        nome_comprou = dictNF["dest"]["xNome"]
        valor_total = dictNF["pag"]["detPag"]["vPag"]
        produtos = dictNF["det"]
        lista_produtos = []
        for produto in produtos:
            valor_produto = produto["prod"]["vProd"]
            nome_produto = produto["prod"]["xProd"]
            lista_produtos.append((nome_produto, valor_produto))
        arquivoInfo.write(f'Seguem as informações da NF\nNome do vendedor: {cnpj_vendeu}\nNome do vendedor: {nome_vendeu}\nCPF do comprador: {cpf_comprou}\nNome do comprador: {nome_comprou}\nValor Total {valor_total}\n Produtos comprados: {lista_produtos}')

    resposta = {
        "cnpj_vendeu": [cnpj_vendeu],
        "nome_vendeu": [nome_vendeu],
        "cpf_comprou": [cpf_comprou],
        "nome_comprou": [nome_comprou],
        "valor total": [valor_total],
        "produtos": [lista_produtos]
    }

    tabela = pd.DataFrame.from_dict(resposta)
    nome_arquivo = "NFs.xlsx"
    db = tabela.to_excel(rf'C:\Users\lucas\OneDrive\Área Pessoal\MeusProjetos\Python\Python\projeto_leitura-xml-nf\{nome_arquivo}')

    return resposta, arquivoInfo, db




def ler_xml_servico():
    with open(r'C:\Users\lucas\OneDrive\Área Pessoal\MeusProjetos\Python\Python\projeto_leitura-xml-nf\NotaCariocaHashtag.xml', 'rb') as arquivoBrotas:
        documento = xmltodict.parse(arquivoBrotas)

    # Valor Total, Produtos/Serviços(valores), CNPJ do vendedor, Nome do vendedor, CPJ/CNPJ do comprador, Nome do comprador

    with open(r"C:\Users\lucas\OneDrive\Área Pessoal\MeusProjetos\Python\Python\projeto_leitura-xml-nf\info-NotaCarioca.txt", 'w', encoding="UTF-8") as arquivoInfo:
        dictNF = documento["ConsultarNfseResposta"]["ListaNfse"]["CompNfse"]["Nfse"]["InfNfse"]
        cnpj_vendeu = dictNF["PrestadorServico"]["IdentificacaoPrestador"]["Cnpj"]
        nome_vendeu = dictNF["PrestadorServico"]["RazaoSocial"]
        cpf_comprou = dictNF["TomadorServico"]["IdentificacaoTomador"]["CpfCnpj"]["Cnpj"]
        nome_comprou = dictNF["TomadorServico"]["RazaoSocial"]
        valor_total = dictNF["Servico"]["Valores"]["ValorServicos"]
        servicos = dictNF["Servico"]["Discriminacao"]
        arquivoInfo.write(f'Seguem as informações da NF\nNome do vendedor: {cnpj_vendeu}\nNome do vendedor: {nome_vendeu}\nCPF do comprador: {cpf_comprou}\nNome do comprador: {nome_comprou}\nValor Total {valor_total}\n Produtos comprados: {servicos}')

    resposta = {
        "cnpj_vendeu": [cnpj_vendeu],
        "nome_vendeu": [nome_vendeu],
        "cpf_comprou": [cpf_comprou],
        "nome_comprou": [nome_comprou],
        "valor total": [valor_total],
        "servicos": [servicos]
    }

    tabela = pd.DataFrame.from_dict(resposta)
    nome_arquivo = "NFes.xlsx"
    db = tabela.to_excel(rf'C:\Users\lucas\OneDrive\Área Pessoal\MeusProjetos\Python\Python\projeto_leitura-xml-nf\{nome_arquivo}')

    return resposta, arquivoInfo, db

lista_arquivos = os.listdir(r"C:\Users\lucas\OneDrive\Área Pessoal\MeusProjetos\Python\Python\projeto_leitura-xml-nf")
for arquivo in lista_arquivos:
    if "xml" in arquivo:
        if "DANFE" in arquivo:
            print(ler_xml_danfe())
        else:
            print(ler_xml_servico())