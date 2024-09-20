import xmltodict
import pandas as pd



with open(r'C:\Users\lucas\OneDrive\Área Pessoal\MeusProjetos\Python\Python\projeto_leitura-xml-nf\DANFEBrota.xml', 'rb') as arquivoBrotas:
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
    "cnpj_vendeu": cnpj_vendeu,
    "nome_vendeu": nome_vendeu,
    "cpf_comprou": cpf_comprou,
    "nome_comprou": nome_comprou,
    "valor total": valor_total,
    "produtos": lista_produtos
}

tabela = pd.DataFrame.from_dict(resposta)
nome_arquivo = "NFs.xlsx"
tabela.to_excel(rf'C:\Users\lucas\OneDrive\Área Pessoal\MeusProjetos\Python\Python\projeto_leitura-xml-nf\{nome_arquivo}')

print(f'Seguem as Informações da NF\n {resposta}\nAs informações foram salvas no arquivo em Excel chamado: "{nome_arquivo}"')
